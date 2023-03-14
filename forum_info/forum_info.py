#!/usr/bin/env python3
# import relevant dependencies
import os
import haversine as hs
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# INITIALISING APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/forum_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

# DECLARING DATABASE CLASS
class forum_db(db.Model):
    __tablename__ = 'forum_table'
    forum_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False)
    title =  db.Column(db.VARCHAR(60), nullable=False)
    description = db.Column(db.VARCHAR(1000))
    datetime = db.Column(db.VARCHAR(19), nullable=False)
    

    def __init__(self, forum_id, username, title, description,datetime):
        self.forum_id = forum_id
        self.username = username
        self.title = title
        self.description = description
        self.datetime = datetime


    def json(self):
        forum = {
            'forum_id': self.forum_id,
            'username': self.username,
            'forum_title': self.forum_title,
            'description': self.description,
            'datetime': self.datetime
        }
        return forum


@app.route("/")
def test():
    return 'welcome to smu'

# SHOW ALL POSTS
@app.route("/all")
def view_all():
    forum_list = forum_db.query.all()
    if len(forum_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "forum": [forum.json() for forum in forum_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no forums."
        }
    ), 404

# RETRIEVE SPECIFIC POST
@app.route("/search/<string:post_id>")
def find_post(forum_id):
    post = forum_db.query.filter_by(forum_id=forum_id).first()

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
            "message": "Posts not found."
        }
    ), 404

# CREATE A POST
@app.route("/create/<int:post_id>", methods=['POST'])
def create_forum(forum_id):

    #check if forum post is already in the db
    if(forum_db.query.filter_by(forum_id=forum_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "forum_id": forum_id
                },
                "message": "Post already exists."
            }
        ), 400
    
    #else, carry on making the post
    data = request.get_json()
    post = forum_db(**data)

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
                    "forum_id":forum_id
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
def delete(forum_id):
    post = forum_db.query.filter_by(forum_id=forum_id).first()

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
                    "forum_id": forum_id
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
                "forum_id": forum_id
            },
            "message": "Post not found."
        }
    )

# EDIT A POST (SEND A JSON WITH UPDATED PARTICULARS)
@app.route("/edit/<int:post_id>", methods=['PUT'])
def edit(forum_id):
    
    post = forum_db.query.filter_by(forum_id=forum_id).first()

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
                        "forum_id": forum_id
                    },
                    "message": "An error occurred while updating the post. " + str(e)
                }
            ), 500
            
    #else, notify that post does not exist
    return jsonify(
        {
            "code": 404,
            "data": {
                "forum_id": forum_id
            },
            "message": "Post not found."
        }
    ), 404