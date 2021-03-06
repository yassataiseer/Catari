from flask import Flask, jsonify,render_template, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import sqlite3
import requests
from user_validator import users
from search_algorithm import find
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sign-up.html")

@app.route("/login-link")
def login_link():
    return render_template("login.html")


@app.route("/search")
def search():
    return render_template("search_engine.html")

@app.route("/search_query" , methods = ["POST","GET"])
def search_query():
    query_bar = request.form["search"]
    query_bar = str(query_bar)
    print(query_bar)
    images = find.get_value(query_bar)
    print(images)
    return render_template("images.html",images=images)

@app.route("/signup-link")
def signup_link():
    return render_template("sign-up.html")

@app.route("/login-user", methods = ["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]
    query = users.Validate_user(email,password)
    print(query)
    if query== True:
        return render_template("search_engine.html",email=email)
    else:
        return "invalid creds." 

@app.route("/sign-up", methods=["POST"])
def sign_up():
    email = request.form["email"]
    password = request.form["password"]
    insert_status = users.add_user(email,password)
    print(insert_status)
    if insert_status==True:
        return render_template("search_engine.html",email=email)
    else:
        return "invalid creds"

if __name__ == '__main__':
    app.run(debug=True)