from veiculo import Veiculo

class Lancha(Veiculo):
    def __init__(self, marca, modelo, chassi, potencia, cor, ano, horas_uso, preco):

        super().__init__(marca, modelo, cor, ano, horas_uso, preco, chassi)

        self.__potencia = potencia
        self.__horas_uso = horas_uso

    
    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia


    def get_horas_uso(self):
        return self.__horas_uso

    def set_horas_uso(self, horas_uso):
        self.__horas_uso = horas_uso
        

    def get_potencia_cilindrada(self):
        return self.__cilindrada
 



