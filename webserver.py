import sqlite3
from flask import Flask, request
from flask_cors import CORS
from create_db import create_db


create_db("main.db")

def get_connection():
    connection = sqlite3.connect("main.db")
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
CORS(app)


@app.route("/users", methods=['GET'])
def get_users():
    if request.method == "GET":
        cur = get_connection()
        cur.execute("SELECT * FROM user").fetchall()
        
