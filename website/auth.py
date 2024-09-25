#!/usr/bin/python3
# auth.py

from flask import Blueprint, render_template, request, flash
from flask import redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from website import db
# from . import app

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='Error')

    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email Already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            new_user = User(
                email=email, first_name=first_name,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
                )
            
            # with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('views.home'))

            flash('Account created!', category='success')
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    return "Logout"


    