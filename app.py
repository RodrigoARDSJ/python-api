import os
from flask import send_from_directory
from controller.jogoController import *
from config.swaggerConfig import *
from server.instance import server

app = app


@app.route('/')
def index():
    return Response(json.dumps({"Erro": "not found way"}), status=404, mimetype='application/json')


@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(f'{os.getcwd()}/templates', 'not-found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
