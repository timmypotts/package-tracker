import userRoutes
import packageRoutes
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import sys
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})
port = 3080
if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("You said port is : {} ".format(port))

#  ========================== SQLAlchemy config ==========================
# Token key to access enconding
app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_API_URL")
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)


# ========== DATABASE TABLES ===============================================
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey(
        "user.public_id"), nullable=False,)
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)


# ========================== ROUTES ========================================

# AFTER REQUEST HOOK

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)  # true only if dev environment
