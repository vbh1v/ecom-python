from flask import Flask, request, jsonify
from services.auth_service import AuthService
from services.category_service import CategoryService
from services.product_service import ProductService
from services.cart_service import CartService
from services.order_service import OrderService
from database.db_connection import get_db_connection

app = Flask(__name__)
auth_service = AuthService()
category_service = CategoryService()
product_service = ProductService()
cart_service = CartService()
order_service = OrderService()

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print(f"Signup attempt for user: {data.get('username')}")
    
    # Check if user already exists
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM users WHERE username = %s", (data.get('username'),))
    existing_user = cursor.fetchone()
    
    if existing_user:
        print(f"User {data.get('username')} already exists")
        cursor.close()
        conn.close()
        return jsonify({'error': 'Username already exists'}), 400
    
    # Attempt signup
    user_id = auth_service.signup(data['username'], data['password'])
    print(f"Signup result: {user_id}")
    
    # Verify user was created
    cursor.execute("SELECT id FROM users WHERE username = %s", (data.get('username'),))
    new_user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if new_user:
        return jsonify({'user_id': new_user['id']})
    else:
        return jsonify({'error': 'Signup failed'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(f"Login attempt for user: {username}")
    
    user_id = auth_service.login(username, password)
    print(f"Login result: {user_id}")
    
    if user_id:
        return jsonify({'user_id': user_id})
    else:
        return jsonify({'error': 'Login failed'}), 401

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = category_service.get_all_categories()
    return jsonify(categories)

@app.route('/products/<int:category_id>', methods=['GET'])
def get_products(category_id):
    products = product_service.get_products_by_category(category_id)
    return jsonify(products)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    cart_service.add_to_cart(data['user_id'], data['product_id'], data['quantity'])
    return jsonify({'message': 'Added to cart'})

@app.route('/cart/buy', methods=['POST'])
def buy_cart():
    data = request.get_json()
    order_id = order_service.create_order(data['user_id'])
    return jsonify({'order_id': order_id})

@app.route('/orders/<int:user_id>', methods=['GET'])
def get_order_history(user_id):
    orders = order_service.get_order_history(user_id)
    return jsonify(orders)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is alive'})