from flask import Flask, redirect, url_for, request


app = Flask(__name__)

@app.route("/")
def index():
    return pagelib.home()

@app.route("/about")
def about():
    return pagelib.about()

@app.route("/archive")
def archive():
    return pagelib.archive()

@app.route("/construction")
def construction():
    return pagelib.construction()

@app.route("/curriculum")
def curriculum():
    return pagelib.curriculum()

@app.route("/resume")
def resume():
    return pagelib.resume()

@app.route("/post/<postid>")
def post(postid):
    return pagelib.post()

import pagelib

#if __name__ == '__main__':
#    app.run(debug=False) #set False for production
