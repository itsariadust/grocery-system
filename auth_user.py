import inquirer
import bcrypt
import sqlite3
from user_database import UserDB

class Auth:
    def get_credentials(self):
        questions = [
            inquirer.Text('username', message="Username"),
            inquirer.Password('password', message="Password"),
        ]
        credentials = inquirer.prompt(questions)

        username = credentials.get("username")
        password = credentials.get("password")

        db_credentials = self.get_credentials_from_db(username)

        if not db_credentials:
            print("Invalid Username.")
            exit()

        hashed_pass, role = db_credentials

        if not bcrypt.checkpw(password.encode(), hashed_pass.encode()):
            print("Authentication failed: Invalid password.")
            exit()

        print(f"Welcome! {username}")

        return username, role
    
    @staticmethod
    def get_credentials_from_db(username):
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor()

        cursor.execute("SELECT hashed_password, role FROM users WHERE username = ?", (username,))
        credentials = cursor.fetchone()
        user_db.close()

        return credentials


        
