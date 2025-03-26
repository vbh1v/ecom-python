import requests

class ApiClient:
    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.user_id = None

    def signup(self, username, password):
        response = requests.post(f"{self.base_url}/signup", json={"username": username, "password": password})
        return response.json().get('user_id')

    def login(self, username, password):
        response = requests.post(f"{self.base_url}/login", json={"username": username, "password": password})
        self.user_id = response.json().get('user_id')
        return self.user_id

    def get_categories(self):
        response = requests.get(f"{self.base_url}/categories")
        return response.json()

    def get_products(self, category_id):
        response = requests.get(f"{self.base_url}/products/{category_id}")
        return response.json()

    def add_to_cart(self, product_id, quantity):
        requests.post(f"{self.base_url}/cart/add", json={"user_id": self.user_id, "product_id": product_id, "quantity": quantity})

    def buy_cart(self):
        response = requests.post(f"{self.base_url}/cart/buy", json={"user_id": self.user_id})
        return response.json().get('order_id')

    def get_order_history(self):
        response = requests.get(f"{self.base_url}/orders/{self.user_id}")
        return response.json()