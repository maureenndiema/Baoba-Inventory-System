from flask import render_template
from . import main
from flask_login import login_required

@main.route("/")
def index():
    title = 'Home'
    
    return render_template("index.html", title=title)
