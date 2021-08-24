from configuration import config
from rbapi.databaseengine import init_db
from rbapi.flaskapp.flask_app import add_namespace, register_blueprint, app

if __name__ == '__main__':
    add_namespace()
    init_db()
    register_blueprint()
    app.run(host=config.API_HOST, debug=config.DEBUG, port=config.API_PORT)
