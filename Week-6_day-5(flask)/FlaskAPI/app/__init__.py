"""
__init__.py

Creates and configures Flask application.
"""

from flask import Flask

from app.database import db
from app.routes import employee_bp


def create_app():
    """
    Application Factory.

    Returns:
        Flask application instance.
    """

    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///employees.db"

    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    ] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(employee_bp)

    return app
