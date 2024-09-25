#!/usr/bin/python3
# routes.py


from flask import Blueprint
from flask import render_template

from flask import request, flash


from flask_login import login_required, current_user
#app.url_map.strict_slashes = False

from .models import Item
from . import db

import json
from flask import jsonify

views = Blueprint('views', __name__)

#@views.route('/index')
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        item = request.form.get('item')

        if len(item) < 1:
            flash('Item is too short!', category='error')
        else:
            new_item = Item(data=item, user_id=current_user.id)

            db.session.add(new_item)
            db.session.commit()

            flash('Item added!', category='success')

    return render_template('home.html', user=current_user)

@views.route('/blog-post')
def blog():
    return render_template('blog_post.html', user=current_user)

@views.route('/delete-item', methods=['POST'])
def delete_item():
    item = json.loads(request.data)
    itemId = item['itemId']
    item = Item.query.get(itemId)

    if item:
        if item.user_id == current_user.id:
            db.session.delete(item)
            db.session.commit()

    return jsonify({})
