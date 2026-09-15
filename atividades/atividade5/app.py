from models.catalogo import Filme

filme_01 = Filme("Invocação do Mal", "Terror/Mistério", 2013)
filme_02 = Filme("Carros", "Infantil/Comédia", 2006)
filme_03 = Filme("Festa da Salsicha", "Comédia/Fantasia", 2016)
filme_04 = Filme("Velozes & Furiosos: Desafio em Tóquio", "Ação/Crime", 2006)
filme_05 = Filme("Reine sobre Mim", "Drama/Drama familiar", 2007)

def main():
    Filme.listar_filmes()

if __name__ == '__main__':
    main()