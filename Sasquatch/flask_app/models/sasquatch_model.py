from flask_app.models import user_model
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "sasquatch"
from flask import flash

class Sasquatch:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.num_of_sasquatch = data['num_of_sasquatch']
        self.user_id = data['user_id']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO  sasquatch (location,what_happened, date, num_of_sasquatch, user_id) VALUES (%(location)s,%(what_happened)s,%(date)s, %(num_of_sasquatch)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sasquatch JOIN users ON sasquatch.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_sasquatch = []
            for row in results:
                this_sasquatch = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_sasquatch.planner = this_user
                all_sasquatch.append(this_sasquatch)
            return all_sasquatch
        return []

    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM sasquatch LEFT JOIN users ON sasquatch.user_id = users.id WHERE sasquatch.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_sasquatch = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
                }
        this_user = user_model.User(user_data)
        this_sasquatch.planner = this_user
        return this_sasquatch


    @classmethod
    def update(cls,data):
        query = "UPDATE sasquatch SET location = %(location)s, what_happened = %(what_happened)s, date = %(date)s, num_of_sasquatch = %(num_of_sasquatch)s "\
            "WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod   
    def delete(cls,data):
        query = "DELETE FROM sasquatch WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True 
        if len(form_data['location']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['what_happened']) < 1:
            flash("what happened required")
            is_valid = False
        if len(form_data['num_of_sasquatch']) < 1:
            flash("num of sasquatch required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        return is_valid
