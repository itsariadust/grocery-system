import inquirer
import uuid
from inventory_database import InventoryDB
from item import Item

class AddItem:
    def __init__(self):
        self.db = InventoryDB()

    def item_constructor(self):
        item_form = [
            inquirer.Text('name','Enter item name'),
            inquirer.Text('category','Enter item category'),
            inquirer.Text('weight','Enter item weight (in metric)'),
            inquirer.Text('quantity','Enter the number of items currently present in the inventory'),
            inquirer.Confirm(name='perishable', message='Is the item perishable?'),
        ]
        item_data = inquirer.prompt(item_form)
        expiry_date = None
        if item_data['perishable']:
            expiry_date_prompt = [
                inquirer.Text('expiry_date','Enter expiry date (In MM-DD-YYYY format)')
            ]
            expiry_date_data = inquirer.prompt(expiry_date_prompt)
            expiry_date = expiry_date_data['expiry_date']

        item = Item(
            name=item_data['name'],
            category=item_data['category'],
            weight=item_data['weight'],
            quantity=int(item_data['quantity']),
            perishable=item_data['perishable'],
            expiry_date=expiry_date
        )
        self.db.insert_item(item)