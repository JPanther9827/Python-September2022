from flask import Flask, render_template # Import Flask to allow us to create our app
# import render_template to be able to serve html files
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')          
def play():
    return render_template("index.html")  


# @app.route('/play/<int:x>/<color>')
# def color():
#     return render_template(color=color)



    
    
    
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.