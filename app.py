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
    tabs = list(mongo.db.tabs.find())
    # Document stats for bottom of homepage after log in
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

        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Another account already linked to this email.")
            return redirect(url_for("register"))

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


# Get tabs from db
@app.route("/get_tabs", methods=["GET", "POST"])
def get_tabs():
    tabs = list(mongo.db.tabs.find())
    # get session user username
    username = mongo.db.users.find_one(
        {"email": session["user"]})["username"]

    return render_template("tabs.html", tabs=tabs, username=username)


# Create new Tab
@app.route("/add_tab", methods=["GET", "POST"])
def add_tab():
    if request.method == "POST":

        existing_tab = mongo.db.tabs.find_one(
            {"tab_name": request.form.get("tab_name").lower()})

        if existing_tab:
            flash("Tab name already exists")
            return redirect(url_for("get_tabs"))

        tab = {
            "tab_name": request.form.get("tab_name").lower()
        }

        mongo.db.tabs.insert_one(tab)

        entry = {
            "entry_emotion": request.form.get("entry_emotion").lower(),
            "entry_date": request.form.get("entry_date").lower(),
            "entry_name": request.form.get("tab_name").lower()
        }

        mongo.db.entries.insert_one(entry)
        return redirect(url_for("get_tabs"))

    return redirect(url_for("get_tabs"))


# Delete Tab
@app.route("/delete_tab/<tab_id>")
def delete_tab(tab_id):
    mongo.db.tabs.remove({"_id": ObjectId(tab_id)})
    return redirect(url_for("get_tabs"))


@app.route("/profile/<tab_id>", methods=["GET", "POST"])
def profile(tab_id):
    tabs = list(mongo.db.tabs.find())

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

    if request.method == "POST":
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

    tabs = list(mongo.db.tabs.find())

    # Count documents for stats in profile dashboard
    happy = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "smile"}]})

    sad = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "frown"}]})

    angry = mongo.db.entries.count_documents(
                                            {"$and": [{"entry_name":
                                             tab["tab_name"]},
                                             {"entry_emotion": "angry"}]})

    logs = mongo.db.entries.count_documents({"entry_name": tab["tab_name"]})

    status = (happy/logs)

    # Datetime get current dates to pass into hidden inputs
    month = datetime.utcnow().strftime("%B")
    day = datetime.utcnow().strftime("%d")
    year = datetime.utcnow().strftime("%Y")

    mongo.db.entries.insert_one(entry)
    return render_template("profile.html", year=year, day=day, month=month,
                           tab=tab, tabs=tabs, happy=happy,
                           sad=sad, angry=angry, status=status)


# Search Entries
@app.route("/search/<tab_id>", methods=["GET", "POST"])
def search(tab_id):
    tabs = list(mongo.db.tabs.find())
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))

    if len(entries) == 0:
        flash("No Results Found")

    return render_template("results.html", tab=tab, tabs=tabs, entries=entries)


# Search Results
@app.route("/results/<tab_id>", methods={"GET", "POST"})
def results(tab_id):
    tabs = list(mongo.db.tabs.find())
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))

    if len(entries) == 0:
        flash("No Results Found")

    return render_template("results.html", tabs=tabs, tab=tab, entry=entries)


# Edit Entries
@app.route("/edit_entry/<entry_id>/<tab_id>", methods=["GET", "POST"])
def edit_entry(entry_id, tab_id):
    if request.method == "POST":

        submit = request.form.get("new_details")

        mongo.db.entries.update({"_id": ObjectId(entry_id)},
                                {"$set": {"entry_details": submit}})

    tabs = list(mongo.db.tabs.find())
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})

    return render_template("success.html", tab=tab, tabs=tabs, entry=entry)


@app.route("/success/<tab_id>", methods=["GET", "POST"])
def success(tab_id):
    tabs = list(mongo.db.tabs.find())
    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    name = request.form.get("search_name").lower()
    query = request.form.get("query")
    entries = list(mongo.db.entries.find(
        {"entry_name": name, "$text": {"$search": query}}))

    return render_template("results.html", tab=tab, tabs=tabs, entries=entries)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
