import sqlite3
import inquirer
import uuid

class AddItem:
    def __init__(self) -> None:
        pass

    def item_constructor(self):
        item_form = [
            inquirer.Text('name','Enter item name'),
            inquirer.Text('category','Enter item category'),
            inquirer.Text('weight','Enter item weight (in metric)'),
            inquirer.Text('quantity','Enter the number of items currently present in the inventory'),
            inquirer.Confirm(name='perishable', message='Is the item perishable?'),
        ]
        item = inquirer.prompt(item_form)
        if item['perishable']:
            expiry_date_prompt = [
                inquirer.Text('expiry_date','Enter expiry date (In MM-DD-YYYY format)')
            ]
            expiry_date = inquirer.prompt(expiry_date_prompt)
            # expiry_date_obj = datetime.strptime(expiry_date['expiry_date'],'%m-%d-%Y')
            # I wasted so much time writing that line lmao
            item.update(expiry_date)
            item.update({"id":f'{uuid.uuid1()}'})

    
        self.insert_item_into_db(item)
    
    def insert_item_into_db(self, item):
        inventory_db = sqlite3.connect('inventory.db')
        cursor = inventory_db.cursor()

        cursor.execute('''
            INSERT INTO inventory (id, name, category, weight, quantity, perishable, expiry_date)
            VALUES (:id, :name, :category, :weight, :quantity, :perishable, :expiry_date)
        ''', item)

        inventory_db.commit()
        inventory_db.close()
