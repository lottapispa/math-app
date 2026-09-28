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
    # Check user type
    #courses = courses.get_courses()
    #return render_template("frontpage.html", courses=courses)
    return render_template("frontpage.html")

@app.route("/new_course", methods=["GET", "POST"])
def new_course():
    if request.method == "GET":
        return render_template("add-course.html")
    if request.method == "POST":
        name = request.form["name"]
        teacher_id = session["id"]
        try:
            course_id = courses.add_course(name, teacher_id)
            return redirect("/new_course", course_name=name, course_id=course_id)
        except sqlite3.IntegrityError:
            return "ERROR"

@app.route("/new_lesson", methods=["GET", "POST"])
def new_lesson():
    if request.method == "GET":
        return render_template("add-course.html")
    if request.method == "POST":
        course_name = request.form["course_name"]
        course_id = request.form["course_id"]
        name = request.form["lessonname"]
        material = request.form["content"]
        file = request.form["file"]
        try:
            courses.add_lesson(course_id, name, material, file)
            return redirect("/new_course", course_name=course_name, course_id=course_id)
        except sqlite3.IntegrityError:
            return "ERROR"

@app.route("/new_test", methods=["GET", "POST"])
def new_test():
    if request.method == "GET":
        return render_template("add-test.html")
    if request.method == "POST":
        course_name = request.form["course_name"]
        course_id = request.form["course_id"]
        name = request.form["testname"]
        try:
            test_id = courses.add_test(course_id, name)
            return redirect("/new_test", course_name=course_name, course_id=course_id, test_id=test_id)
        except sqlite3.IntegrityError:
            return "ERROR"
    
@app.route("/new_exercise", methods=["GET", "POST"])
def new_exercise():
    # This includes adding to databases exercises and answers
    if request.method == "GET":
        return render_template("add-test.html")
    if request.method == "POST":
        course_name = request.form["course_name"]
        course_id = request.form["course_id"]
        test_id = request.form["test_id"]
        question = request.form["question"]
        type = request.form["type"]
        correct_answer = request.form["answer"]
        try:
            courses.add_exercise(test_id, question, type, correct_answer)
            return redirect("/new_test", course_name=course_name, course_id=course_id, test_id=test_id)
        except sqlite3.IntegrityError:
            return "ERROR"
