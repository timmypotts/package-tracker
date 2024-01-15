from fastapi import HTTPException, Depends, APIRouter, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.database import get_db
from app.models import User
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Pydantic models for request bodies
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

user_router = APIRouter()

# Route for creating a user
@user_router.post("/auth/register", tags=["User"])
async def create_user(user_data: UserCreate, response: Response, db_session: Session = Depends(get_db)):
    # Check if the request body is valid
    if user_data.username is None or user_data.password is None:
        raise HTTPException(status_code=400, detail="Username and password are required")

    # Check if the user already exists
    existing_user = db_session.query(User).filter((User.username == user_data.username) | (User.email == user_data.email)).first()
    if existing_user.username == user_data.username:
        raise HTTPException(status_code=400, detail="username already in use")
    if existing_user.email == user_data.email:
        raise HTTPException(status_code=400, detail="email already in use")

    hashed_password = generate_password_hash(user_data.password, method='pbkdf2:sha256')
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
        raise HTTPException(status_code=500, detail="cannot create user")
    
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        raise ValueError("Secret key not found")
    # Create a token for the new user
    token = jwt.encode(
        {"public_id": new_user.public_id, "username": new_user.username},
        os.environ.get('SECRET_KEY'),  # Use the secret key from environment variables
        algorithm="HS256"
    )

    # write jwt token to response header
    response.headers["Authorization"] = f"Bearer {token}"
    return {"username": new_user.username, "public_id": new_user.public_id}

# Route for logging in a user
@user_router.post("/auth/login", tags=["User"])
async def user_login(login_data: UserLogin, response: Response, db_session: Session = Depends(get_db)):
    user = db_session.query(User).filter(User.username == login_data.username).first()
    if user and check_password_hash(user.password, login_data.password):
        token = jwt.encode(
            {"public_id": user.public_id, "username": user.username},
            os.environ.get('SECRET_KEY'),  # Use the secret key from environment variables
            algorithm="HS256"
        )

        # write jwt token to response header
        response.headers["Authorization"] = f"Bearer {token}"
        return {"username": user.username, "public_id": user.public_id}
    else:
        raise HTTPException(
            status_code=401,
            detail='Could not verify credentials',
            headers={"WWW-Authenticate": 'Bearer'},
        )


