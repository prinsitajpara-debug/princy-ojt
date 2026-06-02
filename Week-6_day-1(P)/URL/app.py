from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: "Prinsi",
    2: "Jensi",
    3: "mitali"
}
@app.route("/")
def home():
    return "Welcome to Flask API"

@app.route("/users/<int:user_id>")
def get_user(user_id):
    if user_id in users:
        return jsonify({
            "id": user_id,
            "name": users[user_id]
        })
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
