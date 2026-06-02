from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Hello Flask!"

@main.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Prinsi"},
        {"id": 2, "name": "Jensi"}
    ])