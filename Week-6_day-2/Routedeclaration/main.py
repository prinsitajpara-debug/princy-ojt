from fastapi import FastAPI
from uuid import UUID
from pydantic import BaseModel

app = FastAPI()


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str


@app.get("/users", response_model=list[UserResponse])
def get_users(
    skip: int = 0,
    limit: int = 10,
    role: str | None = None
):
    return []


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID):
    return {
        "id": user_id,
        "name": "Prinsi",
        "email": "prinsi@example.com"
    }