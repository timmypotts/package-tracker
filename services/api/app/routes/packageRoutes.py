from fastapi import FastAPI, Depends, HTTPException, Body, APIRouter
from sqlalchemy.orm import Session
from services.api.app.models import Package, db
from services.api.app.packageSort import packageSort
from services.api.app.outgoing.track import track

package_routes = APIRouter()

# Dependency to get the database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# GET PACKAGES FOR USER
@package_routes.get("/api/packages/{public_id}", tags=["Packages"])
def get_user_packages(public_id: str, db: Session = Depends(get_db)) -> dict:
    packages = db.query(Package).filter_by(user=public_id).all()

    if not packages:
        raise HTTPException(status_code=404, detail="No packages found")

    for package in packages:
        # avoid making API call if package is delivered
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
            package.lat, package.lon = get_recent_lat_lon(res["events"])
            db.commit()

    raw = []

    for package in packages:
        package_data = {
            "id": package.id,
            "user": package.user,
            "item": package.item,
            "courier": package.courier,
            "tracking": package.tracking,
            "status": package.status,
            "shipdate": package.shipdate,
            "deliverdate": package.deliverdate,
            "expected": package.expected,
            "statuscode": package.statuscode,
            "carrierstatus": package.carrierstatus,
            "exceptiondescription": package.exceptiondescription,
            "lat": package.lat,
            "lon": package.lon,
        }
        raw.append(package_data)

    output = packageSort(raw)

    return {"packages": output}


# POST PACKAGE
@package_routes.post("/api/packages/", tags=['Packages'])
def post_package(data: dict = Body(...)):

    try:
        res = track(data["tracking"], data["courier"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to track package: {str(e)}")

    order_status = res["status_description"]
    expected_delivery = res["estimated_delivery_date"]
    ship_date = res["ship_date"]
    delivery_date = res["actual_delivery_date"]
    status_code = res["status_code"]
    carrier_status = res["carrier_status_description"]
    exception_description = res["exception_description"]

    new_package = Package(
        user=data["pubId"],
        item=data["item"],
        courier=data["courier"],
        tracking=data["tracking"],
        status=order_status,
        shipdate=ship_date,
        deliverdate=delivery_date,
        expected=expected_delivery,
        statuscode=status_code,
        carrierstatus=carrier_status,
        exceptiondescription=exception_description
    )

    db.add(new_package)
    db.commit()

    return {"message": "Added package"}

# DELETE PACKAGE
@package_routes.delete("/api/packages/{package_id}", tags=['Packages'])
def delete_package(package_id: str, db: Session = Depends(get_db)):

    try:
        db.query(Package).filter(Package.id == package_id).delete()
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete package: {str(e)}")

    return {"message": "Package Deleted"}


def get_recent_lat_lon(events):
    for event in events:
        if event['latitude'] is not None and event['longitude'] is not None:
            return event['latitude'], event['longitude']
    return None, None