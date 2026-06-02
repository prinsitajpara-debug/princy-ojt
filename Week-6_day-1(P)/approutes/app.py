# #get and post method 

# from flask import Flask, request
# app = Flask(__name__)
# users=[]
# #get method
# @app.route("/users", methods=["GET"])
# def get_users():
#     return{
#         "users":[
#             {"id":1, "name":"prinsi"},
#             {"id":2, "name":"jensi"}
#         ]
#     }
# #post method
# @app.route("/users", methods=["POST"])
# def create_user():
#     data = request.get_json()
#     users.append(data)
#     return {"message":"User created successfully"}, 201

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return "Welcome to Flask API"

@app.route("/users", methods=["GET"])
def get_users():
    return {
        "users": [
            {"id": 1, "name": "prinsi"},
            {"id": 2, "name": "jensi"}
        ]
    }

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(data)

    return {
        "message": "User created successfully"
    }, 201

if __name__ == "__main__":
    app.run(debug=True)