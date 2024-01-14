from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, database, get_db
from app.routes.package_routes import package_router
from app.routes.user_routes import user_router

import time
import logging
import os

# Initialize FastAPI app
app = FastAPI()

# # CORS settings
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Event handler to create tables and connect to the database on startup
@app.on_event("startup")
async def startup():
    # Create tables
    Base.metadata.create_all(bind=engine)
    print("STARTING UP")
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        raise ValueError("Secret key not found")
    # Connect to the database
    await database.connect()

# Event handler to disconnect from the database on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(user_router, prefix="/api", dependencies=[Depends(get_db)])
app.include_router(package_router, prefix="/api", dependencies=[Depends(get_db)])


@app.get("/healthcheck")
async def healthcheck():
    print("DING")
    return {"status": "healthy"}

# middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logging.info(f"{request.method} {request.url} completed in {formatted_process_time}ms")
    return response