import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


# User class has been moved to models package folder because technically it is used to create models and interact with Databases
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This Field cannot be left Blank!"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This Field cannot be left Blank!"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]): # If this value is not None
            return {"message": "A User with that Username already exists"}, 400 # By putting this if condition here, we are not running any connection or cursor code if there is new user being created with an existing username
        user = UserModel(**data) # Same as UserModel(data["username"], data["password"])
        user.save_to_db()
        return {"message": "User Created Successfully."}, 201