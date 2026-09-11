from models.aluno import Aluno

lucas = Aluno("Lucas Ribeiro da Silva", 17, "Administração")
sandra = Aluno("Sandra Almeida da Rocha", 16, "Formação de Doscentes")
guilherme = Aluno("Guilherme Alcântra de Oliveira", 18, "Gastronomia")

def main():
    Aluno.listar_alunos()

if __name__ == "__main__":
    main()