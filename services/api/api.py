from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import Package, Users, db
import os
import sys
from models import db
from packageRoutes import package_blueprint
from userRoutes import user_blueprint

from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={"/api/*": {"origins": "*"}})
    
    # Load configurations and initialize SQLAlchemy
    app.config["SECRET_KEY"] = "thisissecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_API_URL")
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("Connecting to database", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register routes
    app.register_blueprint(user_blueprint)
    app.register_blueprint(package_blueprint)

    return app

