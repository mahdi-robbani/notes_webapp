#URL end points/front end aspects of the website
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS
from flask_login import login_required, current_user
from flask import request
from flask import flash
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ["GET", "POST"])
@login_required
def home():
    """Home page of website displays Notes. Only accessible on login"""

    if request.method == "POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note must have at least one character.", category="error")
        else:
            # Add note to database based on user id
            new_note = Note(text=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user) # user current user in the home template
