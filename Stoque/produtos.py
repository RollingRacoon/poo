class Produto:
    produtos = []
    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco
        self.status = False
        Produto.produtos.append(self)
    def __str__(self):
        return f"Produto: {self.nome_produto} | R${self.preco} | Status: {self.status}"
    def aplicar_desconto(self, desconto):
        self.desconto = desconto
        self.preco -= desconto
    def listar_produtos():
        for produto in Produto.produtos:
            print(f"Produto: {produto.nome_produto} | R${produto.preco} | Status: {produto.status}")

coca = Produto("Coca Cola 2L", 10.99)
freddo = Produto("Freddo Torta Belga 500ml", 41.90)
cheetos = Produto("Salgadinho Cheetos Onda Requeijão 75g", 8.99)
Produto.aplicar_desconto(freddo, 6.00)
# print(coca)
# print(freddo)
# print(cheetos)
# print("=============================================================================")
Produto.listar_produtos()