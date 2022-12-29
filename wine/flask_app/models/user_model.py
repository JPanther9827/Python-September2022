from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "wine"
import re
from flask_app.models import wine_model
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls,data):
        print("============================")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod 
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN wine ON users.id = wine.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        user = cls(results[0])
        list_of_wine = []
        for row in results:
            if row['wine.id'] == None:
                break 
            wine_data = {
                **row,
                'id': row['wine.id'],
                'created_at': row['wine.created_at'],
                'updated_at': row['wine.updated_at']
            }  
            this_wine =  wine_model.Wine(wine_data)   
            list_of_wine.append(this_wine)
            user.wine = list_of_wine
        return user

    @staticmethod
    def validator(potential_user):
        is_valid = True
        if len(potential_user['first_name']) < 1:
            flash("First name is required","reg")
            is_valid = False 
        if len(potential_user['last_name']) < 1:
            flash("last name is required","reg")
            is_valid = False 
        if len(potential_user['email']) < 1:
            flash("Email is required","reg")
            is_valid = False 
        elif not EMAIL_REGEX.match(potential_user['email']):
            flash("email must be valid", "reg")
            is_valid = False 
        else:
            data = {
                'email':potential_user['email']
            }
            user_in_db = User.get_by_email(data)
            if user_in_db:
                flash("email already registered", "reg")
                is_valid = False

        if len(potential_user['password']) < 8:
            flash("password must be 8 characters", "reg")
            is_valid = False
        elif not potential_user['password'] == potential_user['confirm_pass']:
            flash("double check your password confirmation", "reg")
            is_valid = False
        return is_valid