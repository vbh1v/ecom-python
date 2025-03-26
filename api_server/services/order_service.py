from models.order import Order
from models.product import Product
from services.cart_service import CartService
from database.db_connection import DatabaseConnection

class OrderService:
    def __init__(self):
        self.cart_service = CartService()

    def create_order(self, user_id):
        # Get cart items
        cart_items = self.cart_service.get_user_cart(user_id)
        if not cart_items:
            return None
        
        # Get product prices for cart items
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        
        # Enrich cart items with product prices
        for item in cart_items:
            query = "SELECT price FROM products WHERE id = %s"
            cursor.execute(query, (item['product_id'],))
            product = cursor.fetchone()
            item['price'] = product['price']
        
        db.close()
        
        # Calculate total amount
        total_amount = sum(item['quantity'] * item['price'] for item in cart_items)
        
        # Create order
        order = Order(user_id, total_amount)
        order_id = order.save()
        
        # Add order details
        order.add_order_details(cart_items)
        
        # Clear cart
        self.cart_service.clear_cart(user_id)
        
        return order_id

    def get_order_history(self, user_id):
        return Order.get_by_user(user_id)