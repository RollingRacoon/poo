class Carro:

    carros = []

    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self._status = False
        Carro.carros.append(self)

    def __str__(self):
        return f"| {self.marca.ljust(15)} {self.modelo.ljust(8)} - {str(self.ano).ljust(5)} | Status: {self.vendido.ljust(10)} |"

    @classmethod
    def estoque_carros(cls):
        for carro in cls.carros:
            print(f"| {carro.marca.ljust(15)} {carro.modelo.ljust(8)} - {str(carro.ano).ljust(5)} | Status: {carro.vendido.ljust(10)} |")

    @property
    def vendido(self):
        return "Vendido" if self._status else "Disponível"

    def vender(self):
        self._status = not self._status