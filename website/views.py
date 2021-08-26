#URL end points/front end aspects of the website
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """This function will run when we go to the root directory of the
    website"""
    return render_template("home.html")
