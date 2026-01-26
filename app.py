import os
from dotenv import load_dotenv

from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail
from werkzeug.security import generate_password_hash, check_password_hash
from services.email_service import send_welcome_email, send_verification_email
from random import randint
from functools import wraps
from models import db

app = Flask(__name__)
load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = (
    "Begin2Code",
    os.getenv("MAIL_USERNAME")
)
mail = Mail(app)

app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config['PERMANENT_SESSION_LIFETIME'] = 86400 
from routes.courses import courses_bp
from routes.notes import notes_bp
from routes.index import index_bp
from routes.dashboard import dash_bp

app.register_blueprint(index_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(dash_bp)


# DECORATORS
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please Login to Continue", "warning")
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

def ajax_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({
                "success": False,
                "message": "Please login First",
                "require_login": True
            })
        return f(*args, **kwargs)
    return decorated_function

@app.route("/check-auth")
def check_auth():
    is_authenticated = "user_id" in session
    user_data = None
    
    if is_authenticated:
        user = db.get_user_by_email(session.get("user_email"))
        if user:
            user_data = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "coins": user["coins"]
            }
    
    return jsonify({
        "authenticated": is_authenticated,
        "user": user_data
    })



@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"success": False, "message": "All Fields are Required"})

    user = db.get_user_by_email(email)    
    if not user:
        return jsonify({
            "success": False,
            "message": "Email not Registered. Please Create an Account First."
        })
    
    if not check_password_hash(user['password'], password):
        return jsonify({
            "success": False,
            "message": "Invalid Password. Please Try Again."
        })

    session["user_id"] = user["id"]
    session["user_email"] = user["email"]
    session["user_name"] = user["name"]
    session.permanent = True
    
    return jsonify({
        "success": True,
        "message": "Login successful!",
        "redirect": "/dashboard"
    })



@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required"
        })

    existing_user = db.get_user_by_email(email)
    if existing_user:
        return jsonify({
            "success": False,
            "message": "Email Already Registered. Please login instead."
        })

    if len(password) < 6:
        return jsonify({
            "success": False,
            "message": "Password must be at least 6 characters long"
        })

    otp = randint(100000, 999999)

    session["reg_name"] = name
    session["reg_email"] = email
    session["reg_password"] = generate_password_hash(password)
    session["otp"] = otp
    session["otp_attempts"] = 0
    
    try:
        send_verification_email(mail, email, otp)
        return jsonify({
            "success": True,
            "message": "OTP Sent to your Mail. Please check your inbox."
        })
    except Exception as e:
        print(f"Email error: {e}")
        return jsonify({
            "success": False,
            "message": "Failed to send Mail. Please try again later."
        })


@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    entered_otp = request.form.get("otp")

    if "otp" not in session:
        return jsonify({
            "success": False,
            "message": "Session expired. Please register again.",
            "session_expired": True
        })

    session["otp_attempts"] = session.get("otp_attempts", 0) + 1

    if session["otp_attempts"] > 3:
        session.clear()
        return jsonify({
            "success": False,
            "message": "Too many wrong attempts. Please register again.",
            "session_expired": True
        })

    if str(entered_otp) == str(session["otp"]):
        new_user = db.create_user(
            name=session["reg_name"],
            email=session["reg_email"],
            password_hash=session["reg_password"]
        )
        
        if not new_user:
            return jsonify({
                "success": False,
                "message": "Failed to create account. Please try again."
            })
        
        try:
            send_welcome_email(mail, session["reg_email"], session["reg_name"])
        except Exception as e:
            print(f"Welcome email error: {e}")
        
        session["user_id"] = new_user["id"]
        session["user_email"] = new_user["email"]
        session["user_name"] = new_user["name"]
        session.permanent = True
        
        session.pop("reg_name", None)
        session.pop("reg_email", None)
        session.pop("reg_password", None)
        session.pop("otp", None)
        session.pop("otp_attempts", None)
        
        return jsonify({
            "success": True,
            "message": "Account created successfully! Welcome to Begin2Code 🎉",
            "redirect": "/dashboard"
        })
    else:
        remaining = 3 - session["otp_attempts"]
        return jsonify({
            "success": False,
            "message": f"Invalid OTP. {remaining} attempt(s) remaining."
        })


@app.route("/get-user-coins", methods=["GET"])
@ajax_login_required
def get_user_coins():
    user = db.get_user_by_email(session.get("user_email"))
    if user:
        return jsonify({"success": True, "coins": user.get('coins', 0)})
    return jsonify({"success": False, "coins": 0})


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully", "success")
    return redirect('/')


# STATIC PAGES
@app.route("/cookies")
def cookies():
    return render_template("cookies.html")

@app.route("/terms_condition")
def terms():
    return render_template("terms_condition.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("index.html"), 500

if __name__ == "__main__":

    app.run(debug=os.getenv("FLASK_DEBUG") == "True")

