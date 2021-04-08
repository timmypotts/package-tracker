from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

app = Flask(__name__)
CORS(app)


# SQLAlchemy config ========================================================
#Token key to access enconding
app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tim:42bUgfish42!@localhost/packagedb"
db = SQLAlchemy(app)


# ========== DATABASE TABLES ===============================================
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    courier = db.Column(db.String(50), nullable=False)
    tracking = db.Column(db.String(120), unique=True, nullable=False)
    user = db.Column(db.Integer, nullable=False)
    shipped = db.Column(db.Boolean)
    shipdate = db.Column(db.DateTime, nullable=True)
    delivered =  db.Column(db.Boolean)
    deliverdate = db.Column(db.DateTime)

    def __repr__(self):
        return f"Package(name = {name}, tracking = {tracking}, courier = {courier}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)


# ========================== ROUTES ========================================
@app.route("/api/packages", methods=["GET"])
def getPackages():
    return ''

@app.route("/api/packages/<user_id>", methods=["GET"])
def getUserPackages():
    return ''


# CREATE A USER
@app.route("/api/auth/register", methods=["POST"])
def createUser():
    data = request.get_json(force=True)
    print("TESTING ==================================================")
    print(data)
    print(data["username"])

    hashed_password = generate_password_hash(data["password"], method="sha256")

    new_user = User(public_id=str(uuid.uuid4()), username=data["username"], email=data["email"], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message" : "new user created"})

# USER LOGIN
@app.route("/api/auth/login")
def userLogin():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm = "Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

# CHECK IF EXISTS
    if not user:
        return jsonify({"message" : "No user found"})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({"public_id" : user.public_id, "username" : user.username}, app.config["SECRET_KEY"] )

        return jsonify({"token" : token.decode("UTF-8")})

    make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm = "Login required!"'})


# PROMOTE USER TO ADMIN
@app.route("/api/user/<user_id>", methods=["PUT"])
def promoteUser():
    return ''

# DELETE USER
@app.route("/api/user/<user_id>", methods=["DELETE"])
def deleteUser():
    return ''





if __name__ == "__main__":
    app.run(debug=True) # true only if dev environment