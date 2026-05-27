import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "DefaultApp")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    DEFAULT_ENCODING = os.getenv("DEFAULT_ENCODING", "utf-8")