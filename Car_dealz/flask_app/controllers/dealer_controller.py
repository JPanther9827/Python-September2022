from flask_app import app
from flask import render_template, redirect, request, flash, session 
from flask_app.models.user_model import User
from flask_app.models.dealer_model import Dealer

# CREATE NEW PAGE
@app.route('/cardealer/new')
def new_form():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("new.html", cardealer = logged_user)

# PROCESS CREATE PAGE
@app.route('/cardealer/create', methods=['POST'])
def process_cardealer():
    if 'user_id' not in session:
        return redirect('/')
    if not Dealer.validator(request.form):
        return redirect('/cardealer/new')

    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Dealer.create(data)
    return redirect(f'/cardealer/{id}')

@app.route('/cardealer/<int:id>/delete')
def del_dealer(id):
    if 'user_id' not in session:
        return redirect('/')
    dealer = Dealer.get_by_id({'id': id})
    Dealer.delete({'id': id}) 
    return redirect('/welcome') 
   

@app.route('/cardealer/<int:id>/edit')
def edit_dealer_form(id):
    if 'user_id' not in session:
        return redirect('/')
    dealer = Dealer.get_by_id({'id': id})
    return render_template("edit.html", cardealer=dealer)

@app.route('/cardealer/<int:id>/update', methods=['POST'])
def update_dealer(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Dealer.validator(request.form):
        return redirect(f"/cardealer/{id}/edit")
    data = {
        **request.form,
        'id': id
    }
    Dealer.update(data)  
    return redirect('/welcome')

# SHOW ONE
@app.route("/cardealer/<int:id>")
def show_dealer(id):
    dealer = Dealer.get_by_id({'id': id})
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("show.html", cardealer = dealer, logged_user=logged_user)
    