from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninja/new')
def new_ninja():
    all_dojos=Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)



@app.route('/ninja/creates', methods=['POST'])
def created_ninja():
    print("==================")
    Ninja.create(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}')
