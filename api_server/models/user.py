from database.db_connection import DatabaseConnection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (self.username, self.password))
        conn.commit()
        db.close()