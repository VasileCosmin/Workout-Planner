from cs50 import SQL
from flask import Flask, render_template, session, redirect, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, get_exercises

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")


@app.route("/")
@login_required
def index():
  return render_template("index.html")


@app.route("/ïnfo")
@login_required
def info():
  return render_template("info.html")


@app.route("/exercises")
@login_required
def exercises():
  exercises = get_exercises()
  return render_template("exercises.html", exercises=exercises)


@app.route("/login", methods=['POST', 'GET'])
def login():
  session.clear()

  if request.method == 'POST':
    username = request.form.get("username")
    password = request.form.get("password")

    if not username:
      error = 'Enter Username!'
      return render_template("login.html", error1=error)
    elif not password:
      error = 'Enter Password!'
      return render_template("login.html", error2=error)

    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
      error = "Invalid Username And/Or Password"
      return render_template("login.html", error1 = error)

    session["user_id"] = rows[0]["id"]

    return redirect("/")

  else:
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
  if request.method == 'POST':
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    if not username:
      error = 'Enter Username!'
      return render_template("register.html", error=error)
    elif not password:
      error = 'Enter Password!'
      return render_template("register.html", error_pass=error)
    elif not confirmation:
      error= 'Enter Password Again!'
      return render_template("register.html", error_conf=error)

    if confirmation != password:
      error = 'Passwords did not match'
      return render_template("register.html", error_conf=error)

    hash = generate_password_hash(password, 'pbkdf2:sha256', 2)

    usernames = db.execute("SELECT username FROM users")

    for i in range(len(usernames)): 
      if username == usernames[i]:
        error = 'Username Already Exists!'
        return render_template("register.html", error=error)

    new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash) 

    session["user_id"] = new_user

    return redirect("/")
  else:
    return render_template("register.html")


@app.route("/signout")
@login_required
def signout():
  session.clear()

  return redirect("/login")


@app.route("/workout")
@login_required
def workout():
  return render_template("workout.html")