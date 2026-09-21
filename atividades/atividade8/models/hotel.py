from models.avaliacao import Avaliacao
class Hotel:

    hoteis = []

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self._avaliacoes = []
        Hotel.hoteis.append(self)

    def __str__(self):
        return f"{hotel.nome}\n| Cidade: {hotel.cidade}\n| Nota: {hotel.media_avaliacoes}\n=============================="

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(notas_somadas / quantidade_avaliacoes, 1)
        return media

    @classmethod
    def listar_hoteis(cls):
        for hotel in cls.hoteis:
            print(f"{hotel.nome}\n| Cidade: {hotel.cidade}\n| Nota: {hotel.media_avaliacoes}\n==============================")