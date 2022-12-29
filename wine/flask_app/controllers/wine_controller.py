from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.wine_model import Wine
from flask_app.models.user_model import User
from flask import flash


@app.route('/wine/new')
def new_wine_form():
    return render_template("new_wine.html")

@app.route('/wine/create', methods=['POST'])
def create_wine():
    if 'user_id' not in session:
        return redirect('/')
    if not Wine.validator(request.form):
        return redirect('/wine/new')
    data = {
            **request.form,
            'user_id': session['user_id']
    }
    Wine.create(data)
    return redirect('/dashboard')


@app.route('/wine/<int:id>')
def one_wine(id):
   
    if 'user_id' not in session:
        return redirect('/') 
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    this_wine = Wine.get_by_id({'id':id})
    return render_template("wine_info.html", this_wine=this_wine, logged_user=logged_user)


@app.route('/wine/<int:id>/edit')
def edit_wine(id):
    if 'user_id' not in session:
        return redirect('/')
    this_wine = Wine.get_by_id({'id': id})
    return render_template("edit_wine.html", this_wine=this_wine)

@app.route('/wine/<int:id>/update', methods=['POST'])
def update_wine(id):
    if not Wine.validator(request.form):
        return redirect(f'/wine/{id}/edit')
    wine_data = {
        **request.form,
        'id':id
    }
    Wine.update(wine_data)
    return redirect('/dashboard')

@app.route('/wine/<int:id>/delete')
def delete_wine(id):
    this_wine = Wine.get_by_id({'id':id})
    if not this_wine.user_id == session['user_id']:
        flash("Hold Up! wait a minute")
        return redirect('/dashboard')
    Wine.delete({'id': id})
    return redirect('/dashboard')