#!/usr/bin/python3
# website/__init__.py

from flask import Flask
from config import Config

from .views import views

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(views, url_prefix='/')

    return app
