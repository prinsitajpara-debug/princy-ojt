from fastapi import FastAPI

from app.database import (
    Base,
    engine
)

from app.routers.health import (
    router as health_router
)

from app.routers.employees import (
    router as employee_router
)

from app.routers.documents import (
    router as document_router
)

from app.middleware.logging import (
    LoggingMiddleware
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Document Management API"
)

app.add_middleware(
    LoggingMiddleware
)

app.include_router(
    health_router
)

app.include_router(
    employee_router
)

app.include_router(
    document_router
)


@app.get("/")
def root():

    return {
        "message":
        "Document Management System Running"
    }