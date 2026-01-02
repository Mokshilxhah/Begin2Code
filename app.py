from flask import Flask , render_template
from routes.courses import courses_bp
from routes.notes import notes_bp
from routes.index import index_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(notes_bp)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/cookies")
def cookies():
    return render_template("cookies.html")

@app.route("/terms_condition")
def terms():
    return render_template("terms_condition.html")


if __name__ == "__main__":
    app.run()
