from flask import Blueprint, request, jsonify, make_response
from models import Package, Users, db
from packageSort import packageSort
from track import track
from dotenv import load_dotenv

package_blueprint = Blueprint('package_blueprint', __name__)

# GET PACKAGES FOR USER
@package_blueprint.route("/api/packages/<public_id>", methods=["GET"])
def getUserPackages(public_id):

    packages = Package.query.filter_by(user=public_id).all()
    
    if not packages:
        return make_response({"message" : "no packages found"})

    for package in packages:
        if package.statuscode == "DE":
            pass
        else:
            res = track(package.tracking, package.courier) 
            package.status = res["status_description"]
            package.expected = res["estimated_delivery_date"]
            package.shipdate = res["ship_date"]
            package.deliverdate = res["actual_delivery_date"]
            package.statuscode = res["status_code"]
            package.carrierstatus = res["carrier_status_description"]
            package.exceptiondescription = res["exception_description"]
            db.session.commit()

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

@package_blueprint.route("/api/packages/", methods=["POST"])

def postPackage():
    data = request.get_json(force=True)
    print(data)

    res = track(data["tracking"], data["courier"])
    print(res)
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

# DELETE PACKAGE
@package_blueprint.route("/api/packages/<package_id>", methods=["DELETE"])
def deletePackage(package_id):
    db.session.query(Package).filter(Package.id==package_id).delete()
    db.session.commit()
    return make_response("Package Deleted", 200)
