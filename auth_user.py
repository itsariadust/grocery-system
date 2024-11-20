import inquirer
import bcrypt
from user_database import UserDB

class Auth:
    @staticmethod
    def get_credentials():
        questions = [
            inquirer.Text('username', message="Username: "),
            inquirer.Password('password', message="Password: "),
        ]
        credentials = inquirer.prompt(questions)

        username = credentials.get("username")
        password = credentials.get("password")

        db_credentials = UserDB.get_credentials_from_db(username)

        if not db_credentials:
            print("Invalid Username.")
            exit()

        hashed_pass, role = db_credentials

        if not bcrypt.checkpw(password.encode(), hashed_pass.encode()):
            print("Authentication failed: Invalid password.")
            exit()

        print(f"Welcome! {username}")

        return username, role


        
