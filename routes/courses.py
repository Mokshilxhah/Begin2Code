from flask import Blueprint, render_template, session, redirect, url_for
from data.courses_data import courses
from functools import wraps
from models import db

courses_bp = Blueprint('courses', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@courses_bp.route('/courses')
@login_required
def courses_page():
    user_id = session.get("user_id")
    user = db.get_user_by_id(user_id)
    
    if not user:
        session.clear()
        return redirect('/')
    
    user_courses_db = db.get_user_courses(user_id)
    purchased_ids = [uc["course_id"] for uc in user_courses_db]
    
    return render_template(
        'courses.html',
        courses=courses,
        purchased_courses=purchased_ids,
        user=user,
        mode="courses"
    )
