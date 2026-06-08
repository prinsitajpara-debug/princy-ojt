import os

from fastapi import Header
from fastapi import HTTPException

API_KEY = os.getenv(
    "API_KEY",
    "secret123"
)


async def verify_api_key(
    x_api_key: str = Header(...)
):

    if x_api_key != API_KEY:

        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )