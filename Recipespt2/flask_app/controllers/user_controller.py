
from flask import render_template, request, redirect, session,flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/dashboard')
def dash():
    if not "user_id" in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    print(logged_user.first_name)
    all_recipes = Recipe.get_all()
    print(all_recipes)
    return render_template("dashboard.html", logged_user=logged_user, all_recipes=all_recipes)

@app.route('/user/register', methods=['POST'])
def reg_user():
    if not User.validator(request.form):
        return redirect('/')
    hash_browns = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_browns
    }
    new_id = User.create(data)
    session['user_id'] = new_id
    return redirect('/dashboard')

@app.route('/user/login', methods=['POST'])
def log_user():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Credentials", "log")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Credentials **", "log")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/user/logout')
def log_out_user():
    del session['user_id']
    return redirect ('/')

@app.route('/my_recipe')
def users_recipe():
    if not "user_id" in session:
        return redirect('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("recipe.info.html", logged_user=logged_user)