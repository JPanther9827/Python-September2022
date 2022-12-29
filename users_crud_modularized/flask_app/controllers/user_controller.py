from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect('/users')