from flask import Flask
DATABASE = "tvshows"
app = Flask(__name__)
app.secret_key = 'super secret key'
