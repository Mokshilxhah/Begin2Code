from flask import (
    Blueprint, render_template,
    session, redirect, url_for,
    flash, request, jsonify
)

from data.courses_data import courses
from data.notes_data import NOTES
from data.modules_data import MODULES_DATA 

from services.email_service import send_course_purchase_email
from models import db

dash_bp = Blueprint('dashboard', __name__)

def login_required(f):
    """Decorator to check if user is logged in"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to continue", "warning")
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@dash_bp.route('/dashboard')
@login_required
def dashboard():
    user_id = session.get("user_id")
    user = db.get_user_by_id(user_id)
    
    if not user:
        flash("User not found. Please login again.", "error")
        session.clear()
        return redirect('/')
    
    user_courses_db = db.get_user_courses(user_id)
    my_courses = []
    
    for uc in user_courses_db:
        course_id = uc["course_id"]
        
        found = False
        for category_courses in courses.values():
            for course in category_courses:
                if course["id"] == course_id:
                    my_courses.append({
                        "id": course["id"],
                        "name": course["name"],
                        "icon": course["icon"],
                        "description": course["description"],
                        "progress": uc["progress_percentage"]
                    })
                    found = True
                    break
            if found:
                break
    
    return render_template(
        "dashboard.html",
        courses=courses,
        notes=NOTES,
        modules=MODULES_DATA,
        my_courses=my_courses,
        purchased_courses=[uc["course_id"] for uc in user_courses_db],
        user_email=user["email"],
        user_name=user["name"],
        user_coins=user["coins"],
        mode="dashboard"
    )

@dash_bp.route('/buy-course', methods=['POST'])
def buy_course():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first", 
            "require_login": True
        })
    
    user_id = session.get("user_id")
    user = db.get_user_by_id(user_id)
    
    if not user:
        return jsonify({
            "success": False, 
            "message": "User not found", 
            "require_login": True
        })
    
    course_id = int(request.json.get("course_id"))
    
    if db.check_course_purchased(user_id, course_id):
        return jsonify({
            "success": False, 
            "message": "Course already purchased"
        })
    
    course_found = None
    course_price = 0
    
    for category_courses in courses.values():
        for course in category_courses:
            if course["id"] == course_id:
                course_found = course
                course_price = course.get("price", 0)
                break
        if course_found:
            break
    
    if not course_found:
        return jsonify({
            "success": False, 
            "message": "Course not found"
        })
    
    user_coins = user["coins"]
    
    if user_coins < course_price:
        return jsonify({
            "success": False, 
            "message": f"Insufficient coins! You have {user_coins} coins but need {course_price} coins.",
            "low_balance": True
        })
    
    new_balance = user_coins - course_price
    db.update_user_coins(user_id, new_balance)
    db.purchase_course(user_id, course_id, course_found["name"])
    
    db.log_coin_transaction(
        user_id, 
        -course_price, 
        f"Purchased {course_found['name']}"
    )
    
    try:
        send_course_purchase_email(
            recipient_email=user["email"],
            name=user["name"],
            course_name=course_found['name'],
            course_price=course_price
        )
    except Exception as e:
        print(f"Purchase email error: {e}")
    
    return jsonify({
        "success": True, 
        "message": f"Course purchased successfully! {course_price} coins deducted.",
        "remaining_coins": new_balance
    })

@dash_bp.route('/update-progress', methods=['POST'])
def update_progress():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first"
        })
    
    user_id = session.get("user_id")
    course_id = int(request.json.get("course_id"))
    progress = int(request.json.get("progress", 0))
    
    db.update_course_progress(user_id, course_id, progress)
    
    return jsonify({
        "success": True, 
        "progress": progress
    })

@dash_bp.route('/save-lecture', methods=['POST'])
def save_lecture_route():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first",
            "require_login": True
        })
    
    user_id = session.get("user_id")
    course_id = int(request.json.get("course_id"))
    lecture_name = request.json.get("lecture_name")
    
    result = db.save_lecture(user_id, course_id, lecture_name)
    
    if result:
        return jsonify({
            "success": True, 
            "message": f"Lecture '{lecture_name}' saved successfully!"
        })
    else:
        return jsonify({
            "success": False, 
            "message": "Failed to save lecture"
        })

@dash_bp.route('/save-notes', methods=['POST'])
def save_notes_route():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first",
            "require_login": True
        })
    
    user_id = session.get("user_id")
    course_id = int(request.json.get("course_id"))
    module_id = request.json.get("module_id")
    chapter_name = request.json.get("chapter_name")
    note_text = request.json.get("note_text") or request.json.get("notes_content")
    
    note_key = f"{course_id}-{module_id}-{chapter_name}"
    
    result = db.save_notes(user_id, course_id, note_key, note_text)
    
    if result:
        return jsonify({
            "success": True, 
            "message": "Notes saved successfully!"
        })
    else:
        return jsonify({
            "success": False, 
            "message": "Failed to save notes"
        })

@dash_bp.route('/get-notes', methods=['POST'])
def get_notes_route():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first",
            "require_login": True
        })
    
    user_id = session.get("user_id")
    course_id = int(request.json.get("course_id"))
    module_id = request.json.get("module_id")
    chapter_name = request.json.get("chapter_name")
    
    note_key = f"{course_id}-{module_id}-{chapter_name}"
    
    note_text = db.get_saved_notes(user_id, course_id, note_key)
    
    return jsonify({
        "success": True, 
        "note_text": note_text
    })

@dash_bp.route('/mark-complete', methods=['POST'])
def mark_complete():
    if "user_id" not in session:
        return jsonify({
            "success": False, 
            "message": "Please login first",
            "require_login": True
        })
    
    user_id = session.get("user_id")
    course_id = int(request.json.get("course_id"))
    chapter_key = request.json.get("chapter_key") 
    
    activity = db.get_user_activity(user_id, course_id)
    completed_chapters = activity["saved_notes"].get("_completed", [])
    
    if chapter_key in completed_chapters:
        return jsonify({
            "success": False,
            "message": "Chapter already completed"
        })
    
    completed_chapters.append(chapter_key)
    activity["saved_notes"]["_completed"] = completed_chapters
    
    import json
    db.update("user_activity",
        {"saved_notes": json.dumps(activity["saved_notes"])},
        {
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}"
        }
    )
    
    current_progress = db.get_course_progress(user_id, course_id)
    new_progress = min(current_progress + 2, 100)
    
    db.update_course_progress(user_id, course_id, new_progress)
    
    return jsonify({
        "success": True, 
        "progress": new_progress,
        "message": f"Chapter marked complete! Progress: {new_progress}%"
    })
