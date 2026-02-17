from flask import Blueprint, render_template, session, redirect, url_for, send_from_directory, abort, jsonify
from data.notes_data import NOTES
from functools import wraps
from models import db
import os

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

@notes_bp.route('/download-note/<note_type>/<path:filename>')
@login_required
def download_note(note_type, filename):
    """Download notes PDF files"""
    try:
        static_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
        file_path = os.path.join(static_folder, note_type, filename)
        
        if not os.path.exists(file_path):
            return jsonify({"error": "File not available yet"}), 404
        
        directory = os.path.join(static_folder, note_type)
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        print(f"Download error: {e}")
        return jsonify({"error": "File not available yet"}), 404
