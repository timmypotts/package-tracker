from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base, database
from app.routes.package_routes import package_router
from app.routes.user_routes import user_router

# Initialize FastAPI app
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

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Event handler to create tables and connect to the database on startup
@app.on_event("startup")
async def startup():
    # Create tables
    Base.metadata.create_all(bind=engine)

    # Connect to the database
    await database.connect()

# Event handler to disconnect from the database on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(user_router, prefix="/api")
app.include_router(package_router, prefix="/api")

# Additional code (such as endpoint definitions) goes here
