from db import db
import json
from urllib.request import urlopen
import json

class BookModel(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Integer)
    isbn = db.Column(db.Integer)
    title = db.Column(db.String(80))
    subtitle = db.Column(db.String(200))
    npages = db.Column(db.Integer)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, stock, isbn, title, subtitle, npages, store_id):
        self.stock = stock
        self.isbn = isbn
        self.title = title
        self.subtitle = subtitle
        self.npages = npages
        self.store_id = store_id

    def json(self):
        return {"stock": self.stock, "isbn": self.isbn, "title": self.title, "subtitle": self.subtitle, "npages": self.npages}

    def find_by_google_isbn(isbn):
        api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        resp = urlopen(api + isbn)
        book_data = json.load(resp)
        volume_info = book_data["items"][0]["volumeInfo"]
        json_object = json.dumps(volume_info, indent = 4)
        return json_object

    @classmethod
    def find_by_isbn(cls, isbn):
        return cls.query.filter_by(isbn=isbn).first() # SELECT * FROM books WHERE "title"=title LIMIT 1 --> Getting 1st Row

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()