from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(DATABASE).query_db(query) 
        all_ninjas = []
        for row_from_db in results:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len (results) > 0:
            return cls (results[0])
        return False

    @classmethod
    def create(cls,data):
        print("============================")
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id) VALUES (%(first_name)s, %(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    