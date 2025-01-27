#!/usr/bin/python3
# models.py

from bson.objectid import ObjectId
from flask_login import UserMixin
import uuid


class Item:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise ValueError("Item name must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Item price must be a positive number.")
        
        self._id = str(uuid.uuid4())
        self.name = name
        self.price = float(price)

    def to_dict(self):
        """Convert the item to a dictionary for serialization."""
        return {
            "_id": self._id,
            "name": self.name,
            "price": self.price
            }


class Cart:
    def __init__(self, title, supermarket, date):
        self._id = str(uuid.uuid4())  # Generate a unique ID as a string
        self.title = title
        self.supermarket = supermarket
        self.date = date
        self.cart_items = []  # Changed from 'items' to 'cart_items'
        self.total = 0.0

    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Only Item objects can be added to the cart.")
        
        self.cart_items.append(item)  # Changed from 'items' to 'cart_items'
        self.total += item.price  # Update the total price

    def to_dict(self):
        """Convert the cart to a dictionary for serialization."""
        return {
            "_id": self._id,
            "title": self.title,
            "supermarket": self.supermarket,
            "date": self.date,
            "cart_items": [item.to_dict() for item in self.cart_items],  # Serialize cart_items
            "total": self.total
        }


class User(UserMixin):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id  # Store MongoDB's ObjectId for the user
        self.carts = []  # List of Cart objects

    def add_cart(self, cart):
        if not isinstance(cart, Cart):
            raise ValueError("Only Cart objects can be added.")
        
        self.carts.append(cart)  # Store the actual Cart object

    def to_dict(self):
        """Convert the user to a dictionary for serialization."""
        return {
            "email": self.email,
            "password": self.password,
            "carts": [cart.to_dict() for cart in self.carts]  # Serialize carts
        }

    # Flask-Login required methods
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)  # Flask-Login expects a string ID
