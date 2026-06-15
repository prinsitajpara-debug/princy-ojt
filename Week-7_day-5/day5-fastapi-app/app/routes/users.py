from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import Query

from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, LoginRequest
from app.mongo import activity_collection


router = APIRouter()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    hashed_password = pwd_context.hash(
        user.password
    )

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password,
        role_id=1
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    activity_collection.insert_one({
        "user_email": user.email,
        "event": "register"
    })

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }    


@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    is_valid = pwd_context.verify(
        user.password,
        existing_user.password_hash
    )

    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    activity_collection.insert_one({
        "user_id": existing_user.id,
        "event": "login"
    })

    return {
        "message": "login successful"
    } 

@router.post("/logout")
def logout():

    activity_collection.insert_one({
        "event": "logout"
    })

    return {
        "message": "logout successful"
    }

@router.get("/me")
def get_me(
    email: str = Query(...),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role_id": user.role_id
    }
