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
    
    @classmethod
    def save(cls,data):
        query = """
                    INSERT INTO dojos (name)
                    VALUES %(name)s;
                """
        result_id = connectToMySQL(cls.DB).query_db(query,data)
        return result_id
    
    @classmethod
    def get_one(cls, data):
        query = """
                    SELECT *
                    FROM dojos
                    WHERE id = %(id)s;
                """
        results =  connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])
    
    # @classmethod
    # def update(cls,data):
    #     query = """
    #                 UPDATE dojos
    #                 SET name = %(name)s
    #                 WHERE id = %(id)s;
    #             """
    #     return connectToMySQL(cls.DB).query_db(query,data)
    
    # @classmethod
    # def delete(cls,data):
    #     query = """
    #                 DELETE dojos
    #                 WHERE id = %(id)s;
    #             """
    #     return connectToMySQL(cls.DB).query_db(query,data)