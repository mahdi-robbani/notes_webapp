# Store database models
from . import db # import database from __init__
from flask_login import UserMixin # Custom class for our User object
from sqlalchemy.sql import func # Let sql handle the date

class Note(db.Model):
    """Class which represents the Note table in the database"""
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    # func.now lets sql use the current time
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """Class which represents the User table in the database"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstName = db.Column(db.String(100))
    notes = db.relationship('Note') # allows us to access all the notes of a user
