from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Prinsi"},
    2: {"id": 2, "name": "Jensi"}
}

# Home Route
@app.route("/")
def home():
    return "Welcome to Flask!"

# GET All Users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

# GET User by ID (URL Parameter)
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

# Query Parameter
@app.route("/check", methods=["GET"])
def check_role():
    role = request.args.get("role")

    if role == "admin":
        return jsonify({"message": "Welcome Admin!"})
    else:
        return jsonify({"message": "Access Denied!"})

# POST Method + Request Body
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify({
        "message": "User Created",
        "name": data.get("name"),
        "age": data.get("age")
    }), 201

if __name__ == "__main__":
    app.run(debug=True)