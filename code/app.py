from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.book import Book, BookList
from resources.store import Store, StoreList
from db import db
import os
import urllib.request, json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'nrohit'
api = Api(app)

@app.before_first_request #& This is the decorator that will affect the method below it
def create_tables():
    db.create_all() #& This will create all the Tables that have been imported into this app.py file. So, make sure you import everything properly.

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Book, '/book/<string:isbn>')
api.add_resource(BookList, '/books')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=8000, debug=True)