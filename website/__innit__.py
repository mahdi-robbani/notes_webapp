# make website folder a python package
from flask import Flask

def create_app():
    # Initiallize app
    app = Flask(__name__) # __name__ represents the name of the file
    with open("secret_key.txt", "r") as f:
        app.config['SECRET_KEY'] = f #encrypts the cookies/session data
    return app
    