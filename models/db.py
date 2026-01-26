import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Supabase environment variables not set")

HEADERS = {
    "apikey": SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}


# CORE DATABASE FUNCTIONS
def fetch(table, params=None):
    """Read data from Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def insert(table, data):
    """Insert data into Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def update(table, data, match):
    """Update data in Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.patch(url, headers=HEADERS, json=data, params=match)
    response.raise_for_status()
    return response.json()

def delete(table, match):
    """Delete data from Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.delete(url, headers=HEADERS, params=match)
    response.raise_for_status()
    return response.json()


# USER FUNCTIONS
def get_user_by_email(email):
    """Get user by email"""
    try:
        users = fetch("users", params={"email": f"eq.{email}", "select": "*"})
        return users[0] if users else None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None

def get_user_by_id(user_id):
    """Get user by ID"""
    try:
        users = fetch("users", params={"id": f"eq.{user_id}", "select": "*"})
        return users[0] if users else None
    except Exception as e:
        print(f"Error fetching user by ID: {e}")
        return None

def create_user(name, email, password_hash):
    """Create a new user with default 5000 coins"""
    try:
        user_data = {
            "name": name,
            "email": email,
            "password": password_hash,
            "coins": 5000,
            "streak": 0
        }
        result = insert("users", user_data)
        return result[0] if result else None
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def update_user_coins(user_id, new_coin_amount):
    """Update user's coin balance"""
    try:
        return update("users", {"coins": new_coin_amount}, {"id": f"eq.{user_id}"})
    except Exception as e:
        print(f"Error updating coins: {e}")
        return None


# USER COURSES FUNCTIONS
def get_user_courses(user_id):
    """Get all courses purchased by user"""
    try:
        return fetch("user_courses", params={
            "user_id": f"eq.{user_id}",
            "select": "*"
        })
    except Exception as e:
        print(f"Error fetching user courses: {e}")
        return []

def check_course_purchased(user_id, course_id):
    """Check if user has already purchased a course"""
    try:
        result = fetch("user_courses", params={
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}"
        })
        return len(result) > 0
    except Exception as e:
        print(f"Error checking course purchase: {e}")
        return False

def purchase_course(user_id, course_id, course_name):
    """Add a purchased course to user_courses"""
    try:
        purchase_data = {
            "user_id": user_id,
            "course_id": course_id,
            "course_name": course_name,
            "progress_percentage": 0,
            "completed": False
        }
        return insert("user_courses", purchase_data)
    except Exception as e:
        print(f"Error purchasing course: {e}")
        return None

def update_course_progress(user_id, course_id, progress_percentage):
    """Update course progress percentage"""
    try:
        result = update("user_courses", 
            {"progress_percentage": progress_percentage},
            {
                "user_id": f"eq.{user_id}",
                "course_id": f"eq.{course_id}"
            }
        )
        
        if progress_percentage >= 100:
            update("user_courses", 
                {"completed": True},
                {
                    "user_id": f"eq.{user_id}",
                    "course_id": f"eq.{course_id}"
                }
            )
        
        return result
    except Exception as e:
        print(f"Error updating progress: {e}")
        return None

def get_course_progress(user_id, course_id):
    """Get current progress for a specific course"""
    try:
        result = fetch("user_courses", params={
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}",
            "select": "progress_percentage"
        })
        return result[0]["progress_percentage"] if result else 0
    except Exception as e:
        print(f"Error getting course progress: {e}")
        return 0



# USER ACTIVITY FUNCTIONS (Notes & Saved Lectures)
def get_user_activity(user_id, course_id):
    """Get user activity (notes and saved lectures) for a course"""
    try:
        result = fetch("user_activity", params={
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}"
        })
        
        if result:
            activity = result[0]
            return {
                "saved_notes": json.loads(activity.get("saved_notes", "{}")),
                "saved_lectures": json.loads(activity.get("saved_lectures", "[]"))
            }
        return {"saved_notes": {}, "saved_lectures": []}
    except Exception as e:
        print(f"Error fetching user activity: {e}")
        return {"saved_notes": {}, "saved_lectures": []}

def save_lecture(user_id, course_id, lecture_name):
    """Save a lecture to user's saved lectures"""
    try:
        activity = get_user_activity(user_id, course_id)
        saved_lectures = activity["saved_lectures"]
        
        if lecture_name not in saved_lectures:
            saved_lectures.append(lecture_name)
        
        existing = fetch("user_activity", params={
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}"
        })
        
        if existing:
            return update("user_activity",
                {"saved_lectures": json.dumps(saved_lectures)},
                {
                    "user_id": f"eq.{user_id}",
                    "course_id": f"eq.{course_id}"
                }
            )
        else:
            return insert("user_activity", {
                "user_id": user_id,
                "course_id": course_id,
                "saved_lectures": json.dumps(saved_lectures),
                "saved_notes": json.dumps({})
            })
    except Exception as e:
        print(f"Error saving lecture: {e}")
        return None

def save_notes(user_id, course_id, note_key, note_text):
    """Save notes for a specific chapter"""
    try:
        activity = get_user_activity(user_id, course_id)
        saved_notes = activity["saved_notes"]
        
        saved_notes[note_key] = note_text
        
        existing = fetch("user_activity", params={
            "user_id": f"eq.{user_id}",
            "course_id": f"eq.{course_id}"
        })
        
        if existing:
            return update("user_activity",
                {"saved_notes": json.dumps(saved_notes)},
                {
                    "user_id": f"eq.{user_id}",
                    "course_id": f"eq.{course_id}"
                }
            )
        else:
            return insert("user_activity", {
                "user_id": user_id,
                "course_id": course_id,
                "saved_notes": json.dumps(saved_notes),
                "saved_lectures": json.dumps([])
            })
    except Exception as e:
        print(f"Error saving notes: {e}")
        return None

def get_saved_notes(user_id, course_id, note_key):
    """Get saved notes for a specific chapter"""
    try:
        activity = get_user_activity(user_id, course_id)
        return activity["saved_notes"].get(note_key, "")
    except Exception as e:
        print(f"Error getting saved notes: {e}")
        return ""


# COIN HISTORY FUNCTIONS
def log_coin_transaction(user_id, coin_change, reason):
    """Log coin transaction to coin_history"""
    try:
        transaction_data = {
            "user_id": user_id,
            "coin_change": coin_change,
            "reason": reason
        }
        return insert("coin_history", transaction_data)
    except Exception as e:
        print(f"Error logging transaction: {e}")
        return None

def get_coin_history(user_id):
    """Get all coin transactions for a user"""
    try:
        return fetch("coin_history", params={
            "user_id": f"eq.{user_id}",
            "select": "*",
            "order": "id.desc"
        })
    except Exception as e:
        print(f"Error fetching coin history: {e}")
        return []