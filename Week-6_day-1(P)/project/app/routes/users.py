from flask import Blueprint, request, jsonify
import json
import os

users_bp = Blueprint("users", __name__)

DB_FILE = "users.json"


def load_users():
    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(DB_FILE, "w") as file:
        json.dump(users, file, indent=4)



# GET LIST (WITH FILTER)

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = load_users()

    name = request.args.get("name")

    if name:
        users = [
            user for user in users
            if name.lower() in user["name"].lower()
        ]

    return jsonify(users)


# GET ONE

@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = load_users()

    user = next(
        (u for u in users if u["id"] == user_id),
        None
    )

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify(user)


# POST

@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON data required"
        }), 400

    if "name" not in data or "age" not in data:
        return jsonify({
            "error": "name and age required"
        }), 400

    users = load_users()

    new_id = 1

    if users:
        new_id = max(
            user["id"] for user in users
        ) + 1

    new_user = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)
    save_users(users)

    return jsonify(new_user), 201


# PUT

@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON data required"
        }), 400

    users = load_users()

    user = next(
        (u for u in users if u["id"] == user_id),
        None
    )

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    if "name" not in data or "age" not in data:
        return jsonify({
            "error": "name and age required"
        }), 400

    user["name"] = data["name"]
    user["age"] = data["age"]

    save_users(users)

    return jsonify(user)


# DELETE

@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = load_users()

    user = next(
        (u for u in users if u["id"] == user_id),
        None
    )

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    users.remove(user)

    save_users(users)

    return jsonify({
        "message": "User deleted"
    })