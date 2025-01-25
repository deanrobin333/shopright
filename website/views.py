#!/usr/bin/python3
# view.py

from flask import Blueprint, render_template, jsonify

from . import mongo

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')
