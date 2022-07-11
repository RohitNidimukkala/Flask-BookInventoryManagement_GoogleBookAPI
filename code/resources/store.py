from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    #^ NOTE     GET METHOD
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store Not Found"}, 404 # else
    

    #^ NOTE     POST METHOD
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "A Store with name '{}' already exists".format(name)}, 400
        
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {"message": "An Error Occured while inserting the New Store"}, 500 # Internal Server Error
        return store.json(), 201


    #^ NOTE     DELETE METHOD
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "Store Deleted"}
        else:
            return {"message": "Store Not Found"}, 404


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}