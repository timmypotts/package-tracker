from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON


db = SQLAlchemy()
# ========== DATABASE TABLES ===============================================
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey("user.public_id"), nullable=False,)
    item = db.Column(db.String(120), nullable=False)
    courier = db.Column(db.String(50), nullable=False)
    tracking = db.Column(db.String(120), unique=True, nullable=False)
    statuscode = db.Column(db.String(10))
    carrierstatus = db.Column(db.Text)
    status = db.Column(db.String(60), nullable=True)
    shipdate = db.Column(db.DateTime, nullable=True)
    deliverdate = db.Column(db.DateTime)
    exceptiondescription = db.Column(db.String(120))
    expected = db.Column(db.DateTime) 

    def __repr__(self):
        return f"Package(item = {self.item}, tracking = {self.tracking}, courier = {self.courier}"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f"Users( username = {username}"


