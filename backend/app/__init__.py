from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = os.getenv("FLASK_SECRET_KEY")
    db.init_app(app)
    
    from app.routes import api
    from app.routes import auth
    app.register_blueprint(api.bp)
    app.register_blueprint(auth.bp)
    
    
    return app