class Aluno:

    alunos = []

    def __init__(self, aluno, idade, curso):
        self._aluno = aluno
        self._idade = idade
        self._curso = curso
        Aluno.alunos.append(self)

    def __str__(self):
        return f"{self._aluno}\n|Idade: {self._idade} anos\n|Curso: {self._curso}"

    @classmethod
    def listar_alunos(cls):
        for aluno in cls.alunos:
            print(f"{aluno._aluno}\n|Idade: {aluno._idade} anos\n|Curso: {aluno._curso}")