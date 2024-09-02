from flask import render_template
from . import create_app

app = create_app()

# Home page route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")