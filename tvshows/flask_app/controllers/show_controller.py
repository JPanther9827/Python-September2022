from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.show_model import shows
from flask_app.models.user_model import User
from flask import flash

@app.route('/show/new')
def new_show_form():
    return render_template("new_show.html")

@app.route('/show/create', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/')
    if not shows.validator(request.form):
        return redirect('/show/new')
    data = {
            **request.form,
            'user_id': session['user_id']
    }
    shows.create(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def one_show(id):
    if 'user_id' not in session:
        return redirect('/') 
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    this_show = shows.get_by_id({'id':id})
    return render_template("show_info.html", this_show=this_show, logged_user=logged_user)

@app.route('/show/<int:id>/edit')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/')
    this_show = shows.get_by_id({'id': id})
    return render_template("edit_show.html", this_show=this_show)

@app.route('/show/<int:id>/update', methods=['POST'])
def update_show(id):
    if not shows.validator(request.form):
        return redirect(f'/show/{id}/edit')
    show_data = {
        **request.form,
        'id':id
    }
    shows.update(show_data)
    return redirect('/dashboard')

@app.route('/show/<int:id>/delete')
def delete_show(id):
    this_show = shows.get_by_id({'id':id})
    if not this_show.user_id == session['user_id']:
        flash("Hold Up! wait a minute")
        return redirect('/dashboard')
    shows.delete({'id': id})
    return redirect('/dashboard')
