#!/usr/bin/python3
# models.py

from bson.objectid import ObjectId

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}

class Cart:
    def __init__(self, title, supermarket, date):
        self.title = title
        self.supermarket = supermarket
        self.date = date
        self.items = []
        self.total = 0.0

    def add_item(self, item):
        self.items.append(item.to_dict())
        self.total += item.price

    def to_dict(self):
        return {
            "title": self.title,
            "supermarket": self.supermarket,
            "date": self.date,
            "items": self.items,
            "total": self.total
        }

class User:
    def __init__(self, email, password, _id=None):        
        self.email = email
        self.password = password
        self._id = _id  # Store MongoDB's ObjectId for user

        self.carts = []

    def add_cart(self, cart):
        self.carts.append(cart.to_dict())

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "carts": self.carts
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