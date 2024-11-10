from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, chassi, cilindrada, cor, ano, quilometragem, preco):

        super().__init__(marca, modelo, cor, ano, quilometragem, preco, chassi)
        self.__cilindrada = cilindrada


    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def get_potencia_cilindrada(self):
        return self.__cilindrada



moto1 = Moto("Honda", "remaza", "1237-123-ads123", 750, "azul", "1999", "8000km", "R$60.000")

print(moto1.imprimir_dados())