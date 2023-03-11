#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

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
@app.route("/")
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

# CREATE A POST (IN PROGRESS)
@app.route("/createpost/<int:post_id>", methods=['POST'])
def create_post(post_id):

    #check if post is already in the db
    if(food_db.query.filter_by(post_id=post_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "post_id": post_id
                },
                "message": "post already exists"
            }
        ), 400
    #else, carry on making the post
    
    data = request.get_json()
    post = food_db(post_id,**data)

    try:
        db.session.add(post)
        db.session.commit()
    except:
        return jsonify(
            {
                "code":500,
                "data":{
                    "post_id":post_id
                },
                "message": "we got an error bois"
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "data": post.json(),
            "message": "post created successfully"
        }
    ), 201

# DELETE A POST (IN PROGRESS)
# @app.route("/deletepost/<int:post_id>", methods=['DELETE'])
# @app.route("/order/<string:order_id>")
# def find_by_order_id(order_id):
#     order = Order.query.filter_by(order_id=order_id).first()
#     if order:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": order.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "order_id": order_id
#             },
#             "message": "Order not found."
#         }
#     ), 404


# @app.route("/order", methods=['POST'])
# def create_order():
#     customer_id = request.json.get('customer_id', None)
#     order = Order(customer_id=customer_id, status='NEW')

#     cart_item = request.json.get('cart_item')
#     for item in cart_item:
#         order.order_item.append(Order_Item(
#             book_id=item['book_id'], quantity=item['quantity']))

#     try:
#         db.session.add(order)
#         db.session.commit()
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "message": "An error occurred while creating the order. " + str(e)
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": order.json()
#         }
#     ), 201


# @app.route("/order/<string:order_id>", methods=['PUT'])
# def update_order(order_id):
#     try:
#         order = Order.query.filter_by(order_id=order_id).first()
#         if not order:
#             return jsonify(
#                 {
#                     "code": 404,
#                     "data": {
#                         "order_id": order_id
#                     },
#                     "message": "Order not found."
#                 }
#             ), 404

#         # update status
#         data = request.get_json()
#         if data['status']:
#             order.status = data['status']
#             db.session.commit()
#             return jsonify(
#                 {
#                     "code": 200,
#                     "data": order.json()
#                 }
#             ), 200
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "order_id": order_id
#                 },
#                 "message": "An error occurred while updating the order. " + str(e)
#             }
#         ), 500


if __name__ == '__main__':
    app.run(port=5678, debug=True)
