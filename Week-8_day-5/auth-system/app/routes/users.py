from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.put("/{user_id}")
def update_user(user_id: int):

    current_user_id = 1

    if user_id != current_user_id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

    return {"message": "updated"}