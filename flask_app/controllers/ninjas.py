from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models import ninja, dojo
from flask_app.controllers import dojos

@app.route("/add-ninja")
def r_add_ninja():
    return render_template("ninjas.html", dojos = dojo.Dojo.get_all())

@app.route("/new-ninja", methods = ["POST"])
def p_new_ninja():
    ninja.Ninja.save(request.form)
    return redirect(url_for("show_dojo", dojo_id = request.form["dojo_id"]))

