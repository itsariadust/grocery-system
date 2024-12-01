import sqlite3
import bcrypt

class InventoryDB:
    @staticmethod
    def inventory_db_init():
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