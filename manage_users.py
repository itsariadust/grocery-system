import sqlite3
import bcrypt
import inquirer
from tabulate import tabulate

class ManageUsers:
    def __init__(self) -> None:
        pass

    def user_constructor(self):
        options_list = [
                'Add User',
                'Edit User',
                'Delete User',
                'View Users',
                'Exit',
        ]

        options = [
            inquirer.List('choice',
                        message="Please select an option",
                        choices=options_list,
                        ),
        ]

        answers = inquirer.prompt(options)
        self.option_handler(answers['choice'])
    
    def option_handler(self, choice):
        while True:
            flag = False
            match choice:
                case 'Add User':
                    self.add_user()
                case 'Edit User':
                    self.edit_user()
                case 'Delete User':
                    self.delete_user()
                case 'View Users':
                    self.view_users()
                case 'Exit':
                    print("Closing...")
                    flag = True
                case _:
                    print("Invalid choice. Please try again.")
            if flag is True:
                break

    def add_user(self):
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor
    
    def edit_user(self):
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor

    def delete_user(self):
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor
    
    def view_users(self):
        user_db = sqlite3.connect("users.db")
        cursor = user_db.cursor()

        cursor = cursor.execute("SELECT * FROM users")
        header_data = [description[0] for description in cursor.description]
        print(tabulate(cursor, headers=header_data))
        user_db.close()

