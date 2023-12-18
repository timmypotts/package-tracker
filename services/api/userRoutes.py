from api import app
from flask import Flask, request, jsonify, make_response
from api import Package, User, db
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError


# CREATE A USER
@app.route("/api/auth/register", methods=["POST"])
def createUser():
    print("HIT!")
    data = request.get_json(force=True)

    hashed_password = generate_password_hash(data["password"], method="sha256")

    try:
        new_user = User(public_id=str(uuid.uuid4()), username=data["username"], email=data["email"], password=hashed_password, admin=False)
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return make_response("User already exists", 409)

    token = jwt.encode({"public_id" : new_user.public_id, "username" : new_user.username}, app.config["SECRET_KEY"] )
    print("Sending response")
    return jsonify({"token" : token, "username" : new_user.username, "pub_id" : new_user.public_id})

@app.route('/api/auth/register', methods=['OPTIONS'])
def handle_options():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
    response.headers.add('Access-Control-Max-Age', '1728000')
    return response



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
        return make_response("User does not exist", 404)

    if check_password_hash(user.password, data["password"]):
        token = jwt.encode({"public_id" : user.public_id, "username" : user.username}, app.config["SECRET_KEY"] )
        print("Sending response")
        return jsonify({"token" : token, "username" : data["username"], "pub_id" : user.public_id})

    return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm = "Login required!"'})