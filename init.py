from flask import Flask, redirect, url_for, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    try:
        import MySQLdb, credlib

        # Open database connection
        db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)

    except:
        return redirect("/error/" + Exception)

    sql = "SELECT * FROM POST ORDER BY dateID DESC"
    postdict = {}

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
        postdict["desc"] = "Database connection error"

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

@app.route("/archive")
def archive():
    try:
        import MySQLdb, credlib
        # Open database connection
        db = MySQLdb.connect( credlib.db_host, credlib.db_username, credlib.db_password, credlib.db_name)

    except:
        return redirect("/error/" + Exception)

    sql = "SELECT * FROM POST ORDER BY dateID DESC"

    try:
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Execute the SQL command
        cursor.execute(sql)
        # map to result dict
        results = cursor.fetchall()
    except:
        return redirect("/error/" + Exception)

    else:
        postlist = []
        rowcount = 0
        for row in results:
            postlist.insert(rowcount, {})
            postlist[rowcount]["dateID"] = row[0]
            postlist[rowcount]["title"] = row[1]
            postlist[rowcount]["desc"] = row[2]
            postlist[rowcount]["content"] = Markup(row[3])
            rowcount += 1

        return pagelib.archive(postlist)

    finally:
        # disconnect from server
        db.close()

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
    sql = 'SELECT * FROM POST WHERE dateID = "%s"' % (postid)

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
