from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource

user_router = Blueprint('user_router', __name__)
api = Namespace('User', description='Rotas do usuario')


@api.route('/user', methods=['GET', 'DELETE', 'PUT'])
class User(Resource):
    def get(self):
        ...

    def delete(self):
        ...

    def put(self):
        ...
