from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
from flask_app.models import painting_model, user_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Painting:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.customer_id = data['customer_id']

@classmethod 
def get_all(cls):
    query = "SELECT * FROM painting JOIN customer on painting.customer_id = customer.id;"
    return connectToMySQL(DATABASE).query_db(query)

@classmethod
def create(cls,data):
    query = "INSERT INTO painting (title,description,price,customer_id) VALUES(%(title)s,%(description)s,%(price)s,%(user_id)s);"
    return connectToMySQL(DATABASE).query_db(query,data)

@classmethod 
def get_all_with_paintings(cls,data):
    query = "SELECT * FROM painting JOIN customer on painting.customer_id = customer.id WHERE painting.customer_id = %(id)s;"  
    results = connectToMySQL(DATABASE).query_db(query,data)
    if len(results) > 0:
        all_paintings = []
        for row in results:
            this_painting = cls(row)
            user_data = {
                **row,
                'id': row['customer.id'],
                'created_at': row['customer.created_at'],
                'updated_at': row['customer.updated_at']
            }
            this_customer = user_model.User(user_data)
            this_painting.owner = this_customer
            all_paintings.append(this_painting)
        return all_paintings
    return[]

@classmethod
def delete(cls,data):
    query = "DELETE FROM painting WHERE id = %(id)s"
    return connectToMySQL(DATABASE).query_db(query,data)

@classmethod
def get_by_id(cls,data):
    query = "SELECT * FROM painting WHERE painting.id = %(id)s;"
    results = connectToMySQL(DATABASE).query_db(query,data)
    if len(results) < 1:
        return False
    return results[0]

@classmethod
def update(cls,data):
    query = "UPDATE painting SET title = %(title)s, description = %(description)s, price = %(price)s WHERE id = %(id)s"
    return connectToMySQL(DATABASE).query_db(query,data)

@staticmethod
def validator(form_data):
    is_valid = True
    if len(form_data['price']) < 1:
        flash("price required")
        is_valid = False
    if len(form_data['title']) < 1:
        flash("title required")
        is_valid = False
    if len(form_data['description']) < 1:
        flash("description required")
        is_valid = False
    return is_valid 

