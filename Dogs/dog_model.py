from MySQLConnection import connectToMySQL
DATABASE = 'dogs_db'

class Dog:
    def __init__(self,data):
        self.id = data['id'] 
        self.name = data['name'] 
        self.breed = data['breed']
        self.color = data['color'] 
        self.age = data['age'] 
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at'] 

    @classmethod
    def get_all():
        query = "SELECT *FROM dogs;"
        results = connectToMySQL(DATABASE)

        