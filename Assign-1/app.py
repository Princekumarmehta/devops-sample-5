from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["flaskdb"]
collection = db["items"]


@app.route("/create", methods=["POST"])
def create():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Data inserted"}), 201


@app.route("/read", methods=["GET"])
def read():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200


@app.route("/update", methods=["PUT"])
def update():
    data = request.json
    filter_criteria = {"name": data["name"]}
    update_data = {"$set": {"value": data["value"]}}
    collection.update_one(filter_criteria, update_data)
    return jsonify({"message": "Data updated"}), 200


@app.route("/delete", methods=["DELETE"])
def delete():
    data = request.json
    collection.delete_one({"name": data["name"]})
    return jsonify({"message": "Data deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
