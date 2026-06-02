from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before():
    print(f"Request received: {request.method} {request.path}")

@app.route("/")
def home():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)