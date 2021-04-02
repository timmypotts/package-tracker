from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

from models import db

app = Flask(__name__)
api = Api(app)




# Package Put Args


# Package Route
class Package(Resource):
    def put(self, package_id):
        args = package_put_args.parse_args()
        result = PackageModel.query.filter_by(id=package_id).first()
        if result:
            abort(409, message="Package with that ID already exists")

        package = PackageModel(id=package_id, name=args["name"], tracking=args["tracking"], courier=args["courier"], user=args["user"])






if __name__ == "__main__":
    app.run(debug=True) # true only if dev environment