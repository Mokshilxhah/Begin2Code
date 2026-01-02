from flask import Blueprint, render_template
index_bp = Blueprint('index', __name__)

courses = [
        {"name": "Java", "icon": "fa-brands fa-java"},
        {"name": "Python", "icon": "fa-brands fa-python"},
        {"name": "C / C++", "icon": "fa-solid fa-code"},
        {"name": "JavaScript", "icon": "fa-brands fa-js"},
        {"name": "HTML", "icon": "fa-brands fa-html5"},
        {"name": "CSS", "icon": "fa-brands fa-css3-alt"},
        {"name": "TypeScript", "icon": "fa-brands fa-js"},
        {"name": "React", "icon": "fa-brands fa-react"},
        {"name": "Spring Boot", "icon": "fa-solid fa-gears"},
        {"name": "MySQL", "icon": "fa-solid fa-database"},
        {"name": "MongoDB", "icon": "fa-solid fa-leaf"},
        {"name": "Git", "icon": "fa-brands fa-git-alt"},
    ]

stats = [
        {
            "count": "10,000+",
            "label": "Happy Students",
            "bg_class": "bg-purple",
            "image": "images/happy.png"
        },
        {
            "count": "1500+",
            "label": "Video Lectures",
            "bg_class": "bg-red",
            "image": "images/Lecture.png"
        },
        {
            "count": "3000+",
            "label": "Practice Sets",
            "bg_class": "bg-blue",
            "image": "images/practice.png"
        },
        {
            "count": "60+",
            "label": "Courses On Platform",
            "bg_class": "bg-orange",
            "image": "images/course.png"
        }
    ]

hero_icons_left = [
    "fa-brands fa-docker",
    "fa-brands fa-react",
    "fa-brands fa-node-js",
    "fa-brands fa-js",
    "fa-brands fa-python",
    "fa-brands fa-java",
    "fa-brands fa-apple",
    "fa-brands fa-vuejs"
]

hero_icons_right = [
    "fa-brands fa-html5",
    "fa-brands fa-css3-alt",
    "fa-brands fa-bootstrap",
    "fa-brands fa-angular",
    "fa-brands fa-github",
    "fa-brands fa-windows",
    "fa-brands fa-php",
    "fa-solid fa-leaf"
]

problems_row_1 = [
    "🤝 No learning partner",
    "🧑‍💻 No practical / hands-on experience",
    "📞 No doubt support",
    "Do not know how to craft a resume and CV",
    "😞 Do not know how to get interview calls",
    "📞 No doubt support",
    "🚀 Unstructured learning path",
]

problems_row_2 = [
    "🔍 Having no clarity over concepts",
    "💬 No personal guidance, mentorship, support",
    "👎 Outdated lengthy syllabus",
    "💼 No Interview Cracking Skills",
    "✍️ Learning only theory from recordings",
    "🧠 Facing problems in logic building",
    "😵 No clear path what to do",
]

offerings = [
    {
        "image": "images/progress.png",
        "title": "Progress Tracking and Leaderboard",
        "img_style": "width:120px; height:100px;"
    },
    {
        "image": "images/teaching.png",
        "title": "40+ Hrs of Recorded Lecture",
        "img_style": "width:120px; height:100px;"
    },
    {
        "image": "images/notes.png",
        "title": "100+ Curated Practice Problems",
        "img_style": "width:120px; height:120px;"
    },
    {
        "image": "images/community.png",
        "title": "Community Support",
        "img_style": "width:120px; height:120px;"
    },
    {
        "image": "images/hints.png",
        "title": "Hints and Video Solution",
        "img_style": "width:120px; height:120px;"
    },
    {
        "image": "images/doubt.png",
        "title": "Doubt Support by Coders",
        "img_style": "width:120px; height:120px;"
    },
]


placed_students = [
    {"name": "Aman Pinjari", "role": "Software Developer", "company": "Amazon", "image": "students/img1.png"},
    {"name": "Rahul Vedi", "role": "Frontend Developer", "company": "Flipkart", "image": "students/img2.png"},
    {"name": "Akshat Sanghvi", "role": "Backend Developer", "company": "Wipro", "image": "students/img3.png"},
    {"name": "Manan Shah", "role": "Full Stack Developer", "company": "Mahindra", "image": "students/img4.png"},
    {"name": "Prathmesh Tiwari", "role": "Web Developer", "company": "Joyspoon", "image": "students/img5.png"},
    {"name": "Ashwin Chaudary", "role": "Python Developer", "company": "Bingo", "image": "students/img6.png"},
    {"name": "Meet Patel", "role": "Software Testing Engineer", "company": "CAT", "image": "students/img7.png"},
    {"name": "Harshit Doshi", "role": "Junior Software Engineer", "company": "Sugar", "image": "students/img5.png"},
    {"name": "Riya Savani", "role": "Trainee Developer", "company": "Asus", "image": "students/img8.png"},
    {"name": "Ronak Patel", "role": "Database Developer", "company": "AT&BT", "image": "students/img9.png"},
    {"name": "Rahul Triwedi", "role": "SWE-II", "company": "Flipkart", "image": "students/img10.png"},
    {"name": "Divy Jogani", "role": "Automation Engineer", "company": "Mesho", "image": "students/img1.png"}
]

companies = [
    {"image": "Company/Tech_1.jpg", "alt": "Amazon Logo"},
    {"image": "Company/Tech_2.jpg", "alt": "Flipkart Logo"},
    {"image": "Company/Tech_3.jpg", "alt": "Wipro Logo"},
    {"image": "Company/Tech_4.jpg", "alt": "Mahindra Logo"},
    {"image": "Company/Tech_5.jpg", "alt": "Joyspoon Logo"},
    {"image": "Company/Tech_6.jpg", "alt": "Bingo Logo"},
    {"image": "Company/Tech_7.jpg", "alt": "Amazon Logo"},
    {"image": "Company/Tech_8.jpg", "alt": "Flipkart Logo"},
    {"image": "Company/Tech_9.jpg", "alt": "Wipro Logo"},
    {"image": "Company/Tech_10.jpg", "alt": "Mahindra Logo"}
]

faqs = [
    {
        "question": "What is Begin2Code?",
        "answer": "Begin2Code is an online learning platform designed to help students learn "
        "coding and upskill through structured courses, embedded lectures, and supporting resources."
    },
    {
        "question": "Is this course beginner-friendly?",
        "answer": "Yes. The course starts from basics and gradually moves to advanced topics so any "
        "student can follow easily."
    },
    {
        "question": "How do I access courses?",
        "answer": "After registering and logging in, students can browse available courses "
        "and start learning immediately through their personal dashboard."
    },
    {
        "question": "Do I need prior coding experience?",
        "answer": "Not at all! Our platform is built to accommodate beginners as well as "
        "students who have some coding knowledge."
    },
    {
        "question": "Are lectures available in video format?",
        "answer": "Yes, all lectures are embedded directly on the platform for easy access,"
        " allowing students to watch and learn without leaving the site."
    },
    {
        "question": "Is there a way to track my progress?",
        "answer": "Yes, the dashboard allows students to monitor which courses they’ve accessed "
        "and track their learning journey step by step."
    }
]


@index_bp.route("/")
def index():
    return render_template("index.html", 
            courses=courses,
            stats=stats , 
            hero_icons_left=hero_icons_left,
            hero_icons_right=hero_icons_right,
            problems_row_1=problems_row_1,
            problems_row_2=problems_row_2,
            offerings=offerings,
            placed_students=placed_students,
            companies=companies,
            faqs=faqs)