from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser


def restful_api(model=object):
    class Restful(Resource, model):

        def __init__(self):
            super().__init__()

        def get(self):
            request = self.parser.parse_args(strict=True)
            return self.predict(**request)

        @classmethod
        def app(cls):
            app = Flask(__name__)
            api = Api(app)
            api.add_resource(cls, cls().routing)
            app.run(debug=True)

    return Restful
