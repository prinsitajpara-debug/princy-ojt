"""
database.py

This module contains the SQLAlchemy database instance.

The database object is initialized here and imported
wherever database access is required.
"""

from flask_sqlalchemy import SQLAlchemy

# Global database object
db = SQLAlchemy()