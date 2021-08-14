import os

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from configuration import config
from rbapi.routes.login.login import login_router, api as namespace_login
from rbapi.routes.user.user import user_router, api as namespace_user

app = Flask(__name__)

api = Api(app,
          version='1.1',
          title='Api Redação brilhate',
          doc='/docs'
          )


def register_blueprint():
    app.register_blueprint(login_router, url_prefix=config.API_BASE_URL)
    app.register_blueprint(user_router, url_prefix=config.API_BASE_URL)


def add_namespace():
    api.add_namespace(namespace_login, path=config.API_BASE_URL)
    api.add_namespace(namespace_user, path=config.API_BASE_URL)


app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/rb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello!'
