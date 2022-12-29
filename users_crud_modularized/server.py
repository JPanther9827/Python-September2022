# from crypt import methods
from flask import Flask, render_template, request, redirect
# from flask_app import app
# from flask_app.controllers import user
from flask_app.models.user_model import User
from flask_app import app
# from user_model import User 


@app.route('/')
def hello_world():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)

@app.route('/user/<int:id>')
def get_one(id):
    data = {'id': id} 
    user = User.get_one(data)
    return render_template("user_one.html",user=user)

@app.route('/user/new')
def new_user_form():
    return render_template("user_new.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete_user(id):
        data = {'id': id} 
        User.delete(data)
        return redirect('/')

@app.route('/user/edit/<int:id>')
def edit_user_form(id):
    data = {'id': id} 
    user = User.get_one(data)
    return render_template("user_edit.html", user=user)

@app.route('/user/update/<int:id>', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)