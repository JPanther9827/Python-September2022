from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.sasquatch_model import Sasquatch
from flask_app.models.user_model import User
from flask import flash

@app.route('/sasquatch/new')
def new_sasquatch_form():
    return render_template("new_sasquatch.html")

@app.route('/sasquatch/create', methods=['POST'])
def create_sasquatch():
    if 'user_id' not in session:
        return redirect('/')
    if not Sasquatch.validator(request.form):
        return redirect('/sasquatch/new')
    data = {
            **request.form,
            'user_id': session['user_id']
    }
    Sasquatch.create(data)
    return redirect('/dashboard')

@app.route('/sasquatch/<int:id>')
def one_sasquatch(id):
   
    if 'user_id' not in session:
        return redirect('/') 
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    this_sasquatch = Sasquatch.get_by_id({'id':id})
    return render_template("sasquatch_info.html", this_sasquatch=this_sasquatch, logged_user=logged_user)

@app.route('/sasquatch/<int:id>/edit')
def edit_sasquatch(id):
    if 'user_id' not in session:
        return redirect('/')
    this_sasquatch = Sasquatch.get_by_id({'id': id})
    return render_template("edit_sasquatch.html", this_sasquatch=this_sasquatch)

@app.route('/sasquatch/<int:id>/update', methods=['POST'])
def update_sasquatch(id):
    if not Sasquatch.validator(request.form):
        return redirect(f'/sasquatch/{id}/edit')
    sasquatch_data = {
        **request.form,
        'id':id
    }
    Sasquatch.update(sasquatch_data)
    return redirect('/dashboard')

@app.route('/sasquatch/<int:id>/delete')
def delete_sasquatch(id):
    this_sasquatch = Sasquatch.get_by_id({'id':id})
    if not this_sasquatch.user_id == session['user_id']:
        flash("Hold Up! wait a minute")
        return redirect('/dashboard')
    Sasquatch.delete({'id': id})
    return redirect('/dashboard')
