import sqlite3
from tabulate import tabulate
import inquirer
from item import Item

class InventoryDB:
    def __init__(self, db_path='inventory.db'):
        self.db_path = db_path
        self.inventory_db_init()

    def inventory_db_init(self):
        inventory_db = sqlite3.connect(self.db_path)
        cursor = inventory_db.cursor()

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

        inventory_db.commit()
        inventory_db.close()
    
    def insert_item(self, item):
        inventory_db = sqlite3.connect(self.db_path)
        cursor = inventory_db.cursor()

        cursor.execute('''
            INSERT INTO inventory (id, name, category, weight, quantity, perishable, expiry_date)
            VALUES (:id, :name, :category, :weight, :quantity, :perishable, :expiry_date)
        ''', vars(item))

        inventory_db.commit()
        inventory_db.close()

    def get_items_by_name(self, item_name):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory WHERE name = ?", (item_name,))
            return cursor.fetchall()

    def get_items_by_id(self, item_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
            return cursor.fetchall()

    def delete_item_by_name(self, item):
        confirm = inquirer.confirm(message=f"Are you sure you want to delete '{item[1]}'?")
        if confirm:
            inventory_db = sqlite3.connect(self.db_path)
            cursor = inventory_db.cursor()
            cursor.execute("DELETE FROM inventory WHERE name = ?", (item[1],))
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
        duplicate_items = {
            "ID": [],
            "Name": [],
            "Category": [],
            "Weight": [],
            "Quantity": [],
            "Perishable": [],
            "Expiry Date": []
        }

        for row in results:
            duplicate_items["ID"].append(row[0])
            duplicate_items["Name"].append(row[1])
            duplicate_items["Category"].append(row[2])
            duplicate_items["Weight"].append(row[3])
            duplicate_items["Quantity"].append(row[4])
            duplicate_items["Perishable"].append(row[5])
            duplicate_items["Expiry Date"].append(row[6])

        print("Duplicated detected. Please select one item from the table.")
        print(tabulate(duplicate_items,headers=["ID", "Name", "Category", "Weight",
                                                "Quantity", "Perishable?", "Expiry Date"], tablefmt="grid"))
        item_id = inquirer.text(message="ID")
        return item_id

    def edit_item(self, item):
        inventory_db = sqlite3.connect(self.db_path)
        cursor = inventory_db.cursor()
        try:
            cursor.execute('''
                UPDATE inventory
                SET name = :name, category = :category, weight = :weight, quantity = :quantity, 
                perishable = :perishable, expiry_date = :expiry_date
                WHERE id = :id
            ''', item)
        except sqlite3.Error as e:
            print("SQLite error:", e)
        inventory_db.commit()
        inventory_db.close()