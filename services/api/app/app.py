import os
import sys
from fastapi import FastAPI, HTTPException, Depends
from app.database import engine, database
from app.routes import user_router, package_router
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
# from app.models import db, Package, User
# from app.routes.packageRoutes import package_router  
# from app.routes.userRoutes import user_router  
from dotenv import load_dotenv

load_dotenv()

# Dependency to get the database session
def get_db():
    db = database
    try:
        yield db
    finally:
        db.disconnect()

# Dependency to get the database engine
def get_engine():
    return engine

# Dependency to get the database instance
def get_database():
    return database

def create_app():
    # FastAPI app
    app = FastAPI()
    
    # CORS settings
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Load configurations and initialize SQLAlchemy
    app.config["SECRET_KEY"] = "thisissecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_API_URL")
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("Connecting to database", app.config["SQLALCHEMY_DATABASE_URI"])

    # Create tables
    try:
        with app.app_context():
            db.create_all()
    except sqlalchemy.exc.IntegrityError as e:
        app.logger.error(f"Database Integrity Error: {e}")

    # Include routers
    app.include_router(user_router, prefix="/api")
    app.include_router(package_router, prefix="/api")

    return app