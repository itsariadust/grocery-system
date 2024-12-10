import inquirer
from auth_user import Auth
from user_database import UserDB
from inventory_database import InventoryDB
from manage_users import ManageUsers
from add_item import AddItem
from view_inventory import ViewInventory
from delete_item import DeleteItem
import os

class GrocerySystem:
    def __init__(self) -> None:
        if not os.path.exists("inventory.db"):
            print("Inventory database not found. Creating 'inventory.db'...")
            InventoryDB().inventory_db_init()

        if not os.path.exists("users.db"):
            print("User database not found. Creating 'users.db'...")
            UserDB().user_db_init()

        user = Auth().get_credentials()
        if not user:
            exit()

        self.username, self.role = user

        self.menu()
        exit()

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
        while True:
            answers = inquirer.prompt(options)
            self.option_handler(answers['choice'])
    
    def option_handler(self, choice):
        match choice:
            case 'Add Item to Inventory':
                AddItem().item_constructor()
            case 'Edit Item in Inventory':
                self.edit_item()
            case 'Delete Item in Inventory':
                DeleteItem().remove_item()
            case 'View Inventory':
                ViewInventory().view_inventory()
            case 'Manage Users':
                user_mngr = ManageUsers()
                user_mngr.user_constructor()
            case 'Exit Program':
                print("Goodbye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")


def main():
    GrocerySystem()

if __name__ == "__main__":
    main()