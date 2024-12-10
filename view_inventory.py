import sqlite3
from tabulate import tabulate

class ViewInventory:
    def __init__(self) -> None:
        pass

    def view_inventory(self):
        inv_db = sqlite3.connect("inventory.db")
        cursor = inv_db.cursor()

        cursor.execute("SELECT * FROM inventory")
        data = cursor.fetchall()
        print(tabulate(data, headers=["ID", "Name", "Category", "Weight",
                                      "Quantity", "Perishable?", "Expiry Date"], tablefmt="grid"))
        inv_db.commit()
        inv_db.close()
