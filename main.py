import inquirer
from auth_user import Auth
from user_database import UserDB
import os

class GrocerySystem:
    if not os.path.exists("users.db"):
        print("Database not found. Creating 'users.db'...")
        UserDB.initialize_db()

    user = Auth.get_credentials()
    if not user:
        exit()

    print("Grocery System v0.1")
    options = [
        inquirer.List('choice',
                      message="What do you want to do today",
                      choices=['Add Item to Inventory', 'Edit Item in Inventory', 'Delete Item in Inventory', 'View Inventory'],
                      ),
    ]
    answers = inquirer.prompt(options)

def main():
    GrocerySystem()

if __name__ == "__main__":
    main()