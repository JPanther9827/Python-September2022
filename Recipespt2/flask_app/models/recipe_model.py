from flask_app.models import user_model
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "recipes"
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.under = data['under']
        self.user_id = data['user_id']
 
    @classmethod
    def create(cls, data):
        query = "INSERT INTO  recipes (name,description,instruction, date, under, user_id) VALUES (%(name)s,%(description)s,%(instruction)s,%(date)s, %(under)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
   
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_recipes = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        # if len(results) < 1:
        #     return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
                }
        this_user = user_model.User(user_data)
        this_recipe.planner = this_user
        return this_recipe


    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, date = %(date)s, instruction = %(instruction)s "\
            "WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod   
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def validator(form_data):
        is_valid = True 
        if len(form_data['name']) < 1:
            flash("name required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        if len(form_data['instruction']) < 1:
            flash("instruction required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        return is_valid

