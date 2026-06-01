"""
OOP Module - User, AdminUser, Post, Comment system
"""

from dataclasses import dataclass


class User:
    """User class."""

    def __init__(self, username: str):
        self._username = username

    @property
    def username(self):
        """Get username."""
        return self._username

    def create_post(self, content: str):
        """Create a post."""
        return Post(content, self.username)


class AdminUser(User):
    """Admin user with extra permissions."""

    def ban_user(self, user: User):
        """Ban a user (simulation)."""
        return f"{user.username} banned"


class Post:
    """Post class."""

    def __init__(self, content: str, author: str):
        self.content = content
        self.author = author
        self.likes = 0
        self.comments = []

    def add_like(self):
        """Increase like count."""
        self.likes += 1

    def add_comment(self, comment):
        """Add comment."""
        self.comments.append(comment)


@dataclass
class Comment:
    """Comment model."""
    message: str
    author: str