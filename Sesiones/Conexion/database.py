import mysql.connector
import os

class Conection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.database = database
        self. password = password
        self.conn = None

    def getConn(self):
        if (self.conn == None):
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return self.conn

    def getDisconection(self):
        if (self.conn != None):
            self.conn.close()
            self.conn = None


x = Conection("localhost", "root", "", "dbregistros")
conn = x.getConn()

if conn != None:
    print("Conexion exitosa")
else:
    print("Error en la conexion")
