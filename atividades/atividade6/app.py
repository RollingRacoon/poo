from models.funcionario import Funcionario

funcionario1 = Funcionario("Ana", "Gerente", 5000)
funcionario2 = Funcionario("Carlos", "Analista", 3500)
funcionario3 = Funcionario("Mariana", "Assistente", 2500)

Funcionario.aumentar_salario(funcionario3, 15)

def main():
    Funcionario.listar_funcionarios()

if __name__ == '__main__':
    main()