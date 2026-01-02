from flask import Blueprint, render_template
notes_bp = Blueprint('notes', __name__)

notes = [
    {
        "name": "C++",
        "image": "Notes/CC++.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Java",
        "image": "Notes/Java.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Python",
        "image": "Notes/Python.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "JavaScript",
        "image": "Notes/JavaScript.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "HTML",
        "image": "Notes/Html.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Css",
        "image": "Notes/Css.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "React",
        "image": "Notes/React.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Angular",
        "image": "Notes/Angular.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Node.js",
        "image": "Notes/Node.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Express.js",
        "image": "Notes/Express.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "TypeScript",
        "image": "Notes/TypeScript.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Value.js",
        "image": "Notes/Value.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Spring Boot",
        "image": "Notes/Spring.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Bootstrap",
        "image": "Notes/Bootstrap.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Django",
        "image": "Notes/Django.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Flask",
        "image": "Notes/Flask.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "MySQL",
        "image": "Notes/MySQL.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "MongoDB",
        "image": "Notes/Mongo.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Firebase",
        "image": "Notes/Firebase.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    },
    {
        "name": "Redis",
        "image": "Notes/Redis.png",
        "full": "Notes_pdf/.pdf",
        "short": "Notes_pdf/.pdf",
        "mind": "Notes_pdf/.pdf"
    }
]

@notes_bp.route('/notes')
def notes_page():
    return render_template('notes.html',notes=notes)