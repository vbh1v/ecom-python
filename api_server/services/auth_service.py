from database.db_connection import DatabaseConnection

class AuthService:
    def login(self, username, password):
        db = DatabaseConnection()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT id FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user_id = cursor.fetchone()
        db.close()
        return user_id[0] if user_id else None

    def signup(self, username, password):
        from models.user import User
        user = User(username, password)
        user.save()
        return self.login(username, password)