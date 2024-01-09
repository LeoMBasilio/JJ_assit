import mysql.connector

"""
    Descrição:
        Classe responsável por fazer a conexão com o banco de dados
"""

class Conector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def query(self, query):
        try:
            mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            mycursor = mydb.cursor()
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            return myresult
        except Exception as e:
            print(e)
        