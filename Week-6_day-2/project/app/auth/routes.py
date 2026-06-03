# from flask import Blueprint, jsonify

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/login")
# def login():
#     return jsonify({
#         "message": "Login Page"
#     })


from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return jsonify({
        "message": "Login Route Working"
    })