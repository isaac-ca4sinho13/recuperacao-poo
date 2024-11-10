from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, chassi, potencia, cor, ano, quilometragem, preco):
        
        super().__init__(marca, modelo, cor, ano, quilometragem, preco, chassi)
        self.__potencia = potencia


    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

  
    def get_potencia_cilindrada(self):
        return self.__potencia
 