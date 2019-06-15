from flask_restful import Resource
from generator import get_item

class Item(Resource):

    def get(self):
        return get_item()
