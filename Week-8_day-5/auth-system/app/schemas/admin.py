from typing import Optional

from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool


class AssignRoleRequest(BaseModel):
    user_id: int
    role_id: int


class AssignRoleResponse(BaseModel):
    success: bool
    message: str
    user_id: int
    role_id: int


class AssignPermissionRequest(BaseModel):
    role_id: int
    permission_id: int
    assign_to_user_id: Optional[int] = None


class AssignPermissionResponse(BaseModel):
    success: bool
    message: str
    role_id: int
    permission_id: int
    assign_to_user_id: Optional[int] = None
