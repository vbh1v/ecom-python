from services.api_client import ApiClient

class ConsoleUI:
    def __init__(self):
        self.client = ApiClient()
        self.is_authenticated = False 

    def display_unauthenticated_menu(self):
        print("\n1. Signup\n2. Login\n3. Exit")

    def display_authenticated_menu(self):
        print("\n1. View Categories\n2. Add to Cart\n3. Buy Cart\n4. Order History\n5. Logout\n6. Exit")

    def run(self):
        while True:
            if not self.is_authenticated:
                self.display_unauthenticated_menu()
            else:
                self.display_authenticated_menu()

            choice = input("Enter your choice: ")

            if not self.is_authenticated:
                if choice == "1":  
                    username = input("Username: ")
                    password = input("Password: ")
                    user_id = self.client.signup(username, password)
                    if user_id:
                        self.is_authenticated = True
                        print(f"Signup successful! User ID: {user_id}")
                    else:
                        print("Signup failed")

                elif choice == "2": 
                    username = input("Username: ")
                    password = input("Password: ")
                    user_id = self.client.login(username, password)
                    if user_id:
                        self.is_authenticated = True
                        print(f"Login successful! User ID: {user_id}")
                    else:
                        print("Login failed")

                elif choice == "3": 
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

        
            else:
                if choice == "1": 
                    categories = self.client.get_categories()
                    for cat in categories:
                        print(f"{cat['id']}: {cat['name']}")
                    cat_id = int(input("Select category ID: "))
                    products = self.client.get_products(cat_id)
                    for prod in products:
                        print(f"{prod['id']}: {prod['name']} - ${prod['price']}")

                elif choice == "2": 
                    product_id = int(input("Enter Product ID: "))
                    quantity = int(input("Enter Quantity: "))
                    self.client.add_to_cart(product_id, quantity)
                    print("Added to cart!")

                elif choice == "3": 
                    order_id = self.client.buy_cart()
                    if order_id:
                        print(f"Order placed! Order ID: {order_id}")
                    else:
                        print("Failed to place order. Cart might be empty.")

                elif choice == "4": 
                    orders = self.client.get_order_history()
                    for order in orders:
                        print(f"Order ID: {order['id']}, Total: ${order['total_amount']}, Delivery: {order['expected_delivery_date']}")

                elif choice == "5": 
                    self.client.user_id = None
                    self.is_authenticated = False
                    print("Logged out!")

                elif choice == "6":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")