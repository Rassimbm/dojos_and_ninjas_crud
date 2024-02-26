from flask import render_template, session, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    return render_template("dojos.html", dojos = Dojo.get_all())
