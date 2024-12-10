import sqlite3
import bcrypt
from tabulate import tabulate
import inquirer

class InventoryDB:
    def __init__(self, db_path='inventory.db'):
        self.db_path = db_path
        self.inventory_db_init()

    def inventory_db_init(self):
        inv_db = sqlite3.connect("inventory.db")
        cursor = inv_db.cursor()

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT,
                weight REAL,
                quantity INTEGER NOT NULL,
                perishable TEXT NOT NULL,
                expiry_date TEXT
            )
        """)

        inv_db.commit()
        inv_db.close()
    
    def insert_item(self, item):
        inventory_db = sqlite3.connect('inventory.db')
        cursor = inventory_db.cursor()

        cursor.execute('''
            INSERT INTO inventory (id, name, category, weight, quantity, perishable, expiry_date)
            VALUES (:id, :name, :category, :weight, :quantity, :perishable, :expiry_date)
        ''', vars(item))

        inventory_db.commit()
        inventory_db.close()

    def delete_item(self, item):
        inventory_db = sqlite3.connect("inventory.db")
        cursor = inventory_db.cursor()

        cursor.execute("SELECT * FROM inventory WHERE name = ?", (item,))

        results = cursor.fetchall()

        if not results:
            print(f"No items found with the name '{item}'.")
            return

        if len(results) > 1:
            item_id = self._duplicate_items(results)
            confirm = inquirer.confirm("Are you sure that you want to delete this item?")

            if confirm:
                cursor.execute("DELETE FROM inventory WHERE ID = ?", (item_id,))
                print("Item deleted successfully.")
                inventory_db.commit()
                inventory_db.close()
        else:
            confirm = inquirer.confirm("Are you sure that you want to delete this item?")
            if confirm:
                single_item = results[0][1]
                cursor.execute("DELETE FROM inventory WHERE Name = ?", (single_item,))
                print("Item deleted successfully.")
                inventory_db.commit()
                inventory_db.close()
    
    def _duplicate_items(self, results):
        duplicate_items = {"ID": [], "Name": []}

        for row in results:
            duplicate_items["ID"].append(row[0])
            duplicate_items["Name"].append(row[1])

        print("There are duplicate items. Enter the ID of the item that you wish to remove.")
        print(tabulate(duplicate_items))
        item_id = inquirer.text(message="ID")
        return item_id
        