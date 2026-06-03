from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
    field_validator
)
from uuid import UUID, uuid4
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )
        return value


class UserResponse(UserBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# Create UserCreate object
user = UserCreate(
    name="Prinsi",
    email="prinsi@gmail.com",
    password="password123"
)

print(user)

# Create UserResponse object
response = UserResponse(
    id=uuid4(),
    name="Prinsi",
    email="prinsi@gmail.com",
    created_at=datetime.now()
)

print(response)