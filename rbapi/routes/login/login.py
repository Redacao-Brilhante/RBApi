from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource

login_router = Blueprint('login_router', __name__)
api = Namespace('Login', description='Realizar login na plataforma')


@api.route('/login', methods=['POST'])
class Login(Resource):
    def post(self):
        body = request.get_json()

        if not body or 'login' not in body or 'password' not in body:
            return Response('Parametros invalidos', status=400, mimetype='application/json')
