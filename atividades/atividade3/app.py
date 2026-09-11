from models.conta_bancaria import ContaBancaria

conta1 = ContaBancaria("Fernando Kubitschek Kava", 1539.20)
conta2 = ContaBancaria("Eduarda Rossi Weber", 900)

conta_escolhida = int(input("\nEscolha sua conta: \n1 - Fernando Kubitschek Cava \n2 - Eduarda Rossi Weber \n\nDigite o número da conta escolhida: "))

match conta_escolhida:
    case 1:
        conta = conta1
    case 2:
        conta = conta2
    case _:
        print("Conta Inválida!")
        conta = None

ContaBancaria.menu(conta)