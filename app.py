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

    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "home", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# logout
@app.route("/logout")
def logout():

    session.pop("user")
    return redirect(url_for("home"))


@app.route("/get_tabs", methods=["GET", "POST"])
def get_tabs():
    # get tabs from db
    tabs = list(mongo.db.tabs.find())
    # get session user username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template("tabs.html", tabs=tabs, username=username)


@app.route("/add_tab", methods=["GET", "POST"])
def add_tab():
    if request.method == "POST":
        tab = {
            "tab_name": request.form.get("tab_name")
        }
        mongo.db.tabs.insert_one(tab)
        return redirect(url_for("get_tabs"))

    return redirect(url_for("get_tabs"))


@app.route("/edit_tab/<tab_id>", methods=["GET", "POST"])
def edit_tab(tab_id):
    if request.method == "POST":
        submit = {
            "tab_name": request.form.get("new_tab_name")
        }
        mongo.db.tabs.update({"_id": ObjectId(tab_id)}, submit)
        return redirect(url_for("get_tabs"))

    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    return render_template("tabs.html", tab=tab)


@app.route("/delete_tab/<tab_id>")
def delete_tab(tab_id):
    mongo.db.tabs.remove({"_id": ObjectId(tab_id)})
    return redirect(url_for("get_tabs"))


@app.route("/profile/<tab_id>", methods=["GET", "POST"])
def profile(tab_id):

    tab = mongo.db.tabs.find_one({"_id": ObjectId(tab_id)})
    month = datetime.utcnow().strftime("%B")
    day = datetime.utcnow().strftime("%d")
    year = datetime.utcnow().strftime("%Y")

    return render_template(
        "profile.html", year=year, day=day, month=month, tab=tab)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
