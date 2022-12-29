from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask import flash

@app.route('/recipe/new')
def new_recipe_form():
    return render_template("new_recipe.html")

@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipe/new')
    data = {
            **request.form,
            'user_id': session['user_id']
    }
    Recipe.create(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def one_recipe(id):
   
    if 'user_id' not in session:
        return redirect('/') 
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    this_recipe = Recipe.get_by_id({'id':id})
    return render_template("recipe_info.html", this_recipe=this_recipe, logged_user=logged_user)

@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    this_recipe = Recipe.get_by_id({'id': id})
    return render_template("edit_recipe.html", this_recipe=this_recipe)

@app.route('/recipe/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not Recipe.validator(request.form):
        return redirect(f'/recipe/{id}/edit')
    recipe_data = {
        **request.form,
        'id':id
    }
    Recipe.update(recipe_data)
    return redirect('/dashboard')


@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    this_recipe = Recipe.get_by_id({'id':id})
    if not this_recipe.user_id == session['user_id']:
        flash("Hold Up! wait a minute")
        return redirect('/dashboard')
    Recipe.delete({'id': id})
    return redirect('/dashboard')