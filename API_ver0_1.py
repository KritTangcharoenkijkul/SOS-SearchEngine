#use Flask-RESTful, more cleaner
'''
GUIDE

Get: obtain information from other requests
POST: create new resource
PUT: update new resource
'''
from flask import Flask, request
from flask_restful import Resource, Api

import csv
import json

    
app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        f = open('CommonFrame.json',)
        data = json.load(f)
        return {'All Reviews': data}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201


class Reviews(Resource):
    def get(self):
        f = open('ReviewFrame.json',)
        data = json.load(f)
        return {'Reviews': data}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

class WishList(Resource):
    def get(self, name):
        f = open('WishlistFrame.json',)
        data = json.load(f)
        return {'Wishlist': data}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

api.add_resource(Home, '/')
api.add_resource(Reviews, '/reviews')
api.add_resource(WishList, '/wishlist/<int:name>')

if __name__ == '__main__':
   app.run(debug=True)