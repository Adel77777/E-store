import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///estore.db")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024