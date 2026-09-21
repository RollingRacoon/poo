class Funcionario:

    funcionarios = []

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario
        Funcionario.funcionarios.append(self)

    def __str__(self):
        return f"Nome do Funcionário: {self.nome}\n| Cargo: {self.cargo}\n| Salário: R${self.cambio_salario}\n===================================="

    @property
    def cambio_salario(self):
        return f"R${round(self._salario,2)}"

    def aumentar_salario(self, percentual):
        calculo_percentual = percentual / 100
        aumento = self._salario * calculo_percentual
        self._salario += aumento

    @classmethod
    def listar_funcionarios(cls):
        for funcionario in cls.funcionarios:
            print(f"Nome do Funcionário: {funcionario.nome}\n| Cargo: {funcionario.cargo}\n| Salário: R${funcionario.cambio_salario}\n====================================")