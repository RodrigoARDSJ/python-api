class Jogo:
    def __init__(self):
        self.__id: int = 0
        self.__nome: str = ''
        self.__descricao: str = ''

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao) -> None:
        self.__descricao = descricao

    def __str__(self) -> dict:
        return {"nome": self.nome, "descricao": self.descricao}

    def __eq__(self, other) -> bool:
        return self.id == other.id