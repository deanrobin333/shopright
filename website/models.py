#!/usr/bin/python3
# models.py

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # basket = db.Column(db.Integer, db.ForeignKey('basket.id'))

# class Basket(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     basket = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(10000))
    first_name = db.Column(db.String(150))
    items = db.relationship('Item')