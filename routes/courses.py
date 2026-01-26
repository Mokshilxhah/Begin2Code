from flask import Blueprint, render_template
from data.courses_data import courses

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses')
def courses_page():
    return render_template(
        'courses.html',
        courses=courses,
        mode="courses"
    )
