from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from track import fedexTrack, uspsTrack, upsTrack
import requests
from packageSort import packageSort

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# SQLAlchemy config ========================================================
#Token key to access enconding
app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tim:42bUgfish42!@localhost:5432/packagedb"
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)


# ========== DATABASE TABLES ===============================================
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey("user.public_id"), nullable=False,)
    item = db.Column(db.String(120), nullable=False)
    courier = db.Column(db.String(50), nullable=False)
    tracking = db.Column(db.String(120), unique=True, nullable=False)
    statuscode = db.Column(db.String(10))
    carrierstatus = db.Column(db.String(120))
    status = db.Column(db.String(60), nullable=True)
    shipdate = db.Column(db.DateTime, nullable=True)
    deliverdate = db.Column(db.DateTime)
    exceptiondescription = db.Column(db.String(120))
    expected = db.Column(db.DateTime) 

    def __repr__(self):
        return f"Package(item = {self.item}, tracking = {self.tracking}, courier = {self.courier}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)


# ========================== ROUTES ========================================

# GET PACKAGES 
@app.route("/api/packages", methods=["GET"])
def getPackages():
    return ''

# GET PACKAGES FOR USER
@app.route("/api/packages/<public_id>", methods=["GET"])
def getUserPackages(public_id):

    packages = Package.query.filter_by(user=public_id).all()

    if not packages:
        return jsonify({"message" : "no packages found"})

    raw = []

    for package in packages:
        package_data = {}
        package_data["id"] = package.id
        package_data["user"] = package.user
        package_data["item"] = package.item
        package_data["courier"] = package.courier
        package_data["tracking"] = package.tracking
        package_data["status"] = package.status
        package_data["shipdate"] = package.shipdate
        package_data["deliverdate"] = package.deliverdate
        package_data["expected"] = package.expected
        package_data["statuscode"] = package.statuscode
        package_data["carrierstatus"] = package.carrierstatus
        package_data["exceptiondescription"] = package.exceptiondescription
        raw.append(package_data)
    print(raw)
    output = packageSort(raw)

    

    return jsonify({"packages" : output})


    print(packages)

    return jsonify({"packages" : packages}) 

@app.route("/api/packages/", methods=["POST"])

def postPackage():
    data = request.get_json(force=True)
    print(data)
    if data["courier"] == "USPS":
        res = uspsTrack(data["tracking"])
        print(res)
        orderStatus = res["status_description"]
        expectedDelivery = res["estimated_delivery_date"]
        shipDate = res["ship_date"]
        deliveryDate = res["actual_delivery_date"]
        statusCode = res["status_code"]
        carrierStatus = res["carrier_status_description"]
        exceptionDescription = res["exception_description"]
    elif data["courier"] == "FedEx":
        res = fedexTrack(data["tracking"])
        orderStatus = res["status_description"]
        expectedDelivery = res["estimated_delivery_date"]
        shipDate = res["ship_date"]
        deliveryDate = res["actual_delivery_date"]
        statusCode = res["status_code"]
        carrierStatus = res["carrier_status_description"]
        exceptionDescription = res["exception_description"]
    elif data["courier"] == "UPS":
        res = upsTrack(data["tracking"])
        orderStatus = res["status_description"]
        expectedDelivery = res["estimated_delivery_date"]
        shipDate = res["ship_date"]
        deliveryDate = res["actual_delivery_date"]
        statusCode = res["status_code"]
        carrierStatus = res["carrier_status_description"]
        exceptionDescription = res["exception_description"]


    new_package = Package(user = data["pubId"], item = data["item"], courier = data["courier"], tracking = data["tracking"], status = orderStatus, shipdate = shipDate, deliverdate = deliveryDate, expected = expectedDelivery, statuscode = statusCode, carrierstatus = carrierStatus, exceptiondescription = exceptionDescription)


    db.session.add(new_package)
    db.session.commit()

    return jsonify({"message" : "added package"})

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

    return jsonify({"message" : "new user created"})

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