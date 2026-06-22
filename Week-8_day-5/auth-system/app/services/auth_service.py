import hashlib
import uuid
from typing import Optional

# Simple in-memory user store. For production replace with DB-backed logic.
_users: dict[str, dict] = {}
_tokens: dict[str, str] = {}
_next_id = 1


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username: str, email: str, password: str) -> dict:
    global _next_id
    if email in _users:
        raise ValueError("user already exists")

    user = {
        "id": _next_id,
        "username": username,
        "email": email,
        "password_hash": _hash_password(password),
        "is_active": True,
    }
    _users[email] = user
    _next_id += 1
    return {k: v for k, v in user.items() if k != "password_hash"}


def authenticate_user(email: str, password: str) -> Optional[dict]:
    user = _users.get(email)
    if not user:
        return None
    if user["password_hash"] != _hash_password(password):
        return None
    return {k: v for k, v in user.items() if k != "password_hash"}


def generate_token(email: str) -> str:
    token = uuid.uuid4().hex
    _tokens[token] = email
    return token


def change_password(email: str, old_password: str, new_password: str) -> bool:
    user = _users.get(email)
    if not user:
        raise ValueError("user not found")
    if user["password_hash"] != _hash_password(old_password):
        raise ValueError("old password incorrect")
    user["password_hash"] = _hash_password(new_password)
    return True


def get_user_by_token(token: str) -> Optional[dict]:
    email = _tokens.get(token)
    if not email:
        return None
    user = _users.get(email)
    if not user:
        return None
    return {k: v for k, v in user.items() if k != "password_hash"}
