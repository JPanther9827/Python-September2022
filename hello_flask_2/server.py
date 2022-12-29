from flask import Flask, render_template  # Import Flask to allow us to create our app
# import render_template to be able to serve html files
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'we can change this!!'  # Return the string 'Hello World!' as a response

@app.route('/or_this')
@app.route('/success')
def success():
    return "<h1>success</h1>"
# the app.route listens (like an evenlistener) for the <word> and <int:number in your browser to make a request happen 
# your template has access to your route
@app.route('/say/<word>/<int:number>')
# path variables go in <>
#  be default path variables are strings
# your going to pass (word, number) to your template (say.html) 
# your picking your parameter variable and rendering it on line 24
def say_word(word, number):
    # remember to bring your path variables in as parameters
    print(word)
    print(number)
    return render_template("say.html", word=word, number=number)
    # your taking that parameter and passing it as the same name 

# these are path variables
@app.route("/template")
def template():
    # declared the variable inside of your route
    # your grabbing new_variable and returning it in your render for it to work
    new_variable = "This is a test string"
    return render_template("index.html", name_of_variable_on_template = new_variable)
    #                                       name_on_template = value you want
#  your telling the computer that your giving a new variable with a value

@app.route("/route_to_page_2")
def page2():
    return render_template("page2.html")
#  you can pass your variables by putting it in a render template

@app.route("/iterate")
def iterate():
    cats = [
        {
            'name': 'Garfield',
            'color': 'orange'
        },
        {
            'name': 'Scar',
            'color': 'dark brown'
        },
        {
            'name': 'Felix',
            'color': 'cat'
        }
    ]
    return render_template("cats.html", cats=cats, h=100, w=1000, color='pink')
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

