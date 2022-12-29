from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_schema"
from flask_app.models import ninja_model


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len (results) > 0:
            return cls (results[0])
        return False

    @classmethod 
    def create(cls,data):
        query = "INSERT INTO  dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod 
    def get_all_with_dojos(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        all_ninjas = [] 
        dojos_instance = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                **row_from_db,
                'id': row_from_db['ninjas.id'],
                'created_at': row_from_db['ninjas.created_at'],
                'updated_at': row_from_db['ninjas.updated_at']
            }
            ninja_instance = ninja_model.Ninja(ninja_data)
           
            all_ninjas.append(ninja_instance) 
        dojos_instance.recipient = all_ninjas
        return dojos_instance