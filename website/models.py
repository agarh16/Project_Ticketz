# To store the database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userSince = db.Column(db.DateTime(timezone=True), default=func.now())
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    isEmployee = db.Column(db.Boolean, default=False)
    tickets = db.relationship('Ticket')

class Ticket(db.Model):
    ticketId = db.Column(db.Integer, primary_key=True)
    ticketDate = db.Column(db.DateTime(timezone=True), default=func.now())
    ticketName = db.Column(db.String(150))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment')
    allStatus = db.relationship('Status')

class Comment(db.Model):
    commentId = db.Column(db.Integer, primary_key=True)
    commentDate = db.Column(db.DateTime(timezone=True), default=func.now())
    content = db.Column(db.Text)
    ticketId = db.Column(db.Integer, db.ForeignKey('ticket.ticketId'))

class Status(db.Model):
    statusId = db.Column(db.Integer, primary_key=True)
    ticketStatus = db.Column(db.String(50))
    isAssigned = db.Column(db.Boolean)
    statusDate = db.Column(db.DateTime(timezone=True), default=func.now)
    ticketId = db.Column(db.Integer, db.ForeignKey('ticket.ticketId'))