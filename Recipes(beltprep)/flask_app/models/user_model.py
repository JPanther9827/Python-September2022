from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
from flask_app.models import recipe_model
from flask_app.models import user_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

@classmethod
def create(cls,data):
    query = "INSERT INTO customer (first_name,last_name,password,email) VALUES(%(first_name)s,%(last_name)s,%(passwords)s,%(email)s);"
    return connectToMySQL(DATABASE).query_db(query,data)

@classmethod
def get_by_email(cls,data):
    query = "SELECT * FROM customer WHERE email = %(email)s;"
    results = connectToMySQL(DATABASE).query_db(query,data)
    if len(results) < 1:
        return False
    return cls(results[0])

@classmethod
def get_by_id(cls,data):
    query = "SELECT * FROM customer WHERE id = %(id)s;"
    results = connectToMySQL(DATABASE).query

