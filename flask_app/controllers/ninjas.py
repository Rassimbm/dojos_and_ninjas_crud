from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja, dojo

@app.route("/add-ninja")
def r_add_ninja():
    return render_template("ninjas.html", dojos = dojo.Dojo.get_all())

