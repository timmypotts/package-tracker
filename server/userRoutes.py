from __main__ import app
from flask import Flask, request, jsonify, make_response
from api import Package, User, db
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# CREATE A USER
@app.route("/api/auth/register", methods=["POST"])
def createUser():
    data = request.get_json(force=True)
    print(data)
    print(data["username"])

    hashed_password = generate_password_hash(data["password"], method="sha256")

    new_user = User(public_id=str(uuid.uuid4()), username=data["username"], email=data["email"], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    token = jwt.encode({"public_id" : new_user.public_id, "username" : new_user.username}, app.config["SECRET_KEY"] )
    print("Sending response")
    return jsonify({"token" : token, "username" : new_user.username, "pub_id" : new_user.public_id})

# USER LOGIN
@app.route("/api/auth/login", methods=["POST"])
def userLogin():
    data = request.get_json(force=True)
    print(data)

    if not data:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm = "Login required!"'})

    user = User.query.filter_by(username=data["username"]).first()

# CHECK IF EXISTS
    if not user:
        return jsonify({"message" : "No user found"})

    if check_password_hash(user.password, data["password"]):
        token = jwt.encode({"public_id" : user.public_id, "username" : user.username}, app.config["SECRET_KEY"] )
        print("Sending response")
        return jsonify({"token" : token, "username" : data["username"], "pub_id" : user.public_id})

    return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm = "Login required!"'})