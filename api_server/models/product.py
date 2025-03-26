from database.db_connection import DatabaseConnection

class Product:
    def __init__(self, name, price, category_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.name, self.price, self.category_id))
        conn.commit()
        self.id = cursor.lastrowid
        db.close()

    @staticmethod
    def get_by_category(category_id):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM products WHERE category_id = %s"
        cursor.execute(query, (category_id,))
        products = cursor.fetchall()
        db.close()
        return products