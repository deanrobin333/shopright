#!/usr/bin/python3
# view.py

from flask import Blueprint, render_template, jsonify

from flask import request, flash

from flask_login import login_required, current_user

from . import mongo

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/carts', methods=['GET', 'POST'])
@login_required
def carts():
    if request.method == 'POST':
        

            flash('Item added!', category='success')

    return render_template('home.html', user=current_user)