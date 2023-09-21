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
        users = cur.execute("SELECT * FROM user").fetchall()
        all_users = [{u: item[u] for u in item.keys()} for item in users]
        return all_users
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        cur=get_connection()
        user_email = request.form.get('user_email')
        user = cur.execute("SELECT user_email FROM user WHERE user_email=?", (user_email,))
        if user:
            return "Logged in!"
    else:
        return "Not a valid user!"

        
        
app.run(host="localhost", port=8000, debug=True)

