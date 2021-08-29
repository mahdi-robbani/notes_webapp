#URL end points/front end aspects of the website
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    """This function will run when we go to the root directory of the
    website"""
    return render_template("home.html")
