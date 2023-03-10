from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class user_info(db.Model):
    __tablename__ = 'user_info'
#user_ID (INT) (auto increment)
# Name (VARCHAR)
# Default_Address{
# Address (VARCHAR)
# Latitude (FLOAT)
# Longitude (FLOAT)}
# Dietary_Type (ARRAY)
# Travel_Appetite (VARCHAR)

# for ref if want to change the format in sqlworkbench
# https://stackoverflow.com/questions/17371639/how-to-store-arrays-in-mysql

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), nullable=False)
    # default_address = db.Column(db.ARRAY(Nested(MutableList.as_mutable(ARRAY(MutableDict.as_mutable(ARRAY(String)))))))
    address = db.Column(db.VARCHAR(64), nullable=False)
    latitude = db.Column(db.Float(precision=6), nullable=False)
    longitude = db.Column(db.Float(precision=6), nullable=False)
    dietary_type = db.Column(db.VARCHAR(64))
    travel_appetite = db.Column(db.VARCHAR(64))

    def __init__(self, user_id, name, address, latitude, longitude, dietary_type, travel_appetite):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.dietary_type = dietary_type
        self.travel_appetite = travel_appetite

    def json(self):
        return {"user_id": self.user_id, "name": self.name, "address": self.address, "latitude": self.latitude, "longitude":self.longitude, "travel_appetite": self.travel_appetite}

@app.route('/')
def nothing():
    return 'peekaboo!'

@app.route("/profile")
def getUserInfo():

    # retrieve all records
    all_user_info = user_info.query.all()
    if len(all_user_info):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "user": [info.json() for info in all_user_info]
                }
            }
        )
    # if HTTP status code not specified at the end, 
    # then 200 OK returned

    # the else comes here
    return jsonify(
        {
            "code": 404,
            "message": "No information to be displayed."
        }
    ), 404


@app.route("/profile/<int:user_id>", methods=['GET', 'PUT'])
def find_by_user_id(user_id):

    # shd oni hav one book returned and none if no match
    user = user_info.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404

@app.route("/createprofile/<int:user_id>", methods=['POST'])
def create_user(user_id):
    # thinking to create with the name insted of user_id cuz this dont make sense
    
    if (user_info.query.filter_by(user_id=user_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "user_id": user_id
                },
                "message": "user exists already"
            }
        ), 400
    # 400 BAD request

    data = request.get_json()
    user = user_info(user_id, **data)
    #  ** means allow arbitrary number of arguments to a function

    try:
        db.session.add(user)
        db.session.commit()
        # to commit the change

    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user_id": user_id
                },
                "message": "An error occurred creating user info."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=1111, debug=True)
