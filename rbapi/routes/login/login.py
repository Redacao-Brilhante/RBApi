from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource, fields

login_router = Blueprint('login_router', __name__)
api = Namespace('Login', description='Realizar login na plataforma')

login_fields = api.model('Login',{
    'login': fields.String,
    'password': fields.String
})

@api.route('/login', methods=['POST'])
class Login(Resource):
    @api.doc(responses={200: 'Login realizado com sucesso.'})
    @api.doc(responses={400: 'Parâmetros invalidos'})
    @api.doc(responses={500: 'Erro no servidor'})
    @api.expect(login_fields)

    def post(self):
        try:
            body = request.get_json()

            if not body or 'login' not in body or 'password' not in body:
                return Response('Parametros invalidos', status=400, mimetype='application/json')

        except Exception as e:
            return Response('Erro no servidor', status=500, mimetype='application/json')
