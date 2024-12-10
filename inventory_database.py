import sqlite3
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

    def get_items_by_name(self, name):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory WHERE name = ?", (name,))
            return cursor.fetchall()

    def delete_item_by_name(self, item_name):
        confirm = inquirer.confirm(message=f"Are you sure you want to delete '{item_name}'?")
        if confirm:
            inventory_db = sqlite3.connect(self.db_path)
            cursor = inventory_db.cursor()
            cursor.execute("DELETE FROM inventory WHERE id = ?", (item_name[1],))
            inventory_db.commit()
            inventory_db.close()

    def delete_item_by_id(self, item_id):
        confirm = inquirer.confirm(message=f"Are you sure you want to delete '{item_id}'?")
        if confirm:
            inventory_db = sqlite3.connect(self.db_path)
            cursor = inventory_db.cursor()
            cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
            inventory_db.commit()
            inventory_db.close()
    
    def handle_duplicates(self, results):
        duplicate_items = {"ID": [], "Name": []}

        for row in results:
            duplicate_items["ID"].append(row[0])
            duplicate_items["Name"].append(row[1])

        print(tabulate(duplicate_items))
        item_id = inquirer.text(message="ID")
        self.delete_item_by_id(item_id)
        