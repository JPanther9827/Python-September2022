from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
from flask_app.models import user_model

class shows:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.date = data['date']
        self.description = data['description']
        self.Network = data['Network']
        self.posted_by = data['posted_by']
        self.created_at = data['created_at']
        self.user_id = data['user_id']



    @classmethod
    def create(cls, data):
        query = "INSERT INTO  tvshows (title,date,description, Network,posted_by, user_id) VALUES (%(title)s,%(description)s,%(date)s, %(Network)s, %(posted_by)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tvshows JOIN users ON shows.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_show = []
            for row in results:
                this_show = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_show.planner = this_user
                all_show.append(this_show)
            return all_show
        return []

    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM tvshows LEFT JOIN users ON show.user_id = users.id WHERE show.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_show = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
                }
        this_user = user_model.User(user_data)
        this_show.planner = this_user
        return this_show


    @classmethod
    def update(cls,data):
        query = "UPDATE show SET title = %(title)s, date = %(date)s, description = %(description)s, Network = %(Network)s, posted_by = %(posted_by)s "\
            "WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod   
    def delete(cls,data):
        query = "DELETE FROM show WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True 
        if len(form_data['title']) < 1:
            flash("title required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        if len(form_data['Network']) < 1:
            flash("Network required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if len(form_data['posted_by']) < 1:
            flash("posted by required")
            is_valid = False
        return is_valid