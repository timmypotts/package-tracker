from app.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Integer, Text, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
import uuid

# ========== DATABASE TABLES ===============================================
class Package(Base):
    __tablename__ = 'packages'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user = Column(String(120), ForeignKey("users.public_id"), nullable=False,)
    item = Column(String(120), nullable=False)
    courier = Column(String(50), nullable=False)
    tracking = Column(String(120), unique=True, nullable=False)
    statuscode = Column(String(10))
    carrierstatus = Column(Text)
    status = Column(String(60), nullable=True)
    shipdate = Column(DateTime, nullable=True)
    deliverdate = Column(DateTime)
    exceptiondescription = Column(String(120))
    expected = Column(DateTime) 
    events = Column(JSON)
    lat = Column(Float)
    lon = Column(Float)

    def __repr__(self):
        return f"Package(item = {self.item}, tracking = {self.tracking}, courier = {self.courier}"

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    public_id = Column(String(50), unique=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False) 
    admin = Column(Boolean)

    def __repr__(self):
        return f"User( username = {self.username}"


