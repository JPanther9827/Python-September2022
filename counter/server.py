from flask import Flask, render_template, redirect, session
app = Flask (__name__)
app.secret_key = "Hiiiiiii"
# created a if statement conditional
@app.route('/')
def hello_world():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"]+=1
    return render_template('counter.html')
# count is the homepage being redirected
@app.route('/count')
def count():
    
    return redirect ('/')
# created a reset route indexeing the counter route and were redirecting it
@app.route('/reset')
def reset():
    session["counter"] = 0
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.