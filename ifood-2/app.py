from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa

la_mafia = Restaurante("La Mafia", "Rua açai, N:401", "Italiana", 7)
mada = Restaurante("Mada Pizzaria","Rua Atilio, N:209", "Italiana",4)
steve_pizza = Restaurante("Steve Pizza","Rua Doutor Murici, 70","Porções",3)
Restaurante.alterar_estado(la_mafia)
la_mafia.receber_avaliacoes("Heron", 5)

macarrao = Prato("Macarrão do poderoso chefinho", 129.99, "Macarrão muito de bom da vovó, minde papai")
chublub_fortnite = Bebida("GlubGlub azul", 1299.50, "Gigante, ai que dimais")
sobremesa_01 = Sobremesa("Sorvete Flamenguinho",19.99,"Sabor Danonão grosso")

pastel = Prato("Pastel de Flango", 16.99, "Pastel de Flango de passaros da sacada do prédio(pombo)")

la_mafia.adicionar_cardapio(macarrao)
la_mafia.adicionar_cardapio(chublub_fortnite)
la_mafia.adicionar_cardapio(sobremesa_01)

def main():
    la_mafia.exibir_cardapio

if __name__ == '__main__':
    main()
