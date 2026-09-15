from models.biblioteca import Livro

livro_01 = Livro("1984", "George Orwell", "1949")
livro_02 = Livro("Dom Casmurro", "Machado de Assis", "1899")
livro_03 = Livro("O Hobbit", "J.R.R. Tolkien", "1937")
livro_04 = Livro("It", "Stephen King", "1986")

Livro.emprestar(livro_04)
Livro.emprestar(livro_02)
Livro.devolver(livro_01)

def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()