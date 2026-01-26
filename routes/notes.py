from flask import Blueprint, render_template
from data.notes_data import NOTES
notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes')
def notes_page():
    return render_template(
        'notes.html',
        notes=NOTES,
        mode="notes"
    )

