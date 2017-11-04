'''pagelib
This is the library that consolidates each page assembly file.
Importing this will import all page dependencies.'''
from flask import render_template

def home():
    return render_template("home.html")

def about():
    return render_template("about.html")

def archive():
    return render_template("archive.html")

def construction():
    return render_template("construction.html")

def curriculum():
    return render_template("curriculum.html")

def resume():
    return render_tamplate("resume.html")

def post(name):
    return render_template("post.html", postid=name)

