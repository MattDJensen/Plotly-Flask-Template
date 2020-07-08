from flask import current_app as app
from flask import render_template, url_for, redirect

@app.route("/")
def no_url():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index.jinja2")