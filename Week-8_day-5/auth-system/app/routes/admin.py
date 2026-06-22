from fastapi import APIRouter

from app.schemas.admin import (
    AssignPermissionRequest,
    AssignPermissionResponse,
    AssignRoleRequest,
    AssignRoleResponse,
    UserRead,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/users", response_model=list[UserRead])
def get_users():
    return [
        {
            "id": 1,
            "username": "admin_user",
            "email": "admin@example.com",
            "is_active": True,
        },
        {
            "id": 2,
            "username": "johndoe",
            "email": "john@example.com",
            "is_active": True,
        },
        {
            "id": 3,
            "username": "marysmith",
            "email": "mary@example.com",
            "is_active": False,
        },
    ]

# assign role
@router.post("/assign-role", response_model=AssignRoleResponse)
def assign_role(request: AssignRoleRequest):
    return {
        "success": True,
        "message": "Role successfully assigned.",
        "user_id": request.user_id,
        "role_id": request.role_id,
    }

# assign permission
@router.post("/assign-permission", response_model=AssignPermissionResponse)
def assign_permission(request: AssignPermissionRequest):
    return {
        "success": True,
        "message": "Permission successfully assigned.",
        "role_id": request.role_id,
        "permission_id": request.permission_id,
        "assign_to_user_id": request.assign_to_user_id,
    }

