from app import db
from sqlalchemy.dialects.postgresql import JSON

class PackageModel(db.Model):
    __tablename__ = 'Packages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    tracking = db.Column(db.String(120), unique=True, nullable=False)
    courier = db.Column(db.String(50), nullable=False)
    user = db.Column(db.Integer, nullable=False)
    shipdate = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"Package(name = {name}, tracking = {tracking}, courier = {courier}"

class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"User( username = {username}"

