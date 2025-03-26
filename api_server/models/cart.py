from database.db_connection import DatabaseConnection

class Cart:
    def __init__(self, user_id, product_id, quantity, id=None):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO carts (user_id, product_id, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.user_id, self.product_id, self.quantity))
        conn.commit()
        self.id = cursor.lastrowid
        db.close()

    @staticmethod
    def get_by_user(user_id):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM carts WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        cart_items = cursor.fetchall()
        db.close()
        return cart_items

    @staticmethod
    def clear_by_user(user_id):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "DELETE FROM carts WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        db.close()