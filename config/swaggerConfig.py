from server.instance import server
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory, Response
import os

app = server.app

SWAGGER_URL = '/swagger/'
API_URL = '/config/swagger.yml'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "connection"})

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/config/swagger.yml')
def specs():
    return send_from_directory(f"{os.getcwd()}/config", "swagger.yml")
