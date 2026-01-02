from flask import Blueprint, render_template
courses_bp = Blueprint('courses', __name__)

courses = {
    "Full Courses": [
        {
            "name": "MERN Stack Developer",
            "description": "Build full-stack web applications using MongoDB, Express, React & Node.js.",
            "icon": "fa-brands fa-react",
            "techs": [
                {"name": "Node.js", "class": "fa-brands fa-node-js"},
                {"name": "JavaScript", "class": "fa-brands fa-js"},
                {"name": "MongoDB", "class": "fa-solid fa-database"},
                {"name": "React", "class": "fa-brands fa-react"},
                {"name": "Express.js", "class": "fa-brands fa-js"}
            ]
        },

        {
            "name": "Java Developer",
            "description": "Learn Java programming from basics to advanced concepts.",
            "icon": "fa-brands fa-java",
            "techs": [
                {"name": "Java", "class": "fa-brands fa-java"},
                {"name": "Database", "class": "fa-solid fa-database"},
                {"name": "Gears", "class": "fa-solid fa-gears"}
            ]
        },

        {
            "name": "Python Developer",
            "description": "Build full-stack web applications using MongoDB, Express, React & Node.js.",
            "icon": "fa-brands fa-python",
            "techs": [
                {"name": "Python", "class": "fa-brands fa-python"},
                {"name": "Database", "class": "fa-solid fa-database"},
                {"name": "Mongo", "class": "fa-solid fa-leaf"}
            ]
        },

        {
            "name": "Frontend Developer",
            "description": "Create stunning user interfaces with HTML, CSS, and JavaScript.",
            "icon": "fa-brands fa-html5",
            "techs": [
                {"name": "Html", "class": "fa-brands fa-html5"},
                {"name": "Css", "class": "fa-brands fa-css3-alt"},
                {"name": "JavaScript", "class": "fa-brands fa-js"},
                {"name": "React", "class": "fa-brands fa-react"},
                {"name": "Express.js", "class": "fa-brands fa-js"}
            ]
        },

        {
            "name": "Data Science",
            "description": "Analyze and interpret complex data to aid decision-making.",
            "icon": "fa-solid fa-chart-line",
            "techs": [
                {"name": "Python", "class": "fa-brands fa-python"},
                {"name": "Pandas", "class": "fa-solid fa-chart-bar"},
                {"name": "Numpy", "class": "fa-solid fa-calculator"},
            ]
        },

        {
            "name": "DevOps Engineer",
            "description": "Learn to manage infrastructure and deploy applications efficiently.",
            "icon": "fa-solid fa-cloud",
            "techs": [
                {"name": "Docker", "class": "fa-brands fa-docker"},
                {"name": "Cloud", "class": "fa-solid fa-cloud"},
                {"name": "CI/CD", "class": "fa-solid fa-gears"}
            ]
        }
    ],

    "Frontend": [
        {
            "name": "HTML", 
            "description": "Structure and semantics of web pages.", 
            "icon": "fa-brands fa-html5"
        },

        {
            "name": "CSS", 
            "description": "Styling and layout of web pages.", 
            "icon": "fa-brands fa-css3-alt"
        },

        {
            "name": "JavaScript", 
            "description": "Interactive and dynamic web content.", 
            "icon": "fa-brands fa-js"
        },

        {
            "name": "React", 
            "description": "Build user interfaces with reusable components.", 
            "icon": "fa-brands fa-react"
        },

        {
            "name": "Bootstrap", 
            "description": "Responsive design framework for web development.", 
            "icon": "fa-brands fa-bootstrap"
        },

        {
            "name": "Tailwind CSS", 
            "description": "Utility-first CSS framework for rapid UI development.", 
            "icon": "fa-brands fa-css3-alt"
        }
    ],

    "Backend": [
        {
            "name": "Node.js", 
            "description": "Server-side JavaScript runtime for scalable apps.", 
            "icon": "fa-brands fa-node-js"
        },

        {
            "name": "Java", 
            "description": "Versatile programming language for building robust applications.", 
            "icon": "fa-brands fa-java"
        },

        {
            "name": "Python", 
            "description": "High-level programming language known for its readability and versatility.", 
            "icon": "fa-brands fa-python"
        },

        {
            "name": "C / C++", 
            "description": "Low-level programming languages for system-level programming.", 
            "icon": "fa-brands fa-c"
        },

        {
            "name": "PHP (Laravel)", 
            "description": "Server-side scripting language for web development.", 
            "icon": "fa-brands fa-php"
        },

        {
            "name": "Ruby on Rails", 
            "description": "Web application framework written in Ruby.", 
            "icon": "fa-brands fa-gem"
        },

        {
            "name": "Go (Golang)", 
            "description": "Statically typed language designed for simplicity and performance.", 
            "icon": "fa-solid fa-cogs"
        }
    ],

    "Libraries": [
        {
            "name": "Vue.js", 
            "description": "Progressive JS framework for building modern web interfaces.", 
            "icon": "fa-brands fa-vuejs", "badge": "JavaScript"
        },

        {
            "name": "Tensorflow", 
             "description": "Open-source library for machine learning and AI.", 
            "icon": "fa-solid fa-brain", "badge": "Python"
        },

        {
            "name": "Tailwind CSS", 
            "description": "Utility-first CSS framework for rapid UI development.", 
            "icon": "fa-brands fa-css3-alt", "badge": "CSS"
        },

        {
            "name": "Hibernate",  
            "description": "Java-based ORM framework for database interaction.",
            "icon": "fa-solid fa-database", "badge": "Java"
        }
    ],

    "Databases": [
        {  
            "name": "MySQL", 
            "description": "Relational database system.", 
            "icon": "fa-solid fa-database"
        },

        {  
            "name": "MongoDB", 
            "description": "NoSQL database system.", 
            "icon": "fa-solid fa-leaf"
        },

        {  
            "name": "Git", 
            "description": "Version control system for tracking changes.", 
            "icon": "fa-brands fa-git-alt"
        },

        {  
            "name": "GitHub", 
            "description": "Web-based platform for version control and collaboration.", 
            "icon": "fa-brands fa-github"
        }
    ]
}

@courses_bp.route('/courses')
def courses_page():
    return render_template('courses.html', courses=courses)
