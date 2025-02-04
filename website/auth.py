#!/usr/bin/python3
# auth.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from bson.objectid import ObjectId
from website import mongo
from .models import User  # Import your User class

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_data = mongo.db.users.find_one({"email": email})
        

        if user_data:
            if check_password_hash(user_data['password'], password):
                flash('Logged in successfully!', category='success')
                
                # Create a User object
                user = User(email=user_data['email'], password=user_data['password'], _id=user_data['_id'])
                login_user(user, remember=True)
                return redirect(url_for('views.carts'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_data = mongo.db.users.find_one({"email": email})
        print(f"my {user_data}")

        if user_data:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
            new_user = {
                "email": email,
                "first_name": first_name,
                "password": hashed_password
            }
            mongo.db.users.insert_one(new_user)
            flash('Account created!', category='success')

            # Automatically log in the user after sign-up
            user_in_db = mongo.db.users.find_one({"email": email})
            user = User(email=user_in_db['email'], password=user_in_db['password'], _id=user_in_db['_id'])
            login_user(user, remember=True)

            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out Successfully!', category='success')
    return redirect(url_for('views.home'))
