from models.curso import Curso

sistemas = Curso("Desenvolvedor de Sistemas")
web = Curso("Programador Web")

sistemas.matricular_aluno("Paulo", 18)
sistemas.matricular_aluno("Willy", 20)
sistemas.matricular_aluno("Luiz", 18)

web.matricular_aluno("Darion", 45)
web.matricular_aluno("Siwana", 24)
web.matricular_aluno("Pietro", 17)

def main():
    Curso.listar_alunos(sistemas)
    Curso.listar_alunos(web)

if __name__ == '__main__':
    main()