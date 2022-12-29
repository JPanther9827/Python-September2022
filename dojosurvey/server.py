# from crypt import methods
from flask import Flask, render_template, redirect, session,request  # Import Flask to allow us to create our app
# import render_template to be able to serve html files
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Hiiiiipowerrrrr"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    if 'been_there' not in session:
        session['been_there'] = True
    return render_template("dojosurvey.html")  

@app.route('/processing', methods=['POST'])
def processing():
    session['your_name'] = request.form['your_name']
    session['my_location'] = request.form['my_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show():
    return render_template("show.html")


# @app.route('/')
# def home():
#     return redirect('/')











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

