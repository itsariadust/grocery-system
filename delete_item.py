import sqlite3
import inquirer
from tabulate import tabulate
from inventory_database import InventoryDB

class DeleteItem:
    def __init__(self):
        self.db = InventoryDB()

    def item_remover(self):
        item_name = inquirer.text(message="Enter the item's name")
        self.db.delete_item(item_name)
