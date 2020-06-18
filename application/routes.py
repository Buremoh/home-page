from flask import render_template

from application import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route("/courses")
def courses():
    courses = [{
        "courseID": "1111", "title": "python for Data Science",
        "description": "Intro to Data Science with Python",
        "duration": "9 months",
        "term": "cohort 3"},
        {"courseID": "2222", "title": "Fullstack Web",
         "description": "Fullstack web development with python & Javascript",
         "duration": "9 months",
         "term": "cohort 3"},
        {"courseID": "3333", "title": "Jamstack",
         "description": "React, Vue, MongoDB",
         "duration": "6 months",
         "term": "cohort1"},
        {"courseID": "4444", "title": "HTML & CSS",
         "description": "Intro to web development",
         "duration": "3 months",
         "term": "cohort 5"},
        {"courseID": "5555", "title": "Java 2",
         "description": "Advanced Java Programming",
         "duration": "12 months",
         "term": "cohort1"}, ]

    return render_template("courses.html", courses=courses)
