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
                'Manage Users',
                'Exit Program',
            ]
        elif self.role == "stock_mngr":
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
        self.option_handler(answers['choice'])
    
    def option_handler(self, choice):
        match choice:
            case 'Add Item to Inventory':
                self.add_item()
            case 'Edit Item in Inventory':
                self.edit_item()
            case 'Delete Item in Inventory':
                self.delete_item()
            case 'View Inventory':
                self.view_inventory()
            case 'Exit Program':
                print("Goodbye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")


def main():
    GrocerySystem()

if __name__ == "__main__":
    main()