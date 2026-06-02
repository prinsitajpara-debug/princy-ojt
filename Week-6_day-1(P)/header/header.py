# from flask import Flask

# app = Flask(__name__)

# @app.after_request
# def add_headers(response):
#     response.headers["X-App-Name"] = "Flask API"
#     response.headers["X-Version"] = "1.0"
#     return response

# @app.route("/")
# def home():
#     return "Hello Flask!"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.after_request
def add_headers(response):
    print("After request executed - modifying response headers")

    response.headers["X-App-Name"] = "Flask API"
    response.headers["X-Version"] = "1.0"

    return response

@app.route("/")
def home():
    print("Home route executed")
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)