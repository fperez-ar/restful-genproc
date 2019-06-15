from flask_restful import Resource, Api
from flask import Flask
from endpoints.Item import Item

app = Flask(__name__)
api = Api(app)

api.add_resource(Item, '/item')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
