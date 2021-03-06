#authorization
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS
from flask import request
from flask import flash # show message to user
from flask import redirect
from flask import url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    """Log in page of the website"""
    
    if request.method == "POST":
        # Get user info
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                # Keep user logged in unless they remove their cache
                # or server restarts
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    """Log out user and return to log in page"""
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
    """Sign up page of the website"""

    if request.method == "POST":
        # Get form info
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        # Checks
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 5:
            flash("Email must contain at least 5 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must contain at least 2 characters.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 6:
            flash("Password must contain at least 6 characters.", category="error")
        else:
            # Add user to database
            new_user = User(email=email, 
                            first_name=first_name, 
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # Login user
            flash("Account created!", category="success")
            login_user(user, remember=True)
            # Redirect to homepage
            return redirect(url_for('views.home')) # find which url maps to the page home (under views.py)

    return render_template("sign_up.html", user=current_user)
