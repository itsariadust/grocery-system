import sqlite3
import bcrypt

class UserDB:
    @staticmethod
    def user_db_init():
        # Connect to SQLite database
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor()

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                hashed_password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

        # Add some sample users (hashed passwords)
        add_admin = [
            ("admin", bcrypt.hashpw("password".encode(), bcrypt.gensalt()).decode(), "admin"),
        ]
        
        cursor.executemany("""
            INSERT OR IGNORE INTO users (username, hashed_password, role)
            VALUES (?, ?, ?)
        """, add_admin)

        user_db.commit()
        user_db.close()

    
