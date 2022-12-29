from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.painting_model import Painting


# @app.route('/')
# def new_form():
#     if 'user_id' not in session:
#         return redirect('/')
#     logged_user = User.get_by_id({'id': session['user_id']})
#     return render_template("new.html", paintings = logged_user)

@app.route('/painting/create', methods=['POST'])
def process_painting():
    if 'user_id' not in session:
        return redirect('/')
    if not Painting.validator(request.form):
        return redirect('/painting/new')

    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Painting.create(data)
    return redirect(f'/painting/{id}')

@app.route('/painting/<int:id>/delete')
def del_painting(id):
    if 'user_id' not in session:
        return redirect('/')
    painting = Painting.get_by_id({'id': id})
    Painting.delete({'id': id})
    return redirect('/welcome')

@app.route('/painting/<int:id>/edit')
def edit_painting_form(id):
    if 'user_id' not in session:
        return redirect('/')
    painting = Painting.get_by_id({'id':id})
    return render_template("edit.html", paintings=painting)

@app.route('/painting/<int:id>/update', methods=['POST'])
def update_painting(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Painting.validator(request.form):
        return redirect(f"/painting/{id}/edit")
    data = {
        **request.form,
        'id': id
    }
    Painting.update(data)
    return redirect('/welcome')

@app.route("/painting/<int:id>")
def show_painting(id):
    painting = Painting.get_by_id({'id':id})
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("show.html", paintings = painting, logged_user=logged_user)