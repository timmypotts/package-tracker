from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from app.models import User
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Pydantic models for request bodies
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

user_router = APIRouter()

# Route for creating a user
@user_router.post("/api/auth/register", tags=["User"])
async def create_user(user_data: UserCreate, db_session: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db_session.query(User).filter((User.username == user_data.username) | (User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already in use")

    hashed_password = generate_password_hash(user_data.password, method="sha256")
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        admin=False,
    )
    db_session.add(new_user)
    try:
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        raise HTTPException(status_code=409, detail="User already exists")
    
    # Create a token for the new user
    token = jwt.encode(
        {"public_id": new_user.public_id, "username": new_user.username},
        os.environ.get('SECRET_KEY'),  # Use the secret key from environment variables
        algorithm="HS256"
    )
    return {"token": token, "username": new_user.username, "public_id": new_user.public_id}

# Route for logging in a user
@user_router.post("/api/auth/login", tags=["User"])
async def user_login(login_data: UserLogin, db_session: Session = Depends(get_db)):
    user = db_session.query(User).filter(User.username == login_data.username).first()
    if user and check_password_hash(user.password, login_data.password):
        token = jwt.encode(
            {"public_id": user.public_id, "username": user.username},
            os.environ.get('SECRET_KEY'),  # Use the secret key from environment variables
            algorithm="HS256"
        )
        return {"token": token, "username": user.username, "public_id": user.public_id}
    else:
        raise HTTPException(
            status_code=401,
            detail='Could not verify credentials',
            headers={"WWW-Authenticate": 'Bearer'},
        )
