from flask_app.models import user_model
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "wine"
from flask import flash


class Wine:
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.location = data['location']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO  wine (location,description, date, user_id) VALUES (%(location)s,%(description)s,%(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM wine JOIN users ON wine.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_wine = []
            for row in results:
                this_wine = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_wine.planner = this_user
                all_wine.append(this_wine)
            return all_wine
        return [] 


    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM wine LEFT JOIN users ON wine.user_id = users.id WHERE wine.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_wine = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
                }
        this_user = user_model.User(user_data)
        this_wine.planner = this_user
        return this_wine


    @classmethod
    def update(cls,data):
        query = "UPDATE wine SET location = %(location)s, description = %(description)s, date = %(date)s "\
            "WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod   
    def delete(cls,data):
        query = "DELETE FROM wine WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True 
        if len(form_data['location']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        return is_valid