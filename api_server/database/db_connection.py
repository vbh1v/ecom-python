import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="ecommerce_db"
        )
        print("Database connection successful")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

class DatabaseConnection:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "password123"
        self.database = "ecommerce_db"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()