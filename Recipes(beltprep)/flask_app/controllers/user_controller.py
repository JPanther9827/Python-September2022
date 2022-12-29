from flask import render_template, request, redirect, session, flash
from flask_app import app
# from flask_app.models.user_model import User
# from flask_app.models.recipe_model import Recipes
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

# starting point in my coding 
@app.route('/')
def registerpage():
    return render_template('/registration_login.html')

@app.route('/users/register', methods=['post'])
def users_register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_password
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')


@app.route('/users/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    users_in_db = User.get_by_email(data)
    if not users_in_db:
        flash('invalid login info','log')
        return redirect('/')
        session['user_id'] = users_in_db
        return redirect('/welcome')

