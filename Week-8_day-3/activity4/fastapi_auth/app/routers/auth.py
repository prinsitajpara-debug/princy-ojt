from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db

from app.models import User

from app.schemas import (
    UserCreate,
    UserResponse,
    LoginRequest,
    TokenResponse
)

from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(
            user.password
        )
    )

    db.add(db_user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to create user"
        )

    db.refresh(db_user)

    return db_user


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        or_(User.email == credentials.username, User.name == credentials.username)
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        credentials.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 1800
    }


@router.get("/me")
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }