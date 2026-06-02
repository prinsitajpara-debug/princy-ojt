from flask import Flask

def create_app(config_name=None):
    app = Flask(__name__)

    if config_name == "testing":
        app.config["TESTING"] = True

    from app.routes import main
    app.register_blueprint(main)

    return app