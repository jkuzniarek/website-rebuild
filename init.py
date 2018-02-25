from flask import Flask, redirect, url_for, request
import sys

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
    return pagelib.post(postid)

@app.route("/create-post", methods=["GET", "POST"])
def createPost():
    if request.method == "GET":
        return pagelib.createPost()
    if request.method == "POST":
        try:
            import MySQLdb, credlib

            # Open database connection
            db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)

        except:
            return redirect(url_for("/error/" + sys.exc_info()[0]))

        sql = "INSERT INTO POST(dateID, title, description, content) \
                VALUES ('%s','%s','%s','%s')" % \
                (request.form["data_dateID"], request.form["data_title"], \
                request.form["data_desc"], request.form["data_content"], )

        try:
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
            return redirect("/error/" + sys.exc_info()[0]))

        else:
            return redirect(url_for("/postCreated"))

        finally:
            # disconnect from server
            db.close()

@app.route("/post-created")
def postCreated():
    return pagelib.postCreated()

@app.route("/error/<error_message>")
def error(error_message):
    return pagelib.error(error_message)

import pagelib

#if __name__ == '__main__':
#    app.run(debug=False) #set False for production
