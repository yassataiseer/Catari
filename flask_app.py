from flask import Flask, jsonify,render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sign-up.html")





if __name__ == '__main__':
    app.run(debug=True)