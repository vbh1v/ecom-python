from database.db_connection import DatabaseConnection
from datetime import datetime, timedelta

class Order:
    def __init__(self, user_id, total_amount, id=None, order_date=None, expected_delivery_date=None):
        self.id = id
        self.user_id = user_id
        self.total_amount = total_amount
        self.order_date = order_date or datetime.now()
        self.expected_delivery_date = expected_delivery_date or (self.order_date + timedelta(days=5))  # Default: 5 days

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = """
            INSERT INTO orders (user_id, total_amount, order_date, expected_delivery_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.user_id, self.total_amount, self.order_date, self.expected_delivery_date))
        conn.commit()
        self.id = cursor.lastrowid
        db.close()
        return self.id

    def add_order_details(self, cart_items):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = """
            INSERT INTO order_details (order_id, product_id, quantity, price_at_time)
            VALUES (%s, %s, %s, %s)
        """
        for item in cart_items:
            cursor.execute(query, (self.id, item['product_id'], item['quantity'], item['price']))
        conn.commit()
        db.close()

    @staticmethod
    def get_by_user(user_id):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM orders WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        orders = cursor.fetchall()
        db.close()
        return orders