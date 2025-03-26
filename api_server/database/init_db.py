import mysql.connector
from mysql.connector import Error
import os

def init_database():
    # Initial connection without database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123"
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
            print("Database 'ecommerce_db' created successfully")
            
            # Switch to the database
            cursor.execute("USE ecommerce_db")
            
            # Read and execute the schema.sql file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            schema_path = os.path.join(current_dir, 'schema.sql')
            
            with open(schema_path, 'r') as schema_file:
                # Read the entire file content
                schema_content = schema_file.read()
                
                # Split the schema file into individual commands
                commands = schema_content.split(';')
                
                for command in commands:
                    # Skip empty commands
                    if command.strip():
                        try:
                            cursor.execute(command)
                            connection.commit()
                        except Error as e:
                            # Skip the "already exists" errors
                            if "already exists" not in str(e):
                                print(f"Error executing command: {e}")
                
            print("Database schema initialized successfully")
            
            # Add some sample data
            add_sample_data(connection)
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

def add_sample_data(connection):
    try:
        cursor = connection.cursor()
        
        # Add sample categories
        categories = [
            "Electronics",
            "Clothing",
            "Books",
            "Home & Kitchen"
        ]
        
        for category in categories:
            cursor.execute("INSERT INTO categories (name) VALUES (%s)", (category,))
        
        # Add sample products
        products = [
    ("Smartphone", 49999, 1),  
    ("Laptop", 79999, 1),  
    ("Kurta", 1499, 2),  
    ("Jeans", 2499, 2),  
    ("Hindi Novel", 499, 3),  
    ("Recipe Book", 999, 3),  
    ("Mixer Grinder", 3499, 4),  
    ("Coffee Maker", 2499, 4)  
]


        
        for product in products:
            cursor.execute(
                "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)",
                product
            )
        
        connection.commit()
        print("Sample data added successfully")
        
    except Error as e:
        print(f"Error adding sample data: {e}")

if __name__ == "__main__":
    init_database() 