from flask import Flask, request

app = Flask(__name__)

@app.before_request
def log_request():
    print(
        f"Method: {request.method} | "
        f"URL: {request.url} | "
        f"IP: {request.remote_addr}"
    )

@app.route("/")
def home():
    return "Home Page"

if __name__ == "__main__":
    app.run(debug=True)