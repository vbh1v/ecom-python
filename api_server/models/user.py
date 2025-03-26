from database.db_connection import DatabaseConnection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db = DatabaseConnection()
        conn = db.connect()
        if not conn:
            print("Failed to connect to database")
            return None
        
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(query, (self.username, self.password))
            conn.commit()
            print(f"User {self.username} saved successfully")
        except Exception as e:
            print(f"Error saving user: {e}")
            conn.rollback()
        finally:
            db.close()