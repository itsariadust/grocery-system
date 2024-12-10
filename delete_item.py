import inquirer
from inventory_database import InventoryDB

class DeleteItem:
    def __init__(self):
        self.db = InventoryDB()

    def remove_item(self):
        item_name = inquirer.text(message="Enter the item's name")
        items = self.db.get_items_by_name(item_name)

        if not items:
            print(f"No items found with the name '{item_name}'.")
            return

        if len(items) > 1:
            item_id = self.db.handle_duplicates(items)
            self.db.delete_item_by_id(item_id)
        else:
            self.db.delete_item_by_name(items[0])