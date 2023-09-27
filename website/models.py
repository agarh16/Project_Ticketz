# To store the database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_since = db.Column(db.DateTime(timezone=True), default=func.now())
    user_name = db.Column(db.String(150))
    user_last_name = db.Column(db.String(150))
    user_email = db.Column(db.String(150), unique=True)
    user_password = db.Column(db.String(150))
    is_employee = db.Column(db.Boolean)

class Ticket(db.Model, UserMixin):
    ticket_id
    ticket_date
    ticket_name
    user_id