from models.hotel import Hotel

astron = Hotel("Astron Suítes", "São José dos Pinhais")
palace = Hotel("Curitiba Palace", "Curitiba")
goldmen = Hotel("GoldMen Business", "Londrina")

astron.receber_avaliacoes("Poliana", 5)
astron.receber_avaliacoes("Jefferson", 3.6)
astron.receber_avaliacoes("Rodrigo", 4.2)
astron.receber_avaliacoes("Gislaine", 1.4)
astron.receber_avaliacoes("Fernanda", 4.8)
palace.receber_avaliacoes("Roberto", 3.4)
palace.receber_avaliacoes("Celton", 4.5)
palace.receber_avaliacoes("Sebastian", 4.8)
palace.receber_avaliacoes("Micaela", 1)
palace.receber_avaliacoes("Jennifer", 3.8)
goldmen.receber_avaliacoes("Miranda", 5)
goldmen.receber_avaliacoes("Maria", 5)
goldmen.receber_avaliacoes("Orlando", 4.1)
goldmen.receber_avaliacoes("Maurício", 3.9)
goldmen.receber_avaliacoes("Vanessa", 4.7)

def main():
    Hotel.listar_hoteis()

if __name__ == '__main__':
    main()