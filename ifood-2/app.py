from models.restaurante import Restaurante

la_mafia = Restaurante("La Mafia", "Rua Açaí, N°401", "Italiana", 7)
mada = Restaurante("Mada Pizzaria", "Rua Atilho, N°209", "Italiana", 4)
steve_pizza = Restaurante("Steve Pizza", "Rua Doutor Murici, 70", "Porções", 3)

Restaurante.alterar_estado(la_mafia)

la_mafia.receber_avaliacoes("Heron Gordo", 5)


def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()