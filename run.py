from configuration import config
from rbapi.flaskapp import app, db, add_namespace, register_blueprint
from rbapi import models

if __name__ == '__main__':
    add_namespace()
    register_blueprint()
    app.run(host=config.API_HOST, debug=config.DEBUG, port=config.API_PORT)
