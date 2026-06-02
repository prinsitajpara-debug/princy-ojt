from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)

@app.route("/")
def home():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)