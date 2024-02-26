from flask import render_template, session, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    return render_template("dojos.html", dojos = Dojo.get_all())

@app.route("/add-dojo", methods = ["POST"])
def p_add_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")

@app.route("/show-dojo/<int:dojo_id>")
def show_dojo(dojo_id):
    return render_template("show_dojo.html", dojo = Dojo.get_one(dojo_id))

