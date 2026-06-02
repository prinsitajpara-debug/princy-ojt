from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Flask API"

@app.route("/users")
def get_users():
    role = request.args.get("role")

    if role == "admin":
        return "Welcome Admin!"
    else:
        return "Access Denied!"

if __name__ == "__main__":
    app.run(debug=True)