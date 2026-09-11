from models.avaliacoes import Avaliacoes
class Restaurante:
    restaurantes = []
    def __init__(self, nome_restaurante, localizacao, tipo_de_comida, quantidade_funcionarios):
        self.nome_restaurante = nome_restaurante
        self.localizacao = localizacao
        self.tipo_de_comida = tipo_de_comida
        self.quantidade_funcionarios = quantidade_funcionarios
        self._status = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f"Nome: {self.nome_restaurante} \n|Rua: {self.localizacao} \n|Tipo de Comida: {self.tipo_de_comida} \n|Quantidade de Funcionários: {str(self.quantidade_funcionarios)} \n|Status: {self._ativo}"
    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_de_comida} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Avaliações: {restaurante.media_avaliacoes} \n|Status: {restaurante.ativo}")
    @property
    def ativo(self):
        return "Ativo" if self._status else "Inativo"
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(notas_somadas/quantidade_avaliacoes, 1)
        return media

    def alterar_estado(self):
        self._status = not self._status

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)