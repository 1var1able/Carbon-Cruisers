from flask import Flask, render_template, session, redirect, url_for, request
from datetime import timedelta

app = Flask(__name__)


@app.route("/home")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign-up")
def signup():
    return render_template("signup.html")

@app.route("/individual")
def individual():
    return render_template("individualplan.html")

@app.route("/friends")
def friends():
    return render_template("friendsplan.html")

@app.route("/family")
def family():
    return render_template("familyplan.html")


if __name__ == "__main__":
    app.run(debug = True)