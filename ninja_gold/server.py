from flask import Flask, render_template, session, redirect, request
from random import randint
app = Flask (__name__)
app.secret_key = "Hiiipoweeerrrr"

@app.route('/')
def hello_world():
    if 'process_money' not in session:
        session['process_money'] = 0
        session['activity_list'] = []
    print(session['process_money'])
    return render_template ("frontpage.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    if request.form["building"]== "House":
        random_number =randint(2,5)
        building = request.form["building"]
        session['process_money'] += random_number
        user_action = f"bought a {building} earned {random_number} gold points"
        session['activity_list'].append
        (user_action)
        print(random_number)
        print(session['process_money'])
    if request.form["building"]== "Cave":
        random_number =randint(5,10)
        building = request.form["building"]
        session['process_money'] += random_number
        user_action = f"bought a {building} earned {random_number} gold points"
        session['activity_list'].append(user_action)
    if request.form["building"]== "Casino":
        random_number =randint(0,50)
        building = request.form["building"]
        session['process_money'] += random_number
        user_action = f"bought a {building} earned {random_number} gold points"
        session['activity_list'].append(user_action)
    if request.form["building"]== "Farm":
        random_number =randint(10,20)
        building = request.form["building"]
        session['process_money'] += random_number
        user_action = f"bought a {building} earned {random_number} gold points"
        session['activity_list'].append(user_action)
    return redirect ('/')












if __name__=="__main__":
    app.run(debug=True)