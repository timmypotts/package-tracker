from fastapi import HTTPException, Depends, Body, APIRouter
from app.models import User, db
from sqlalchemy.orm import Session
from database import get_db
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

user_router = APIRouter()

# # Enable CORS for all routes
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# CREATE A USER
@user_router.post("/api/auth/register", tags=["User"])
async def create_user(data: dict = Body(...), db: Session = Depends(get_db)):
    hashed_password = generate_password_hash(data["password"], method="sha256")

    try:
        new_user = User(
            public_id=str(uuid.uuid4()),
            username=data["username"],
            email=data["email"],
            password=hashed_password,
            admin=False,
        )
        db.add(new_user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="User already exists")

    token = jwt.encode(
        {"public_id": new_user.public_id, "username": new_user.username},
        "your_secret_key",  # Replace with your actual secret key
    )
    return {"token": token, "username": new_user.username, "pub_id": new_user.public_id}

# USER LOGIN
@user_router.post("/api/auth/login", tags=["User"])
async def user_login(data: dict = Body(...)):
    if not data:
        raise HTTPException(
            status_code=401, detail='Could not verify', headers={"WWW-Authenticate": 'Basic realm="Login required!"'}
        )

    user = db.query(User).filter_by(username=data["username"]).first()

    # CHECK IF EXISTS
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    if check_password_hash(user.password, data["password"]):
        token = jwt.encode(
            {"public_id": user.public_id, "username": user.username},
            "your_secret_key",  # Replace with your actual secret key
        )
        return {"token": token, "username": data["username"], "pub_id": user.public_id}

    raise HTTPException(
        status_code=401,
        detail='Could not verify',
        headers={"WWW-Authenticate": 'Basic realm="Login required!"'},
    )