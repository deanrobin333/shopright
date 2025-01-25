#!/usr/bin/python3
# config.py

import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    MONGO_URI = os.environ.get('MONGO_URI') or \
        'mongodb://localhost:27017/mydb'
    SECRET_KEY = os.environ.get('SECRET_KEY')