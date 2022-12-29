from crypt import methods
from flask import Flask, render_template, request # Import Flask to allow us to create our app
# import request to be able to access the body of our post requests (request.form)
app = Flask(__name__)    # Create a new instance of the Flask class called "app"





@app.route('/')          # The "@" decorator associates this route with the function immediately following
def render_form():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


@app.route('/process_form', methods=['POST'] ) 
    # methods list for specifying methods to listen for
def process_form():
    print(request.form)
    return "got a form"











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

