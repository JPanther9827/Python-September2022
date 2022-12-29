from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE
from flask import flash 
from flask_app.models import dealer_model, user_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Dealer:
    def __init__(self,data):
        self.id = data['id']
        self.model= data['model']
        self.year = data['year']
        self.price = data['price']
        self.description = data['description']
        self.make = data['make']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.customer_id = data['customer_id']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dealer JOIN customer on dealer.customer_id = customer.id;"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod 
    def create(cls,data):
        query = "INSERT INTO dealer (model,year,price,description,make,customer_id) VALUES(%(model)s,%(year)s,%(price)s,%(description)s,%(make)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_with_dealers(cls,data):
        query = "SELECT * FROM dealer JOIN customer on dealer.customer_id = customer.id WHERE dealer.customer_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            all_dealers = []
            for row in results:
                this_dealer = cls(row)
                user_data = {
                    **row,
                    'id': row['customer.id'],
                    'created_at': row['customer.created_at'],
                    'updated_at': row['customer.updated_at']
                }
                this_customer = user_model.User(user_data)
                this_dealer.owner = this_customer
                all_dealers.append(this_dealer)
            return all_dealers
        return []

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dealer WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

        
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dealer WHERE dealer.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return results[0]

    @classmethod
    def update(cls,data):
        query = "UPDATE dealer SET model = %(model)s, year = %(year)s, price = %(price)s, description = %(description)s, make = %(make)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['price']) < 1:
            flash("price required")
            is_valid = False
        if len(form_data['model']) < 1:
            flash("model required")
            is_valid = False
        if len(form_data['make']) < 1:
            flash("make required")
            is_valid = False
        if len(form_data['year']) < 1:
            flash("year required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        return is_valid