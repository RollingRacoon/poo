class Filme:

    filmes = []

    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        Filme.filmes.append(self)

    @classmethod
    def listar_filmes(cls):
        print(f"|{"Filme".ljust(40)}|{"Gênero".ljust(40)}|{"Ano de Lançamento".ljust(40)}")
        for filme in cls.filmes:
            print(f"|{filme.titulo.ljust(40)}|{filme.genero.ljust(40)}|{str(filme.ano).ljust(40)}")