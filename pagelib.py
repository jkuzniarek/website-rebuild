'''pagelib
This is the library that consolidates each page assembly file.
Importing this will import all page dependencies.'''
from flask import render_template, url_for

resources = {}
resources[navbar] = '''
<nav>
  <ul>
  <li><a href="''' + url_for("home") + '''"><span class="green">[</span> jkuzniarek.me <span
    class="green">]</span></a></li>
  <li><a href="''' + url_for("about") + '''"><span class="green">[</span> About <span
    class="green">]</span></a></li>
  <li><a href="''' + url_for("resume") + '''"><span class="green">[</span> Resume <span
    class="green">]</span></a></li>
  <li><a href="''' + url_for("curriculum") + '''"><span class="green">[</span> Curriculum <span
    class="green">]</span></a></li>
  <li><a href="''' + url_for("archive") + '''"><span class="green">[</span> Archive <span
    class="green">]</span></a></li>
  <li><a href="http://github.com/jkuzniarek"><span class="green">[</span> GitHub <span
    class="green">]</span></a></li>
	</ul>
</nav>'''
resources[style] = '<link rel=stylesheet href=' + url_for("static", filename=style.css) + >'

def home():
    return render_template("home.html", resources)

def about():
    return render_template("about.html", resources)

def archive():
    return render_template("archive.html", resources)

def construction():
    return render_template("construction.html", resources)

def curriculum():
    return render_template("curriculum.html", resources)

def resume():
    return render_tamplate("resume.html", resources)

def post(name):
    return render_template("post.html", postid=name, resources)
