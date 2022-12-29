from flask_app import app
from flask import render_template, redirect, request, flash, session 
from flask_bcrypt import Bcrypt 
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

# THIS IS MY LANDING PAGE: LONGIN
@app.route('/')
def register():
    return render_template("register.html")

# PROCESSING NEW USER
@app.route('/users/register', methods=['post'])
def users_register():
    #BUILD THIS OUT: NOT DONE
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

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
        all_parties = Party.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('index.html', all_parties=all_parties,logged_user=logged_user)

@app.route('/magic')
def magic():
    return render_template("magic.html")

@app.route('/party')
def party():
    return render_template("party.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/guestlist')
def guestlist():
    return render_template("myparties.html")

@app.route('/users/guestlist', methods=['POST'])
def users_guest_list():
    if not Users.validate(register.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')



@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)