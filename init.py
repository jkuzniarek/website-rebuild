from flask import Flask, redirect, url_for, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    try:
        import MySQLdb, credlib

        # Open database connection
        db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)
        databaseError = ""
    except:
        databaseError = str(Exception)

    sql = "SELECT * FROM POST ORDER BY dateID DESC"
    postdict = {}

    if databaseError == "":

        try:
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            # Execute the SQL command
            cursor.execute(sql)
            # map to result dict
            result = cursor.fetchone()
        except:
            postdict["dateID"] = "NA"
            postdict["title"] = "Post Not Found"
            postdict["desc"] = "Error. Not found in database"

        else:
            if result is None:
                postdict["dateID"] = "NA"
                postdict["title"] = "No Posts Found"
                postdict["desc"] = "No posts available in database"

            else:
                postdict["dateID"] = result[0]
                postdict["title"] = result[1]
                postdict["desc"] = result[2]

            return pagelib.home(postdict)

        finally:
            # disconnect from server
            db.close()

    if databaseError != "":
        postdict["dateID"] = "NA"
        postdict["title"] = "Connection Error"
        postdict["desc"] = "Database connection error: " + databaseError
        return pagelib.home(postdict)

@app.route("/archive")
def archive():
    try:
        import MySQLdb, credlib
        # Open database connection
        db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)
        databaseError = ""

    except:
        databaseError = str(Exception)

    sql = "SELECT * FROM POST ORDER BY dateID DESC"

    if databaseError == "":
        try:
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            # Execute the SQL command
            cursor.execute(sql)
            # map to result dict
            results = cursor.fetchall()
        except:
            return redirect("/error/" + str(Exception))

        else:
            postlist = []
            rowcount = 0
            for row in results:
                postlist.insert(rowcount, {})
                postlist[rowcount]["dateID"] = row[0]
                postlist[rowcount]["title"] = row[1]
                postlist[rowcount]["desc"] = row[2]
                rowcount += 1

            return pagelib.archive(postlist)

        finally:
            # disconnect from server
            db.close()

    if databaseError != "":
        postlist = []
        postlist.insert(0, {})
        postlist[0]["dateID"] = "NA"
        postlist[0]["title"] = "Connection Error"
        postlist[0]["desc"] = "Database connection error: " + databaseError
        return pagelib.archive(postlist)

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
        databaseError = ""

    except:
        databaseError = str(Exception)

    postid = str(postid)
    sql = 'SELECT * FROM POST WHERE dateID = "%s"' % (postid)
    if databaseError == "":

        try:
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            # Execute the SQL command
            cursor.execute(sql)
            # map to result dict
            result = cursor.fetchone()
        except:
            return redirect("/error/" + str(Exception))

        else:
            postdict = {}

            if result is None:
                postdict["dateID"] = "NA"
                postdict["title"] = "Post Not Found"
                postdict["content"] = Markup("""<h1 class="green">Post Not Found</h1>
        <br>
        <p>
          The post you attempted to access does not exist or was not found.
        </p>""")

            else:
                postdict["dateID"] = result[0]
                postdict["title"] = result[1]
                postdict["desc"] = result[2]
                postdict["content"] = Markup(result[3])

            return pagelib.post(postdict)

        finally:
            # disconnect from server
            db.close()

    if databaseError != "":
        postdict = {}
        postdict["dateID"] = "NA"
        postdict["title"] = "Connection Error"
        postdict["desc"] = "Database connection error: " + databaseError
        postdict["content"] = Markup("""<h1 class="green">Connection Error</h1>
<br>
<p>
  Database connection error """ + databaseError + """
</p>""")
        return pagelib.post(postdict)

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
            return redirect("/error/" + str(Exception))

        sql = """INSERT INTO POST(dateID, title, description, content) \
                VALUES ('%s','%s','%s','%s')""" % \
                (request.form["data_dateID"].replace("'", "''"), request.form["data_title"].replace("'", "''"), \
                request.form["data_desc"].replace("'", "''"), request.form["data_content"].replace("'", "''"))

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
            return redirect("/error/" + str(Exception))

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

@app.route("/favicon.ico")
def iconRedirect():
    return redirect("/static/favicon.ico")

import pagelib

# comment out below before push
#if __name__ == '__main__':
#    app.run(debug=True) #set False for production
