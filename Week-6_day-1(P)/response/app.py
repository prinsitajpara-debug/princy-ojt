# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/users")
# def get_users():
#     return jsonify({
#         "id": 1,
#         "name": "Prinsi"
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask!"

@app.route("/users")
def get_users():
    return jsonify({
        "id": 1,
        "name": "Prinsi"
    })

if __name__ == "__main__":
    app.run(debug=True)