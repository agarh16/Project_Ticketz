import sqlite3
from test_project_ticketz import test_add_users

def create_db(name="main.db"):
     """Creates the database and the tables from the schema.sql. As a default it creates a "main" database.
     :param name: Name of the database.
     :return: A database
     """

     db = sqlite3.connect(name)
     with open("schema.sql") as schema: 
        db.executescript(schema.read())

        test_add_users(db)
     
        return db

    

def add_users(db):
    cur = db.cursor()
    
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES (?, ?, ?)")
    
    db.commit()     

def add_tickets(db):
    pass
def add_note(db):
    pass   