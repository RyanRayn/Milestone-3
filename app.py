import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])
    # Document stats for homepage dashboard after log in
    happy = mongo.db.entries.count_documents({"entry_emotion": "smile"})
    sad = mongo.db.entries.count_documents({"entry_emotion": "frown"})
    angry = mongo.db.entries.count_documents({"entry_emotion": "angry"})
    logs = mongo.db.entries.count_documents({})
    a = (happy/logs)
    b = round(a, 2)*100
    happyPercent = int(b)
    profiles = mongo.db.tabs.count_documents({})

    return render_template("home.html",
                           happy=happy, sad=sad, angry=angry,
                           logs=logs, happyPercent=happyPercent,
                           tabs=tabs, profiles=profiles)


# Register new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Check for existing user and flash message if one already exists
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Another account already linked to this email.")
            return redirect(url_for("register"))

        # Insert new user into db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("email").lower()
        return redirect(url_for("home", email=session["user"]))

    return render_template("register.html")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            if check_password_hash(
                                existing_user["password"],
                                request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                return redirect(url_for(
                    "home", email=session["user"]))
            else:
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# logout
@app.route("/logout")
def logout():

    session.pop("user")
    return redirect(url_for("home"))


# Get tabs from and sort alphabetically from db
@app.route("/get_tabs", methods=["GET", "POST"])
def get_tabs():
    tabs = list(mongo.db.tabs.find().sort([("tab_name", 1)]))
    # get session user username
    username = mongo.db.users.find_one(
        {"email": session["user"]})["username"]

    return render_template("tabs.html", tabs=tabs, username=username)


# Create new tab
@app.route("/add_tab", methods=["GET", "POST"])
def add_tab():
    if request.method == "POST":

        # Check if tab name already exists and flash message if it does
        existing_tab = mongo.db.tabs.find_one(
            {"tab_name": request.form.get("tab_name").lower()})

        if existing_tab:
            flash("Tab name already exists")
            return redirect(url_for("get_tabs"))

        # Insert new tab into db
        tab = {
            "tab_name": request.form.get("tab_name").lower()
        }

        mongo.db.tabs.insert_one(tab)

        # Hidden inputs into db with new tab name to avoid
        # errors when loading new profile page
        entry = {
            "entry_emotion": request.form.get("entry_emotion").lower(),
            "entry_date": request.form.get("entry_date").lower(),
            "entry_name": request.form.get("tab_name").lower(),
            "entry_subject": request.form.get("entry_subject").lower(),
            "entry_details": request.form.get("entry_details"),
            "entry_feeling": request.form.get("entry_feeling")
        }

        mongo.db.entries.insert_one(entry)
        return redirect(url_for("get_tabs"))

    return redirect(url_for("get_tabs"))


# Delete Tab
@app.route("/delete_tab/<tab_id>")
def delete_tab(tab_id):
    # Get tab name from db
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    # Delete tab from db
    mongo.db.tabs.remove({"_id": ObjectId(tab_id)})
    # Delete all tab entries from db
    tab_entries = {"entry_name": tab["tab_name"]}
    mongo.db.entries.delete_many(tab_entries)

    return redirect(url_for("get_tabs"))


@app.route("/profile/<tab_id>", methods=["GET", "POST"])
def profile(tab_id):

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])

    # Count documents for stats in profile dashboard
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    happy = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_feeling": "happy"}]})

    sad = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "frown"}]})

    angry = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "angry"}]})

    smile = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "smile"}]})

    logs = mongo.db.entries.count_documents({"entry_name": tab["tab_name"]})

    status = (smile/logs)

    # Datetime get current dates to pass into hidden inputs
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    month = datetime.utcnow().strftime("%B")
    day = datetime.utcnow().strftime("%d")
    year = datetime.utcnow().strftime("%Y")

    return render_template("profile.html", year=year, day=day, month=month,
                           tab=tab, tabs=tabs, happy=happy,
                           sad=sad, angry=angry, status=status)


# Entry modal on profile page
@app.route("/entry_form/<tab_id>", methods=["GET", "POST"])
def entry_form(tab_id):
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])

    if request.method == "POST":

        # Event entry for tab
        entry = {
            "entry_emotion": request.form.get("entry_emotion").lower(),
            "entry_feeling": request.form.get("entry_feeling").lower(),
            "entry_month": request.form.get("entry_month").lower(),
            "entry_day": request.form.get("entry_day").lower(),
            "entry_date": request.form.get("entry_date").lower(),
            "entry_year": request.form.get("entry_year").lower(),
            "entry_subject": request.form.get("entry_subject"),
            "entry_details": request.form.get("entry_details"),
            "entry_name": request.form.get("entry_name").lower()
        }
    mongo.db.entries.insert_one(entry)

    # Datetime get current dates to pass into hidden inputs
    month = datetime.utcnow().strftime("%B")
    day = datetime.utcnow().strftime("%d")
    year = datetime.utcnow().strftime("%Y")

    # Get data to search from form
    name = request.form.get("entry_name").lower()
    query = request.form.get("entry_month").lower()
    print(name)
    print(query)
    # Search db
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))

    return render_template("monthly.html", year=year, day=day, month=month,
                           tab=tab, tabs=tabs, entries=entries)


# Search Entries
@app.route("/search/<tab_id>", methods=["GET", "POST"])
def search(tab_id):

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])
    # Get tab info from db
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    # Get data to search from form
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    # Search db
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))
    # Flash message if no query results
    if len(entries) == 0:
        flash("No Results Found")

    return render_template("results.html", tab=tab, tabs=tabs, entries=entries)


# Search Results
@app.route("/results/<tab_id>", methods={"GET", "POST"})
def results(tab_id):

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])
    # Get tab info from db
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    # Get data to search from form
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    # Search db
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))
    # Flash message if no query results
    if len(entries) == 0:
        flash("No Results Found")

    return render_template("results.html", tabs=tabs, tab=tab, entry=entries)


# Edit Entries
@app.route("/edit_entry/<entry_id>/<tab_id>", methods=["GET", "POST"])
def edit_entry(entry_id, tab_id):
    if request.method == "POST":
        # Get new details from form and update db
        submit = request.form.get("new_details")

        mongo.db.entries.update({"_id": ObjectId(entry_id)},
                                {"$set": {"entry_details": submit}})

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])
    # Get tab info from db
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    # Find entry in db to edit
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})

    return render_template("success.html", tab=tab, tabs=tabs, entry=entry)


@app.route("/success/<tab_id>", methods=["GET", "POST"])
def success(tab_id):

    # Get tabs from db alphabetically for dropdown menu
    tabs = mongo.db.tabs.find().sort([("tab_name", 1)])
    # Get tab info from db
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    # Get data to search from from
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    # Search db
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))

    return render_template("results.html", tab=tab, tabs=tabs, entries=entries)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')


@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
