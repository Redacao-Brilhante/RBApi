from configuration import config
from rbapi.flaskapp import app, add_namespace, register_blueprint

if __name__ == '__main__':
    add_namespace()
    register_blueprint()
    app.run(host=config.API_HOST, debug=config.DEBUG, port=config.API_PORT)
