from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy import Integer
from models.book import BookModel
import json


class Book(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "stock",
        type=int,
        required=True,
        help="Please Mention the Number of Books available in Stock"
    ) #* If you have a HTML Form, you can use this RequestParser to go through the Form Fields

    parser.add_argument(
        "title",
        type=str,
        required=True,
        help="Title Field cannot be Empty"
    )

    parser.add_argument(
        "subtitle",
        type=str,
        required=True,
        help="Title Field cannot be Empty"
    )

    parser.add_argument(
        "npages",
        type=int,
        required=True,
        help="Please Mention the Number of Pages in the Book"
    )

    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every Book Needs a Store ID"
    )

    #^ NOTE     GET METHOD
    @jwt_required()
    def get(self, isbn):
        book = BookModel.find_by_google_isbn(isbn)
        if book:
            return json.dumps(book)
        return {"message": "Book Not Found"}, 404 # else
    

    #^ NOTE     POST METHOD
    def post(self, isbn):
        if BookModel.find_by_isbn(isbn):
            return {"message": "An book with isbn '{}' already exists".format(isbn)}, 400

        data = Book.parser.parse_args()
        book = BookModel(data["stock"], isbn, data["title"], data["subtitle"], data["npages"], data["store_id"]) # **data is same as , , ...

        try:
            book.save_to_db()
        except:
            return {"message": "An Error Occured while inserting the New Book"}, 500 # Internal Server Error
        return book.json(), 201


    #^ NOTE     DELETE METHOD
    def delete(self, isbn):
        book = BookModel.find_by_isbn(isbn)
        if book:
            book.delete_from_db()
            return {"message": "Book Deleted"}
        else:
            return {"message": "Book Not Found"}, 404
           

    #^ NOTE     PUT METHOD
    def put(self, isbn): #* For both Posting and Updating an Book
        data = Book.parser.parse_args()
        book = BookModel.find_by_isbn(isbn)
        if book is None:
            book = BookModel(data["stock"], isbn, data["title"], data["subtitle"], data["npages"], data["store_id"])
        else:
            book.stock = data["stock"]
            book.title = data["title"]
            book.subtitle = data["subtitle"]
            book.npages = data["npages"]
        book.save_to_db()
        return book.json()



class BookList(Resource):
    def get(self):
        return {"books": [book.json() for book in BookModel.query.all()]}