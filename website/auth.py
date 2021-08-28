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

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Get form info
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        # Checks
        if len(email) < 5:
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
            # Show message
            flash("Account created!", category="success")
            # Redirect to homepage
            return redirect(url_for('views.home')) # find which url maps to the page home (under views.py)

    return render_template("sign_up.html")
