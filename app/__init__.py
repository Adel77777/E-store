from flask import Flask
from .extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    @app.context_processor
    def inject_shop():
        return {"shop_name": app.config["SHOP_NAME"], "accent_color": app.config["ACCENT_COLOR"]},
        "background_color": app.config["BACKGROUND_COLOR"], "shop_description": app.config["SHOP_DESCRIPTION"]}
   

    with app.app_context():
        from . import models
        db.create_all()

    return app
