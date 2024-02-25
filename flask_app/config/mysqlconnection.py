import pymysql.cursors
class MySQLconnection:
    def __init__(self,db):
        self.connection = pymysql.connect(
            host = "locahost",
            user = "root",
            password = "root",
            db = db,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True

        )

    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f"Running query: {query}")

                cursor.execute(query)
                
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
                
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLconnection(db)