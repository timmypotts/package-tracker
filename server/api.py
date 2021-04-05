from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)

# SQLAlchemy config
app.config.from_object(os.evviron[APP_SETTINGS])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



# Package Put Args
package_put_args = reqparse.RequestParser()
package_put_args.add_argument("name", type=str, help="Please include a name for the package", required=True)
package_put_args.add_argument("courier", type=str, help="Please include the courier of the package", required=True)
package_put_args.add_argument("tracking", type=str, help="Please include the tracking number", required=True)
package_put_args.add_argument("user", type=int, help="Please include the user who has ordered the package", required=True)



# Serialize models
package_fields = {
    "id" : fields.Integer,
    "name" : fields.String,
    "courier" : fields.String,
    "tracking" : fields.String,
    "user" : fields.Integer,
    "shipped" : fields.Boolean,
    "shipdate" : fields.DateTime,
    "delivered" : fields.Boolean
}

user_fields = {
    "id" : fields.Integer,
    "name" : fields.String

}

# Package Routes
class Package(Resource):

# get packages for user
    @marshal_with(package_fields)
    def get(self, user_id):
        result = VideoModel.query.filter_by(user=user_id).all()
        if not result:
            abort(404, message="It does not look like you have any packages")
        return result

# create package
    @marshal_with(package_fields)
    def put(self, package_id):
        args = package_put_args.parse_args()
        result = PackageModel.query.filter_by(id=package_id).first()
        if result:
            abort(409, message="Package with that ID already exists")

        package = PackageModel(id=package_id, name=args["name"], tracking=args["tracking"], courier=args["courier"], user=args["user"])
        db.session.add(package)
        db.session.commit()
        return package, 201


api.add_resource(Package, "/package/")






if __name__ == "__main__":
    app.run(debug=True) # true only if dev environment