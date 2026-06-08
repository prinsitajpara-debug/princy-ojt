from fastapi import HTTPException


ALLOWED_FILE_TYPES = [
    "application/pdf",
    "image/jpeg",
    "image/png"
]


def validate_cv(content_type: str):

    if content_type not in ALLOWED_FILE_TYPES:

        raise HTTPException(
            status_code=400,
            detail="Only PDF, JPG, and PNG files are allowed."
        )
