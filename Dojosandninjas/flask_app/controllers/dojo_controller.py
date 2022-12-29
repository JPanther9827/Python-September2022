from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
	all_dojos = Dojo.get_all()
	return render_template("dashboard.html", all_dojos=all_dojos)



@app.route('/dojo/<int:id>')
def get_one(id):
    data = {'id':id}
    dojo = Dojo.get_all_with_dojos(data)
    return render_template("ninja_info.html", dojo=dojo)


@app.route('/dojo/create', methods=['POST'])
def created_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route("/dojos")
def all_dojos():
    all_dojos = Dojo.get_all_with_dojos()
    return render_template("ninja_info.html", all_dojos=all_dojos)


