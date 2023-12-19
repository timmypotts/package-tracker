import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import sqlalchemy
from models import db, Package, Users
from package_routes import package_blueprint
from user_routes import user_blueprint
from dotenv import load_dotenv

load_dotenv()

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
    try:
        with app.app_context():
            db.create_all()
    except sqlalchemy.exc.IntegrityError as e:
        app.logger.error(f"Database Integrity Error: {e}")
        # additional error handling as needed

    # Register routes
    app.register_blueprint(user_blueprint)
    app.register_blueprint(package_blueprint)

    return app