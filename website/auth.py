#authorization
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS
from flask import request
from flask import flash # show message to user

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
        # get form info
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        #checks
        if len(email) < 5:
            flash("Email must contain at least 5 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must contain at least 2 characters.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 6:
            flash("Password must contain at least 6 characters.", category="error")
        else:
            flash("Account created!", category="success")
            #add user to database

    return  render_template("sign_up.html")
