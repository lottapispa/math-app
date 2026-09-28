from flask import Flask, session
from flask import redirect, render_template, request
import sqlite3
import config, courses, users

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        user_type = request.form["type"]
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return "ERROR: the passwords don't match"

        try:
            users.register(username, password1, user_type)
        except sqlite3.IntegrityError:
            return "ERROR: username is taken"

        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            session["username"] = username
            return redirect("/frontpage")
        else:
            return "ERROR: wrong username or password"

@app.route("/logout", methods=["GET", "POST"])
def logout():
    del session["username"]
    return redirect("/")

@app.route("/frontpage", methods=["GET", "POST"])
def front_page():
    return render_template("frontpage.html")

@app.route("/elementary-math")
def elementary_math():
    return render_template("elementary-math.html")

@app.route("/addition")
def addition():
    return render_template("addition.html")

@app.route("/el-math-statistics")
def statistics():
    return render_template("el-math-statistics.html")
