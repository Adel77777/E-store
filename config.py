import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///estore.db")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    SHOP_NAME = "My E-Store"
    ACCENT_COLOR = "#FF5733"
    SHOP_DESCRIPTION = "Welcome to My E-Store! We offer a wide range of products to meet your needs."
    BACKGROUND_COLOR = "#F5F5F5"
