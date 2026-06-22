# from fastapi import APIRouter

# router = APIRouter(prefix="/auth", tags=["Auth"])

# #register endpoint
# @router.post("/register")
# def register():
#     return {"message": "user registered"}

# @router.post("/login")
# def login():
#     return {
#         "access_token": "jwt-token",
#         "token_type": "bearer"
#     }

# @router.post("/refresh")
# def refresh_token():
#     return {"message": "new token generated"}

# @router.post("/logout")
# def logout():
#     return {"message": "logged out"}

# @router.post("/change-password")
# def change_password():
#     return {"message": "password changed"}

# @router.get("/me")
# def me():
#     return {"email": "admin@test.com"}

# # from fastapi import APIRouter
# # from app.schemas.auth import RegisterRequest

# # router = APIRouter(
# #     prefix="/auth",
# #     tags=["Auth"]
# # )

# # @router.post("/register")
# # def register(user: RegisterRequest):
# #     return {
# #         "username": user.username,
# #         "email": user.email,
# #         "message": "user registered"
# #     }


from fastapi import APIRouter, HTTPException, status, Header

from app.schemas.auth import RegisterRequest, LoginRequest, ChangePasswordRequest
from app.services import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


# Register endpoint
@router.post("/register")
def register(user: RegisterRequest):
    try:
        created = auth_service.register_user(user.username, user.email, user.password)
        return {"username": created["username"], "email": created["email"], "message": "user registered"}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")


# Login endpoint
@router.post("/login")
def login(user: LoginRequest):
    auth = auth_service.authenticate_user(user.email, user.password)
    if not auth:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = auth_service.generate_token(user.email)
    return {"email": user.email, "access_token": token, "token_type": "bearer"}


# Refresh token (not implemented)
@router.post("/refresh")
def refresh_token():
    return {"message": "new token generated"}


# Logout (not implemented)
@router.post("/logout")
def logout():
    return {"message": "logged out"}


@router.post("/change-password")
def change_password(data: ChangePasswordRequest, authorization: str | None = Header(None)):
    # Require Authorization: Bearer <token>
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header")
    token = parts[1]
    user = auth_service.get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    try:
        auth_service.change_password(user["email"], data.old_password, data.new_password)
        return {"old_password": data.old_password, "message": "password changed successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# Current user (optional token header)
@router.get("/me")
def me(authorization: str | None = Header(None)):
    # Expect header Authorization: Bearer <token>
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header")
    token = parts[1]
    user = auth_service.get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user