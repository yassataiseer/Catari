from flask import Flask, jsonify,render_template, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import sqlite3
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sign-up.html")

@app.route("/login-link")
def login_link():
    return render_template("login.html")

@app.route("/signup-link")
def signup_link():
    return render_template("sign-up.html")

@app.route("/login-user", methods = ["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]

    return "logged in"

if __name__ == '__main__':
    app.run(debug=True)