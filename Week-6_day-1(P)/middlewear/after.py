from flask import Flask

app = Flask(__name__)

@app.after_request
def after(response):
    print("Response sent")
    return response

@app.route("/")
def home():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)