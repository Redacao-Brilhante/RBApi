from flask import Flask
from flask_restx import Api
from rbapi.databaseengine import db_session
from configuration import config
from rbapi.routes.login.login import login_router, api as namespace_login
from rbapi.routes.user.user import user_router, api as namespace_user

app = Flask(__name__)

api = Api(app,
          version='1.0',
          title='Api Redação brilhate',
          doc='/docs'
          )


def register_blueprint():
    blueprints = [
        user_router,
        login_router,

    ]

    [app.register_blueprint(blueprint, url_prefix=config.API_BASE_URL)
     for blueprint in blueprints]


def add_namespace():
    namespaces = [
        namespace_login,
        namespace_user
    ]
    [api.add_namespace(namespace, path=config.API_BASE_URL)
     for namespace in namespaces]


@app.route('/')
def hello():
    return 'Hello!'
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()