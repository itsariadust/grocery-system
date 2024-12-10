import inquirer
from inventory_database import InventoryDB
from item import Item

class EditItem:
    def __init__(self):
        self.db = InventoryDB()

    def edit_item(self):
        item_name = inquirer.text(message="Enter the item's name")
        items = self.db.get_items_by_name(item_name)

        if not items:
            print(f"No items found with the name '{item_name}'.")
            return

        if len(items) > 1:
            item_id = self.db.handle_duplicates(items)
            item = self.db.get_items_by_id(item_id)[0]
            self.edit_item_form(item)
        else:
            item = items[0]
            self.edit_item_form(item)

    def edit_item_form(self, item):
        edit_item_form = [
            inquirer.Text('name', 'Enter item name', item[1]),
            inquirer.Text('category', 'Enter item category', item[2]),
            inquirer.Text('weight', 'Enter item weight (in metric)', item[3]),
            inquirer.Text('quantity', 'Enter the number of items currently present in the inventory', item[4]),
            inquirer.Confirm('perishable', message='Is the item perishable?', default=item[5]),
        ]
        edited_item_data = inquirer.prompt(edit_item_form)
        expiry_date = None
        if edited_item_data['perishable']:
            expiry_date_prompt = [
                inquirer.Text('expiry_date', 'Enter expiry date (In MM-DD-YYYY format)', item[6]),
            ]
            expiry_date = inquirer.prompt(expiry_date_prompt)
            edited_item_data.update(expiry_date)
            edited_item_data["id"] = item[0]

        self.db.edit_item(edited_item_data)