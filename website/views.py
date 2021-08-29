#URL end points/front end aspects of the website
from flask import Blueprint # lets us define views in multiple files
from flask import render_template # lets us render HTMLS
from flask_login import login_required, current_user
from flask import request
from flask import flash
from .models import Note
from . import db
import json
from flask import jsonify

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

@views.route('delete-note', methods = ["POST"])
def delete_note():
    """Gets a POST request from a JS function to delete a note with a 
    given ID and returns an empty json as a response"""

    # use request.data instead of request.form since we are not sending
    # the request as a form
    # load data from post request as a python dict
    note = json.loads(request.data)
    # get note_id from dict
    note_id =  note['noteId']
    # find the databse entry for that note_id
    note = Note.query.get(note_id)
    # Delete database entry if it exists and the current user owns it
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    # Return an empty json object as response (flask requires a response)
    return jsonify({})
