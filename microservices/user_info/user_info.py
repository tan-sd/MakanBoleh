from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

import os, sys
import haversine as hs
import requests
# from invokes import invoke_http

# request.args for get param
# request.form for post param
# request.values for the abv 2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class user_info(db.Model):
    __tablename__ = 'user_info'

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
        
@app.route('/')
def nothing():
    return render_template('search_query.html')
    
# to diplay profile of all users
@app.route("/profile")
def getUserInfo():

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

# search user by username
@app.route("/search/user", methods=['POST'])
def find_user():
    name = request.form.get('name')
    user = user_info.query.filter_by(name=name).first()
    if name and user:
        return render_template('search_user.html', name=name, data=user)
    else:
        return 'Please go back and enter a valid name...', 400  # 400 Bad Request
    

# to display user info
@app.route("/profile/<int:user_id>", methods=['GET'])
def find_by_user_id(user_id):

    # shd display user profile
    user = user_info.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404

# just to update user profile, according to the data receieved from website
@app.route("/profile/<string:name>/update", methods=['PUT'])
def update_by_user_id(name):
    
    user = user_info.query.filter_by(name=name).first()
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

# to create user info when user first created account
@app.route("/createprofile/<string:name>", methods=['POST'])
def create_user(name):

    # focus on name of boxes not id
    # name = request.form.get('name1')
    # dietary = request.form.get('dietary')
    # address = request.form.get('address')
    # travel = request.form.get('travel')

    # if user dont exist, ill create user
    # if name:
    #     return render_template('create_user.html', name=name, travel=travel)
    # else:
    #     return 'Please go back and enter your name...', 400  # 400 Bad Request
    

    if (user_info.query.filter_by(name=name).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "name": name
                },
                "message": "user exists already"
            }
        ), 400
    # 400 BAD request

    data = request.get_json()
    user = user_info(name, **data)
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
                    "name": name
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
