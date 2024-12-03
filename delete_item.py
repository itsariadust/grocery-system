import sqlite3
import inquirer
from tabulate import tabulate

class DeleteItem:
    def __init__(self) -> None:
        pass

    def item_remover(self):
        item_name = inquirer.text(message="Enter the item's name")
        self.delete_item_from_db(item_name)

    def delete_item_from_db(self, item_name):
        inventory_db = sqlite3.connect("inventory.db")
        cursor = inventory_db.cursor()

        cursor.execute("SELECT * FROM inventory WHERE name = ?", (item_name,))

        results = cursor.fetchall()

        if not results:
            print(f"No items found with the name '{item_name}'.")
            return

        if len(results) > 1:
            duplicate_items = {"ID": [], "Name": []}

            for row in results:
                duplicate_items["ID"].append(row[0])
                duplicate_items["Name"].append(row[1])

            print("There are duplicate items. Enter the ID of the item that you wish to remove.")
            print(tabulate(duplicate_items))
            item_id = inquirer.text(message="ID")
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
