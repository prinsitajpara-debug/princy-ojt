"""
conftest.py

Pytest fixtures for Flask testing.
"""

import os
import sys
import pytest

# Ensure the project root is on sys.path so tests can import the `app` package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app
from app.database import db


@pytest.fixture
def client():
    """
    Create test client.

    Uses SQLite in-memory database.
    """

    app = create_app()

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///:memory:"

    app.config["TESTING"] = True

    with app.test_client() as client:

        with app.app_context():
            db.create_all()

        yield client

        with app.app_context():
            db.drop_all()
