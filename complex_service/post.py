from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import haversine as hs

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user_info'
 
    # user_id = db.Column(db.String(13), primary_key=True)
    # name = db.Column(db.String(128))
    # address = db.Column(db.String(128), nullable=False)
    # latitude = db.Column(db.Float(precision=4), nullable=False)
    # longitude = db.Column(db.Float(precision=4), nullable=False)
    # dietary_type = db.Column(db.VARCHAR(64))
    # travel_appetite = db.Column(db.Integer)
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
        return {"user_id": self.user_id, "name": self.name, "address": self.address, "latitude": self.latitude, "longitude": self.longitude, "dietary_type": self.dietary_type, "travel_appetite": self.travel_appetite}
    
    def get_distance(self, Location):
        '''
        input: Location

        syntax: self.get_distance(Location)

        output: Location JSON if Location within self.travel_appetite else Failure message
        '''
        distance = hs.haversine((self.latitude,self.longitude),(Location.latitude, Location.longitude))
        if distance <= self.travel_appetite:
            return {"post_id": Location.post_id, "address": Location.address, "latitude": Location.latitude, "longitude": Location.longitude}
        else:
            return "Method failed because distance larger than travel_appetite"

class Location:
    def __init__(self, post_id, address, latitude, longitude):
        self.post_id = post_id
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

@app.route("/post")
def get_all():
    user_list = User.query.all()
    if len(user_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "posts": [user.json() for user in user_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no such users."
        }
    ), 404

 
@app.route("/post/<string:user_id>")
def find_by_user_id(user_id):
    user = User.query.filter_by(user_id=user_id).first()

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
            "message": "Post not found."
        }
    ), 404

@app.route("/post/<string:user_id>", methods=['POST'])
def create_book(user_id):
    if (User.query.filter_by(user_id=user_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "user_id": user_id
                },
                "message": "User already exists."
            }
        ), 400
 
    data = request.get_json()
    user = User(user_id, **data)
 
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user_id": user_id
                },
                "message": "An error occurred creating the user."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201

@app.route("/post/check/<string:post_id>", methods=['POST'])
def create_post(post_id):
    # if (User.query.filter_by(user_id=user_id).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "data": {
    #                 "user_id": user_id
    #             },
    #             "message": "User already exists."
    #         }
    #     ), 400
 
    data = request.get_json()
    user = Location(post_id, **data)
 
    try:
        # db.session.add(user)
        # db.session.commit()
        return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user_id": user_id
                },
                "message": "An error occurred creating the user."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)