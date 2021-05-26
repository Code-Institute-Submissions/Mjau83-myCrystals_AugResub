import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template('pages/index.html')


@app.route("/crystals")
def view_crystals():
    crystals = list(mongo.db.crystals.find())
    return render_template("pages/crystals.html", crystals=crystals)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # does username already exists?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You are registered and can start to add your crystals!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("pages/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # does username already exists?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # does password match user?
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("The Username and/or Password is incorrect. Please try again")
                return redirect(url_for("login"))

        else:
            # username dosen't exist
            flash("The Username and/or Password is incorrect. Please try again")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/<username>", methods=["GET", "POST"])
def profile(username):
    # grab only the user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("pages/crystals.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # log out user and remove cookies
    flash("You are logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_crystal")
def add_crystal():
    chakras = mongo.db.chakras.find().sort("chakras", 1)
    return render_template("pages/add_crystal.html", chakras=chakras)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
