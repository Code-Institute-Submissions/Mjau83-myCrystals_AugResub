import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import logging
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/crystals")
def view_crystals():
    crystals = list(mongo.db.crystals.find())
    return render_template("pages/crystals.html", crystals=crystals)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    crystals = list(mongo.db.crystals.find({"$text": {"$search": query}}))
    return render_template("pages/crystals.html", crystals=crystals)

# Register page 
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

# Login page
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
                    return redirect(url_for(
                        "view_crystals", username=session["user"]))
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

# Add a new crystal to db
@app.route("/add_crystal", methods=["GET", "POST"])
def add_crystal():
    if request.method == "POST":
        is_waterproof = "yes" if request.form.get("is_waterproof") else "no"
        is_sunproof = "yes" if request.form.get("is_sunproof") else "no"
        crystal = {
            "crystal_name": request.form.get("crystal_name"),
            "color": request.form.get("color"),
            "usage": request.form.get("usage"),
            "is_waterproof": is_waterproof,
            "is_sunproof": is_sunproof,
            "name_of_chakra": request.form.get("name_of_chakra"),
            "quantity": request.form.get("quantity"),
            "date_used": request.form.get("date_used"),
            "name_of_method": request.form.get("name_of_method"),
            "notes": request.form.get("notes")
        }
        mongo.db.crystals.insert_one(crystal)
        flash("You Just Added A Crystal!")
        return redirect(url_for("view_crystals"))

    chakras = mongo.db.chakras.find().sort("chakras", 1)
    usage_method = mongo.db.usage_method.find().sort("usage_method", 1)
    return render_template("pages/add_crystal.html", chakras=chakras, 
        usage_method=usage_method)

# Edit crystal
@app.route("/edit_crystal/<crystal_id>", methods=["GET", "POST"])
def edit_crystal(crystal_id):
    if request.method == "POST":
        is_waterproof = "yes" if request.form.get("is_waterproof") else "no"
        is_sunproof = "yes" if request.form.get("is_sunproof") else "no"
        edit = {
            "crystal_name": request.form.get("crystal_name"),
            "color": request.form.get("color"),
            "usage": request.form.get("usage"),
            "is_waterproof": is_waterproof,
            "is_sunproof": is_sunproof,
            "name_of_chakra": request.form.get("name_of_chakra"),
            "quantity": request.form.get("quantity"),
            "date_used": request.form.get("date_used"),
            "name_of_method": request.form.get("name_of_method"),
            "notes": request.form.get("notes")
        }
        mongo.db.crystals.update({"_id": ObjectId(crystal_id)}, edit)
        flash("Your Crystal Is Updated!")

    crystal = mongo.db.crystals.find_one({"_id": ObjectId(crystal_id)})
    chakras = mongo.db.crystals.find().sort("chakras", 1)
    usage_method = mongo.db.usage_method.find().sort("usage_method", 1)
    return render_template("pages/edit_crystal.html", crystal=crystal, 
        chakras=chakras, usage_method=usage_method)

# Delete crystal
@app.route("/delete_crystal/<crystal_id>")
def delete_crystal(crystal_id):
    mongo.db.crystals.remove({"_id": ObjectId(crystal_id)})
    flash("Your Crystal Is Deleted!")
    return redirect(url_for("view_crystals"))


@app.route("/journal")
def view_entries():
    logs = mongo.db.crystal_log()
    return render_template("pages/journal.html", logs=logs)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
