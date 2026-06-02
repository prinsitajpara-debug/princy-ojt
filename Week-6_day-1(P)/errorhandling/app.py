from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)


# Custom Exception Class
class AppError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


# Sample Data
users = {
    1: "Prinsi",
    2: "Jensi"
}


# Route
@app.route("/users/<int:user_id>")
def get_user(user_id):

    if user_id not in users:
        abort(404)

    return jsonify({
        "success": True,
        "data": {
            "id": user_id,
            "name": users[user_id]
        }
    })


# Route using Custom Error
@app.route("/admin")
def admin():
    raise AppError("Admin access required", 403)


# Handle Custom Errors
@app.errorhandler(AppError)
def handle_app_error(error):
    return jsonify({
        "success": False,
        "error": {
            "code": error.status_code,
            "message": error.message
        }
    }), error.status_code


# Handle 404 Errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": {
            "code": 404,
            "message": "Resource not found"
        }
    }), 404


# Handle 400 Errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": {
            "code": 400,
            "message": "Bad request"
        }
    }), 400


if __name__ == "__main__":
    app.run(debug=True)