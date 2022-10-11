from typing import Any

from model.jogo import Jogo
from util.DBFactory import DBFactory


class JogoDaoSemBanco:
    def __init__(self):
        self.factory: DBFactory = DBFactory()
        self.jogos: list[Jogo] = self.factory.jogos

    def find_all(self) -> list:
        return self.jogos

    def find_by_id(self, id) -> Any:
        jogo_por_id: Jogo = Jogo()
        for jogo in self.jogos:
            if jogo.id == id:
                jogo_por_id = jogo
        if jogo_por_id.id < 1:
            return None
        return jogo_por_id

    def save(self, jogo) -> bool:
        jogo.id = len(self.jogos) + 1
        self.jogos.append(jogo)
        return True

    def update(self, corpo, id) -> Any:
        if id > len(self.jogos) or id < 1:
            return None
        else:
            jogo: Jogo = Jogo()
            jogo.id = id
            jogo.nome = corpo['nome']
            jogo.descricao = corpo['descricao']
            self.jogos[id - 1] = jogo
            return jogo

    def delete_by_id(self, id) -> bool:
        if self.is_present(id):
            self.jogos.pop(id)
            return True
        else:
            return False

    def is_present(self, id) -> bool:
        jogo = self.jogos[id - 1]
        if jogo:
            return False
        else:
            return True
