#!/usr/bin/python3
# website/__init__.py

from flask import Flask
from config import Config


from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # Initialize MongoDB
    mongo.init_app(app)

    return app
