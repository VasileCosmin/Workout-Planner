from cs50 import SQL
from flask import Flask, flash, render_template, session, redirect, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, get_exercises

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")


@app.route("/add", methods=["POST"])
@login_required
def add():
    if request.method == "POST":
        user_id = session["user_id"]
        name = request.form.get("name")
        equipment = request.form.get("equipment")
        instructions = request.form.get("instructions")

        db.execute(
            "INSERT INTO exercises (user_id, exercise, equipment, instructions) VALUES (?, ?, ?, ?)",
            user_id,
            name,
            equipment,
            instructions,
        )

        flash("Exercise Added!")

        return redirect("/exercises")


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    user_id = session["user_id"]
    exercise = request.form.get("exercise")
    if id:
        db.execute(
            "DELETE FROM exercises WHERE exercise = ? AND user_id = ?",
            exercise,
            user_id,
        )

    flash("Exercise Removed!")

    return redirect("/workout")


@app.route("/workout")
@login_required
def workout():
    user_id = session["user_id"]
    exercises = db.execute("SELECT * FROM exercises WHERE user_id = ?", user_id)

    return render_template("workout.html", exercises=exercises)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/info")
@login_required
def info():
    return render_template("info.html")


@app.route("/exercises", methods=["GET", "POST"])
@login_required
def exercises():
    if request.method == "POST":
        muscle = request.form.get("muscles")
        exercises = get_exercises(muscle)

        return render_template("exercises.html", exercises=exercises)
    else:
        return render_template("exercises.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            error = "Enter Username!"
            return render_template("login.html", error1=error)
        elif not password:
            error = "Enter Password!"
            return render_template("login.html", error2=error)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            error = "Invalid Username And/Or Password"
            return render_template("login.html", error1=error)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            error = "Enter Username!"
            return render_template("register.html", error=error)
        elif not password:
            error = "Enter Password!"
            return render_template("register.html", error_pass=error)
        elif not confirmation:
            error = "Enter Password Again!"
            return render_template("register.html", error_conf=error)

        if confirmation != password:
            error = "Passwords did not match"
            return render_template("register.html", error_conf=error)

        hash = generate_password_hash(password, "pbkdf2:sha256", 2)

        usernames = db.execute("SELECT username FROM users")

        for i in range(len(usernames)):
            if username == usernames[i]:
                error = "Username Already Exists!"
                return render_template("register.html", error=error)

        new_user = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
        )

        session["user_id"] = new_user

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/signout")
@login_required
def signout():
    session.clear()

    return redirect("/login")
