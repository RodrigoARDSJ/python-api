from model.jogo import Jogo


class DBFactory:
    jogos: list = []
    jogo1: Jogo = Jogo()
    jogo2: Jogo = Jogo()
    jogo3: Jogo = Jogo()

    jogo1.id = 1
    jogo1.nome = "Assassins Creed"
    jogo1.descricao = "Jogo 1."

    jogo2.id = 2
    jogo2.nome = "Red dead redenption 2"
    jogo2.descricao = "Jogo 2."

    jogo3.id = 3
    jogo3.nome = "Fifa"
    jogo3.descricao = "Jogo 3 "

    jogos.append(jogo1)
    jogos.append(jogo2)
    jogos.append(jogo3)

    def get_jogos(self) -> list:
        return self.jogos
