from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Dependency Injection Demo")


# ---------------------------
# Fake Database
# ---------------------------
fake_users_db = [
    {"id": 1, "name": "Prinsi", "email": "prinsi@example.com"},
    {"id": 2, "name": "John", "email": "john@example.com"}
]


# ---------------------------
# Pydantic Response Model
# ---------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    email: str


# ---------------------------
# Database Dependency
# ---------------------------
def get_db():
    print("Database session opened")

    db = fake_users_db

    try:
        yield db
    finally:
        print("Database session closed")


# ---------------------------
# Authentication Dependency
# ---------------------------
def verify_token():
    token = "secret123"  # Normally comes from request headers

    if token != "secret123":
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return {"username": "admin"}


# ---------------------------
# Route Using DB Dependency
# ---------------------------
@app.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users(
    db=Depends(get_db)
):
    return db


# ---------------------------
# Route Using Auth Dependency
# ---------------------------
@app.get("/profile")
def profile(
    current_user=Depends(verify_token)
):
    return {
        "message": "Welcome",
        "user": current_user
    }


# ---------------------------
# Multiple Dependencies
# ---------------------------
@app.get("/dashboard")
def dashboard(
    current_user=Depends(verify_token),
    db=Depends(get_db)
):
    return {
        "user": current_user,
        "total_users": len(db)
    }


# ---------------------------
# Root Route
# ---------------------------
@app.get("/")
def home():
    return {
        "message": "FastAPI Dependency Injection Example"
    }