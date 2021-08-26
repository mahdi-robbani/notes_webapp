# make website folder a python package
from flask import Flask

def create_app():
    """Initialize the website"""
    app = Flask(__name__) # __name__ represents the name of the application's module or package
    with open("secret_key.txt", "r") as f:
        app.config['SECRET_KEY'] = f.read() #encrypts the cookies/session data

    # Import blueprints
    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app    