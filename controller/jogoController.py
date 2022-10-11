import json
from typing import Any

import werkzeug.exceptions
from flask import request, Response
from service.jogoService import JogoService
from server.instance import server
from model.jogo import Jogo

app = server.app
jogo_service = JogoService()


@app.route('/jogos')
def get_all_jogos() -> Response:
    jogos = [(jogo.__str__()) for jogo in jogo_service.listar_jogos()]
    jogos = json.dumps(jogos)
    if len(jogos) == 0:
        return Response(jogos, status=204, mimetype='application/json')
    else:
        return Response(jogos, status=200, mimetype='application/json')


@app.route('/jogos/<int:id>')
@app.errorhandler(werkzeug.exceptions.NotFound)
def get_jogo_by_id(id) -> Any:
    jogo = jogo_service.busca_por_id(id)
    if jogo:
        jogo = json.dumps(jogo.__str__())
        return Response(jogo, status=200, mimetype='application/json')
    else:
        return 'jogo não encontrado', 404


@app.route('/jogos', methods=['POST'])
@app.errorhandler(werkzeug.exceptions.BadRequest)
def add_jogo() -> Any:
    new_jogo = request.get_json()
    response: bool | str = jogo_service.criar(new_jogo)
    if type(response) is bool:
        return Response(status=201)
    else:
        return f'Erro: Atributo {response} pendente', 400


@app.route('/jogos/<int:id>', methods=['PUT'])
@app.errorhandler(werkzeug.exceptions.BadRequest)
def att_jogo(id) -> Any:
    jogo = request.get_json()
    response = jogo_service.atualizar(jogo, id)
    if type(response) is jogo:
        retorno = json.dumps(response.__str__())
        return Response(retorno, status=200, mimetype='application/json')
    elif "atributo" in response:
        return response, 400
    else:
        return response, 400


@app.route('/jogos/<int:id>', methods=['DELETE'])
def delete_jogo(id) -> Response:
    if jogo_service.deletar(id):
        return Response(status=204)
    else:
        return Response("Cliente não encontrado!", status=404, mimetype='application/json')
