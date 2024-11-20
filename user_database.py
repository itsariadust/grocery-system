import sqlite3
import bcrypt
import os

class UserDB:
    @staticmethod
    def initialize_db():
        # Connect to SQLite database
        db = sqlite3.connect("users.db")
        cursor = db.cursor()

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

        db.commit()
        db.close()

    @staticmethod
    def get_credentials_from_db(username):
        db = sqlite3.connect("users.db")
        cursor = db.cursor()

        cursor.execute("SELECT hashed_password, role FROM users WHERE username = ?", (username,))
        credentials = cursor.fetchone()
        db.close()

        return credentials
