from database.db_connection import DatabaseConnection

class AuthService:
    def login(self, username, password):
        db = DatabaseConnection()
        conn = db.connect()
        if not conn:
            print("Failed to connect to database")
            return None
            
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        db.close()
        
        if result:
            return result['id']
        return None

    def signup(self, username, password):
        from models.user import User
        user = User(username, password)
        user.save()
        return self.login(username, password)