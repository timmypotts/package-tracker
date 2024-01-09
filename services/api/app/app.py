from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, database, get_db
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

# Event handler to create tables and connect to the database on startup
@app.on_event("startup")
async def startup():
    # Create tables
    Base.metadata.create_all(bind=engine)
    print("STARTING UP")
    # Connect to the database
    await database.connect()

# Event handler to disconnect from the database on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(user_router, prefix="/api", dependencies=[Depends(get_db)])
app.include_router(package_router, prefix="/api", dependencies=[Depends(get_db)])

# Additional code (such as endpoint definitions) goes here
