from typing import Any
from flask import Flask

from dao.jogoDaoSemBanco import JogoDaoSemBanco
from model.jogo import Jogo
import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)

app = Flask(__name__)

class JogoService:
    def __init__(self):
        self.__jogo_dao = JogoDaoSemBanco()

    def listar_jogos(self) -> list:
        app.logger.info("INICIANDO METODO DE LISTAGEM  DE JOGOS")
        app.logger.info("LISTANDO TODOS OS JOGOS")
        return self.__jogo_dao.find_all()

    def busca_por_id(self, id) -> Any:
        app.logger.info("INICIANDO METODO PARA BUSCAR UM JOGO")
        jogo = self.__jogo_dao.find_by_id(id)
        app.logger.info("BUSCANDO JOGO PELO ID ")
        if jogo is None:
            app.logger.info("FINALIZANDO METODO DE BUSCAR JOGo")
            return False
        else:
            app.logger.info("FINALIZANDO METODO DE BUSCAR JOGO")
            return jogo

    def criar(self, jogo_req) -> Any:
        app.logger.info("INICIANDO METODO PARA CADASTRAR UM JOGO")
        valida = self.__valida_json(jogo_req)
        if type(valida) is bool:
            jogo: Jogo = Jogo()
            jogo.nome = jogo_req['nome']
            jogo.descricao = jogo_req['descricao']
            app.logger.info("JOGO CADASTRADO")
            app.logger.info("FINALIZANDO METODO DE CADASTRO")
            return self.__jogo_dao.save(jogo)
        else:
            return valida

    def atualizar(self, jogo, id) -> Any:
        app.logger.info("INICIANDO METODO PARA ATUALIZAR UM JOGO")
        valida: bool | list = self.__valida_json(jogo)
        if type(valida) is bool:
            jogo_res = self.__jogo_dao.update(jogo, id)
            if jogo_res is None:
                app.logger.warning("JOGO NÃO ENCONTRADO: ID = " + id)
                return "JOGO nao encontrado!"
            else:
                app.logger.info("JOGO CADASTRADO COM SUCESSO")
                return jogo_res
        else:
            return f"Erro atributo {valida} pendente!"

    def deletar(self, id) -> bool:
        app.logger.info("INICIANDO METODO DE DELETAR JOGO")
        delete =self.__jogo_dao.delete_by_id(id)
        app.logger.info("JOGO DELETADO COM SUCESSO")
        app.logger.info("FINALIZANDO METODO DELETAR")
        return delete

    @staticmethod
    def __valida_json(jogo):
        props = ["nome", "descricao"]
        for prop in props:
            if prop in jogo:
                return True
            else:
                return prop

