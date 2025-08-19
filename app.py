from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection (make sure MongoDB is running locally or use cloud)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Missing fields"}), 400

    todo = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo)
    return jsonify({"message": "To-Do item saved successfully!", "item": todo}), 201
