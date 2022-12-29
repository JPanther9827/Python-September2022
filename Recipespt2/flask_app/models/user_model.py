# from flask_app.models.recipe_model import DATABASE
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "recipes"
import re
from flask_app.models import recipe_model
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
        # self.dojo_id = data['Recipe_id']
        
   
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
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        user = cls(results[0])
        list_of_recipe = []
        for row in results:
            if row['recipes.id'] == None:
                break 
            recipe_data = {
                **row,
                'id': row['recipes.id'],
                'created_at': row['recipes.created_at'],
                'updated_at': row['recipes.updated_at']
            }  
            this_recipe =  recipe_model.Recipe(recipe_data)   
            list_of_recipe.append(this_recipe)
            user.recipe = list_of_recipe
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
            flash("First name is required","reg")
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
        
        

    