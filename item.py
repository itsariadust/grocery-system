import uuid

class Item:
    """Represents an inventory item."""
    def __init__(self, name, category, weight, quantity, perishable, expiry_date=None):
        self.id = str(uuid.uuid1())
        self.name = name
        self.category = category
        self.weight = weight
        self.quantity = quantity
        self.perishable = perishable
        self.expiry_date = expiry_date