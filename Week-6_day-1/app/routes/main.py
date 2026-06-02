from flask import Blueprint, request

main = Blueprint("main", __name__)

users = [
    {"id": 1, "name": "prinsi"},
    {"id": 2, "name": "jensi"}
]


@main.route("/")
def home():
    return "Hello Flask App Factory!"


@main.route("/users", methods=["GET"])
def get_users():
    return {"users": users}


@main.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return {"error": "JSON body required"}, 400

    users.append(data)
    return {"message": "User created successfully"}, 201