from flask import Flask
from .config import Config
from flask_cors import CORS, cross_origin

def create_app(config_c=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from .models import db
    db.init_app(app)
    from app import authorization, sessionsperev, sessionsperpoint, sessionsperprovider, sessionsperstation, usertovehicle
    app.register_blueprint(authorization.bp)
    app.register_blueprint(sessionsperpoint.bp)
    app.register_blueprint(sessionsperstation.bp)
    app.register_blueprint(sessionsperev.bp)
    app.register_blueprint(sessionsperprovider.bp)
    app.register_blueprint(usertovehicle.bp)
    CORS(app, supports_credentials=True)
    return app