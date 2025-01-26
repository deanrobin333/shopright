#!/usr/bin/python3
# website/__init__.py

from flask import Flask, Blueprint
from config import Config


from flask_pymongo import PyMongo
from flask_login import LoginManager
from bson.objectid import ObjectId  # Add this import for ObjectId

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .views import views
    from .auth import auth

    from .models import User

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Initialize MongoDB
    mongo.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Query the user collection to find the user by their ID
        user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return User(
                email=user_data.get("email"),
                password=user_data.get("password"),
                _id=user_data.get("_id"),
            )
        return None

    return app
