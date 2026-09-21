from models.aluno import Aluno
class Curso:

    cursos = []

    def __init__(self, nome_curso):
        self.nome_curso = nome_curso
        self._alunos = []
        Curso.cursos.append(self)

    def matricular_aluno(self, nome, idade):
        aluno = Aluno(nome, idade)
        self._alunos.append(aluno)

    def listar_alunos(self):
        print(f"\n{self.nome_curso}")
        for aluno in self._alunos:
            print(f"Aluno: {aluno._nome.ljust(15)} | Idade: {aluno._idade}")