#use Flask-RESTful, more cleaner
'''
GUIDE

Get: obtain information from other requests
POST: create new resource
PUT: update new resource
'''
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {'about':'Home'}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

class ReviewByuser(Resource):
    def get(self):
        return {'about':'review by user'}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

class Reviews(Resource):
    def get(self):
        return {'about':'average review for each item'}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

class WishList(Resource):
    def get(self, name):
        return {'result': name}

    def post(self):
        some_json = request.get_json()
        return {'you sent':some_json}, 201

api.add_resource(Home, '/')
api.add_resource(ReviewByuser, '/review-by-user')
api.add_resource(Reviews, '/reviews')
api.add_resource(WishList, '/wishlist/<int:name>')

if __name__ == '__main__':
   app.run(debug=True)