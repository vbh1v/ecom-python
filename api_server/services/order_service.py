from models.order import Order
from models.product import Product
from services.cart_service import CartService

class OrderService:
    def __init__(self):
        self.cart_service = CartService()

    def create_order(self, user_id):
        cart_items = self.cart_service.get_user_cart(user_id)
        if not cart_items:
            return None
        
        total_amount = sum(item['quantity'] * item['price'] for item in cart_items)
        order = Order(user_id, total_amount)
        order_id = order.save()
        order.add_order_details(cart_items)
        self.cart_service.clear_cart(user_id)
        return order_id

    def get_order_history(self, user_id):
        return Order.get_by_user(user_id)