from database.db_connection import DatabaseConnection

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO categories (name) VALUES (%s)"
        cursor.execute(query, (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        db.close()

    @staticmethod
    def get_all():
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM categories"
        cursor.execute(query)
        categories = cursor.fetchall()
        db.close()
        return categories