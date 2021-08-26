#URL end points/front end aspects of the website
from flask import Blueprint # lets us define views in multiple fles

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """This function will run when we go to the root directory of the
    website"""
    return "<h1>Test</h1>"
