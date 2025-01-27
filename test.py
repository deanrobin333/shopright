#!/usr/bin/python3
# view.py

from flask import Blueprint, render_template

from flask import redirect, url_for

from flask import request, flash

from flask_login import login_required, current_user

from . import mongo

from .models import Cart  # Import the Cart model

from bson.objectid import ObjectId


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

# Route for the carts page
@views.route('/carts')
@login_required
def carts():
    # Retrieve all carts for the current user    
    user_data = mongo.db.users.find_one({"_id": ObjectId(current_user.get_id())})
    # carts = user_data.get("carts", [])
    carts = user_data.get("carts", [])
        
    return render_template('carts.html', carts=carts, user=current_user)


@views.route('/create-cart', methods=['GET', 'POST'])
@login_required
def create_cart():
    if request.method == 'POST':
        title = request.form.get('title')
        supermarket = request.form.get('supermarket')
        date = request.form.get('date')
        
        # Create a new cart object
        new_cart = Cart(title=title, supermarket=supermarket, date=date)
        
        # Add it to the user's cart collection in MongoDB
        mongo.db.users.update_one(
            {"_id": ObjectId(current_user.get_id())},
            {"$push": {"carts": new_cart.to_dict()}}
        )
        
        return redirect(url_for('views.carts'))
    
    return render_template('create_cart.html', user=current_user)



@views.route('/cart/<cart_id>', methods=['GET', 'POST'])
@login_required
def view_cart(cart_id):
    # Fetch the current user's data
    user_data = mongo.db.users.find_one({"_id": ObjectId(current_user.get_id())})
    carts = user_data.get("carts", [])
    cart = next((cart for cart in carts if cart["_id"] == cart_id), None)

    # Handle the case where the cart is not found
    if not cart:
        return "Cart not found", 404

    # Handle POST request to add an item
    if request.method == 'POST':
        # Get the form data
        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')

        # Validate the form data
        if not item_name or not item_price:
            return "Invalid item data", 400

        try:
            # Convert item price to a float
            item_price = float(item_price)

            # Create a new Item object
            new_item = {"name": item_name, "price": item_price}

            # Append the new item to the cart's items
            cart['cart_items'].append(new_item)

            # Update the cart's total
            cart['total'] += item_price

            # Update the user's cart in the database
            mongo.db.users.update_one(
                {"_id": ObjectId(current_user.get_id()), "carts._id": cart_id},
                {
                    "$set": {
                        "carts.$.cart_items": cart['cart_items'],
                        "carts.$.total": cart['total']
                    }
                }
            )
        except ValueError:
            return "Invalid price value", 400

    # Render the template with the updated cart
    return render_template('view_cart.html', cart=cart, user=current_user)


    <ul>
        {% for item in cart.cart_items %}
        <li>{{ item['name'] }} - ${{ item['price'] }}</li>
        {% else %}
        <li>No items in the cart yet!</li>
        {% endfor %}
    </ul>

    <li class="list-group-item">
            <button type="button" class="btn btn-success" >{{ item['name'] }} - ${{ item['price'] }}
                <span aria-hidden="true">&times;</span>
            </button>
        </li>





    <div class="container-sm">
        <div class="row items-list">
            <div class="col-2 item-list">{{ item['name'] }}</div>          
            <div class="col item-list">ksh{{ item['price'] }}</div>          
        </div>
      </div>