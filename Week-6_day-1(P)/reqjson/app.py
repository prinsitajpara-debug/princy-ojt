from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Server Running!"

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return jsonify({
        "message": "User created",
        "name": name,
        "age": age
    }), 201

if __name__ == "__main__":
    app.run(debug=True)