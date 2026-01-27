from flask import Blueprint, render_template, session, redirect, url_for
from data.notes_data import NOTES
from functools import wraps
from models import db

notes_bp = Blueprint('notes', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@notes_bp.route('/notes')
@login_required
def notes_page():
    user_id = session.get("user_id")
    user = db.get_user_by_id(user_id)
    
    if not user:
        session.clear()
        return redirect('/')
    
    return render_template(
        'notes.html',
        notes=NOTES,
        user=user,
        mode="notes"
    )
