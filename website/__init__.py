#!/usr/bin/python3
# __init__.py

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.url_map.strict_slashes = False
    from .views import views
    from .auth import auth

    from .models import User
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    db.init_app(app)


    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app 
