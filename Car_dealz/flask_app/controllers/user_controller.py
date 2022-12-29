from logging import LoggerAdapter
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.dealer_model import Dealer
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

#STARTING POINT
@app.route('/')
def register():
    return render_template("login_registration.html")

# PROCESSING NEW USER
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
    session['user_id'] =  id
    return redirect('/welcome')

# PROSECCING EXISITNG USER TO LOGIN


@app.route('/users/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    users_in_db = User.get_by_email(data)
    if not users_in_db:
        flash('Invalid login info','log')
        return redirect('/')
    if not bcrypt.check_password_hash(users_in_db.password, request.form['password']):
        flash('Invalid login info','log')
        return redirect('/')
    session['user_id'] = users_in_db.id
    return redirect('/welcome')

# DASHBOARD
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    all_cardealer = Dealer.get_all()
    logged_user = User.get_by_id(user_data)
    print("+++++++++++++++++++++++++++", all_cardealer)
    return render_template('dashboard.html', cardealer=all_cardealer,logged_user=logged_user)


@app.route('/users/show', methods=['POST'])
def users_guest_list():
    if not User.validate(register.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/show.html')

# LOGOUT
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)