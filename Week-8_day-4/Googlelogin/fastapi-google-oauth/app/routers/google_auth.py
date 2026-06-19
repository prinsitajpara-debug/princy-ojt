from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth

from app.core.config import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)

router = APIRouter()

oauth = OAuth()

oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=
    "https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)


@router.get("/login/google")
async def login(request: Request):

    redirect_uri = request.url_for("auth")

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/auth")
async def auth(request: Request):

    token = await oauth.google.authorize_access_token(
        request
    )

    user = token["userinfo"]

    return {
        "name": user["name"],
        "email": user["email"]
    }