from models.concessionária import Carro

gol = Carro("Gol", "Volkswagen", 2012)
civic = Carro("Civic", "Honda", 2020)
fusca = Carro("Fusca", "Volkswagen", 1975)
mustang = Carro("Mustang", "Ford", 1967)

Carro.vender(fusca)

def main():
    Carro.estoque_carros()

if __name__ == "__main__":
    main()