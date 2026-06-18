from fastapi import FastAPI

from .database import Base
from .database import engine

from .routers.auth import router


Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="JWT Authentication API",
    debug=True
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "FastAPI Auth API Running"
    }