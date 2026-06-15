from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import SessionLocal
from app.models import User, Role
from app.mongo import activity_collection

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# GET /analytics/users
# ==========================
@router.get("/users")
def analytics_users(db: Session = Depends(get_db)):

    total_users = db.query(User).count()

    users_by_role = (
        db.query(
            Role.name,
            func.count(User.id)
        )
        .join(User, User.role_id == Role.id)
        .group_by(Role.name)
        .all()
    )

    role_data = {}

    for role_name, count in users_by_role:
        role_data[role_name] = count

    return {
        "total_users": total_users,
        "active_users": total_users,
        "roles": role_data
    }


# ==========================
# GET /analytics/activity
# ==========================
@router.get("/activity")
def analytics_activity():

    pipeline = [
        {
            "$group": {
                "_id": "$timestamp",
                "count": {"$sum": 1}
            }
        }
    ]

    result = activity_collection.aggregate(pipeline)

    data = {}

    for item in result:
        data[item["_id"]] = item["count"]

    return data


# ==========================
# GET /analytics/logins
# ==========================
@router.get("/logins")
def analytics_logins():

    pipeline = [
        {
            "$match": {
                "event": "login"
            }
        },
        {
            "$group": {
                "_id": "$user_id",
                "count": {"$sum": 1}
            }
        }
    ]

    result = activity_collection.aggregate(pipeline)

    data = {}

    for item in result:
        data[f"user_{item['_id']}"] = item["count"]

    return data