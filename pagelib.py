'''pagelib
This is the library that consolidates each page assembly file.
Importing this will import all page dependencies.'''
from flask import render_template, url_for

navbar = {}
navbar["/"] = "jkuzniarek.me"
navbar["/static/resume.pdf"] = "Resume"
navbar["/curriculum"] = "Curriculum"
navbar["/archive"] = "Archive"
navbar["http://github.com/jkuzniarek"] = "GitHub"

def home(post_data):
    return render_template("home.html", navbar=navbar, post=post_data)

def archive(post_data):
    return render_template("archive.html", navbar=navbar, posts=post_data)

def construction():
    return render_template("construction.html", navbar=navbar)

def curriculum():
    return render_template("curriculum.html", navbar=navbar)

def resume():
    return render_template("resume.html", navbar=navbar)

def post(post_data):
    return render_template("post.html", navbar=navbar, post=post_data)

def createPost():
    return render_template("create-post.html", navbar=navbar)

def postCreated():
    return render_template("post-created.html", navbar=navbar)

def error(message):
    return render_template("error.html", navbar=navbar, error_message=message)
