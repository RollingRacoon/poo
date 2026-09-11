class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

        ContaBancaria.contas.append(self)

    def __str__(self):
        return f"| Titular: {self.titular} | Saldo em conta: R${self.saldo} |\n================================================="

    @classmethod
    def listar_contas(cls):
        for conta in cls.contas:
            print(f"| Titular: {conta.titular} | Saldo em conta: R${conta.saldo} |\n=================================================")

    def depositar(self, valor):
        self._saldo += valor
 
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print(f"Saldo insuficiente para realizar o saque de R$ {valor:.2f}")

    def menu(conta):
        if conta:
            operacao = int(input("\nQual operação deseja realizar? \n1 - Consultar Saldo \n2 - Depósito \n3 - Saque \n\nEscolha uma operação: "))
            match operacao:
                case 1:
                    print(f"\nSeu saldo é de: R${conta.saldo:.2f}")
                case 2:
                    valor = float(input("\nDigite o valor a ser depositado: "))
                    conta.depositar(valor)
                    print(f"Novo saldo: R${conta.saldo:.2f}")
                case 3:
                    valor = float(input("\nDigite o valor a ser sacado: "))
                    conta.sacar(valor)
                    print(f"Novo saldo: R${conta.saldo:.2f}")
                case _:
                    print("Operação Inválida!")

    
    @property
    def saldo(self):
        return self._saldo