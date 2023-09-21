#import pytest

def test_add_users(db):
    cur = db.cursor()
    
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Luis', 'Alvarez', TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Amelia', 'Alvarez', TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Andrea', 'Garcia', FALSE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Janina', 'Wilke', FALSE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Christopher', 'Wilke', TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Liam', 'Wilke', FALSE)")
    
    db.commit()


def test_add_tickets(db):
    pass


def test_add_comment(db):
    pass   