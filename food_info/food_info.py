#!/usr/bin/env python3
# import relevant dependencies
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# INITIALISING APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

# DECLARING DATABASE CLASS
class food_db(db.Model):
    __tablename__ = 'food_info'

    post_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    post_name = db.Column(db.VARCHAR(64), nullable=False)
    latitude =  db.Column(db.Float(precision=6), nullable=False)
    longitude = db.Column(db.Float(precision=6), nullable=False)
    description = db.Column(db.VARCHAR(300))
    allergens = db.Column(db.VARCHAR(64))
    is_available = db.Column(db.Integer(), nullable=False)

    def __init__(self, post_id, creator_id, post_name, latitude, longitude, description, allergens, is_available):
        self.post_id = post_id
        self.creator_id = creator_id
        self.post_name = post_name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.allergens = allergens
        self.is_available = is_available

    def json(self):
        post = {
            'post_id': self.post_id,
            'creator_id': self.creator_id,
            'post_name': self.post_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'description': self.description,
            'allergens' : self.allergens,
            'is_available' : self.is_available 
        }
        return post

# SHOW ALL POSTS
@app.route("/all")
def test():
    food_list = food_db.query.all()
    if len(food_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "food": [food.json() for food in food_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no food."
        }
    ), 404

# RETRIEVE SPECIFIC POST
@app.route("/search/<string:post_id>")
def find_post(post_id):
    post = food_db.query.filter_by(post_id=post_id).first()

    #if post exists, return post json
    if post:
        return jsonify(
            {
                "code": 200,
                "data": post.json()
            }
        )
    
    #else, return error message
    return jsonify(
        {
            "code": 404,
            "message": "Book not found."
        }
    ), 404

# CREATE A POST
@app.route("/create/<int:post_id>", methods=['POST'])
def create_post(post_id):

    #check if post is already in the db
    if(food_db.query.filter_by(post_id=post_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "post_id": post_id
                },
                "message": "Post already exists."
            }
        ), 400
    
    #else, carry on making the post
    data = request.get_json()
    post = food_db(**data)

    #attempt to add post into db
    try:
        db.session.add(post)
        db.session.commit()

    #if post cannot be made, return error message
    except:
        return jsonify(
            {
                "code":500,
                "data":{
                    "post_id":post_id
                },
                "message": "An error occurred when creating a post. Please check if all fields meet the constraints of the database."
            }
        ), 500
    
    #if no errors, return success message
    return jsonify(
        {
            "code": 201,
            "data": post.json(),
            "message": "Post created successfully."
        }
    ), 201

# DELETE A POST
@app.route("/delete/<int:post_id>", methods=['DELETE'])
def delete(post_id):
    post = food_db.query.filter_by(post_id=post_id).first()

    #check if post exists
    if post:

        #attempt to delete post from db
        try:
            db.session.delete(post)
            db.session.commit()

        #if post cannot be deleted, return error message
        except:
             return jsonify(
            {
                "code": 500,
                "data": {
                    "post_id": post_id
                },
                "message": "An error occurred when deleting the post. Please check if the post still exists."
            }
        ), 500

        #if no errors, return success message
        return jsonify(
            {
                "code": 201,
                "data": post.json(),
                "message":"Post successfully deleted."
            }
        ), 201
        
    #else, notify that the post doesn't exist
    return jsonify(
        {
            "code": 404,
            "data": {
                "post_id": post_id
            },
            "message": "Post not found."
        }
    )

# EDIT A POST (SEND A JSON WITH UPDATED PARTICULARS)
@app.route("/edit/<int:post_id>", methods=['PUT'])
def edit(post_id):
    
    post = food_db.query.filter_by(post_id=post_id).first()

    #check if post exists
    if post:

        #attempt to edit
        try:
            data = request.get_json()

            #update fields
            post.post_name = data['post_name']
            post.latitude = data['latitude'] 
            post.longitude = data['longitude'] 
            post.description = data['description']  
            post.allergens = data['allergens'] 
            post.is_available = data['is_available'] 

            #commit changes
            db.session.commit()

            #if no errors, return success message
            return jsonify(
                {
                    "code": 200,
                    "data": post.json(),
                    "message": "Post edited successfully. See above for updated post details."
                }
            ), 200
        
        #if post cannot be edited, return error message
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "post_id": post_id
                    },
                    "message": "An error occurred while updating the post. " + str(e)
                }
            ), 500

    #else, notify that post does not exist
    return jsonify(
        {
            "code": 404,
            "data": {
                "post_id": post_id
            },
            "message": "Post not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(port=1112, debug=True)
