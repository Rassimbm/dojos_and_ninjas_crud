from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_rev"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
                    SELECT *
                    FROM dojos;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dict_row in results:
            dojos.append(cls(dict_row))
        return dojos