#import pytest

def test_add_users(db):
    cur = db.cursor()
    
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Luis', 'Alvarez', 'la@mail.com', '1234567', TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Amelia', 'Alvarez', 'aa@mail.com', '1234567',TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Andrea', 'Garcia', 'ag@mail.com', '1234567', FALSE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Janina', 'Wilke', 'jw@mail.com', '1234567', FALSE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Christopher', 'Wilke', 'cw@mail.com', '1234567', TRUE)")
    cur.execute("INSERT INTO user (user_name, user_last_name, is_employee) VALUES ('Liam', 'Wilke', 'lw@mail.com', '1234567', FALSE)")
    
    db.commit()


def test_add_tickets(db):
    pass


def test_add_comment(db):
    pass   