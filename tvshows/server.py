from flask_app import app
from flask import render_template
from flask_app.controllers import user_controller, show_controller





@app.route('/login')
def login():
    return render_template("index.html")






if __name__ == "__main__":
	app.run(debug=True)