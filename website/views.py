#!/usr/bin/python3
# view.py

from flask import Blueprint, render_template, jsonify

from . import mongo

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/test-db-connection', methods=['GET'])
def test_db_connection():
    try:
        # Insert a test document into a collection
        test_document = {"name": "Test User", "email": "test@example.com"}
        result = mongo.db.test_collection.insert_one(test_document)

        # Retrieve the inserted document to verify connection
        inserted_doc = mongo.db.test_collection.find_one({"_id": result.inserted_id})
        
        # Return the document as a JSON response
        return jsonify({
            "success": True,
            "message": "Connected to MongoDB successfully!",
            "inserted_document": {
                "id": str(inserted_doc["_id"]),
                "name": inserted_doc["name"],
                "email": inserted_doc["email"]
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Failed to connect to MongoDB.",
            "error": str(e)
        }), 500