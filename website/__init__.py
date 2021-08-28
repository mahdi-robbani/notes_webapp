# make website folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# create database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """Initialize the website"""

    app = Flask(__name__) # __name__ represents the name of the application's module or package
    with open("secret_key.txt", "r") as f:
        app.config['SECRET_KEY'] = f.read() #encrypts the cookies/session data
    # Let flask know we are using a database
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # Initialize datase with our website
    db.init_app(app)

    # Import blueprints
    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    # Classes need to be defined before initializing db
    from .models import User, Note
    create_database(app)

    return app    

def create_database(app):
    """Checks if database already exists for website and creates a
    database if it does not already exist"""

    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Created Database!")

