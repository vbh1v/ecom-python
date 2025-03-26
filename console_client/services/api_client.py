import requests

class ApiClient:
    def __init__(self):
        self.base_url = "http://localhost:5001"
        self.user_id = None

    def signup(self, username, password):
        try:
            response = requests.post(
                f"{self.base_url}/signup", 
                json={"username": username, "password": password}
            )
            
            # Don't raise exception, just check status code
            if response.status_code == 200:
                return response.json().get('user_id')
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {e}")
            return None

    def login(self, username, password):
        try:
            response = requests.post(
                f"{self.base_url}/login", 
                json={"username": username, "password": password}
            )
            response.raise_for_status()
            self.user_id = response.json().get('user_id')
            return self.user_id
        except requests.exceptions.RequestException as e:
            print(f"Error during login: {e}")
            return None

    def get_categories(self):
        try:
            response = requests.get(f"{self.base_url}/categories")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting categories: {e}")
            return []

    def get_products(self, category_id):
        try:
            response = requests.get(f"{self.base_url}/products/{category_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting products: {e}")
            return []

    def add_to_cart(self, product_id, quantity):
        try:
            response = requests.post(
                f"{self.base_url}/cart/add", 
                json={"user_id": self.user_id, "product_id": product_id, "quantity": quantity}
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error adding to cart: {e}")
            return False

    def buy_cart(self):
        try:
            response = requests.post(
                f"{self.base_url}/cart/buy", 
                json={"user_id": self.user_id}
            )
            response.raise_for_status()
            return response.json().get('order_id')
        except requests.exceptions.RequestException as e:
            print(f"Error buying cart: {e}")
            return None

    def get_order_history(self):
        try:
            response = requests.get(f"{self.base_url}/orders/{self.user_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting order history: {e}")
            return []