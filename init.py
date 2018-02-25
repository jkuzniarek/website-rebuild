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
    try:
        import MySQLdb, credlib

        # Open database connection
        db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)

    except:
        return redirect("/error/" + Exception)

    postid = str(postid)
    sql = "SELECT * FROM POST WHERE dateID = %s" % (postid)

    try:
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Execute the SQL command
        cursor.execute(sql)
        # map to result dict
        result = cursor.fetchone()
    except:
        return redirect("/error/" + Exception)

    else:
        postdict = {}

        if result is None:
            postdict["postID"] = "NA"
            postdict["title"] = "Post Not Found"
            postdict["content"] = """<h1 class="green">Post Not Found</h1>
        <br>
        <p>
          The post you attempted to access does not exist or was not found.
        </p>"""

        else:
            postdict["postID"] = result[0]
            postdict["title"] = result[1]
            postdict["desc"] = result[2]
            postdict["content"] = result[3]

    return pagelib.post(postdict)

    finally:
        # disconnect from server
        db.close()
    return pagelib.post(post_data)

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
            return redirect("/error/" + Exception)

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
            return redirect("/error/" + Exception)

        else:
            return redirect(url_for("postCreated"))

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
