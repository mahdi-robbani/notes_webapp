#authorization
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return  render_template("sign_up.html")
