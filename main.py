import inquirer
from auth_user import Auth
from user_database import UserDB
import os

class GrocerySystem:
    def __init__(self) -> None:
        if not os.path.exists("users.db"):
            print("Database not found. Creating 'users.db'...")
            UserDB.initialize_db()

        user = Auth.get_credentials()
        if not user:
            exit()

        self.username, self.role = user

        self.menu()

    def menu(self):
        if self.role == "admin":
            options_list = [
                'Add Item to Inventory',
                'Edit Item in Inventory',
                'Delete Item in Inventory',
                'View Inventory',
                'Exit Program',
            ]
        elif self.role == "user":
            options_list = [
                'View Inventory',
                'Exit Program',
            ]
        else:
            print("Unknown role. Exiting.")
            exit()


        print("Grocery System v0.1")
        options = [
            inquirer.List('choice',
                        message="What do you want to do today",
                        choices=options_list,
                        ),
        ]
        answers = inquirer.prompt(options)
        self.handle_choice(answers['choice'])
    
    def option_handler(self, choice):
        if choice == 'Add Item to Inventory':
            self.add_item()
        elif choice == 'Edit Item in Inventory':
            self.edit_item()
        elif choice == 'Delete Item in Inventory':
            self.delete_item()
        elif choice == 'View Inventory':
            self.view_inventory()
        elif choice == 'Exit Program':
            print("Goodbye!")
            exit()

def main():
    GrocerySystem()

if __name__ == "__main__":
    main()