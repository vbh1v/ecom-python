from models.cart import Cart

class CartService:
    def add_to_cart(self, user_id, product_id, quantity):
        cart_item = Cart(user_id, product_id, quantity)
        cart_item.save()

    def get_user_cart(self, user_id):
        return Cart.get_by_user(user_id)

    def clear_cart(self, user_id):
        Cart.clear_by_user(user_id)