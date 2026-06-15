# # from fastapi import FastAPI

# # app = FastAPI()

# # @app.get("/")
# # def home():
# #     return {"message": "Day 5 Project Running"}
# from fastapi import FastAPI

# from app.database import engine
# from app.models import Base
# from app.routes.users import router as user_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.include_router(user_router)

# @app.get("/")
# def home():
#     return {"message": "Working"}


from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes.users import router as user_router
from app.routes.analytics import router as analytics_router

# Create PostgreSQL tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Day 5 Analytics App"
)

# User Routes
app.include_router(user_router)

# Analytics Routes
app.include_router(analytics_router)

@app.get("/")
def home():
    return {
        "message": "Day 5 Analytics App Running"
    }