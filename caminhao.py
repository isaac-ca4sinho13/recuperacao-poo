from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, chassi, qtd_eixos, cor, ano, quilometragem, preco):
        
        super().__init__(marca, modelo, cor, ano, quilometragem, preco, chassi)
        self.__qtd_eixos = qtd_eixos

    
    def get_qtd_eixos(self):
        return self.__qtd_eixos

    def set_qtd_eixos(self, qtd_eixos):
        self.__qtd_eixos = qtd_eixos

