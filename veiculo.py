

class Veiculo:
    def __init__(self, marca, modelo, cor, ano, quilometragem, preco, chassi):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__quilometragem = quilometragem
        self.__preco = preco
        self.__chassi = chassi

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca


    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo


    def get_cor(self):
        return self.__cor
    
    def set_cor(self, cor):
        self.__cor = cor


    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano


    def get_quilometragem(self):
        return self.__quilometragem
    
    def set_quilometragem(self, quilometragem):
        self.__quilometragem = quilometragem


    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco


    def get_chassi(self):
        return self.__chassi

    def set_chassi(self, chassi):
        self.__chassi = chassi


    
    def imprimir_dados(self):

        print(f"Marca: {self.__marca}\n"
              f"Modelo: {self.__modelo}        Potência/Cilindrada: {self.get_potencia_cilindrada()}\n"
              f"Cor: {self.__cor} Ano: {self.__ano}   Quilometragem/Horas de uso: {self.__quilometragem}\n"
              f"Preço: {self.__preco}")
        
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
        return self.__potencia
    

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, chassi, qtd_eixos, cor, ano, quilometragem, preco):
        
        super().__init__(marca, modelo, cor, ano, quilometragem, preco, chassi)
        self.__qtd_eixos = qtd_eixos

    
    def get_qtd_eixos(self):
        return self.__qtd_eixos

    def set_qtd_eixos(self, qtd_eixos):
        self.__qtd_eixos = qtd_eixos


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


moto1 = Moto("Honda", "remaza", "12ASD123", 750, "azul", "1999", 8000, 60000)
moto2 = Moto("Yamaha", "Fazer 250", "ABC98765", 250, "Preta", "2018", 30000, 11500)

carro1 = Carro("Ford", "Fusion", "RST34567", 200, "Cinza", 2018, 80000, 95000)
carro2 = Carro("Chevrolet", "Camaro", "UVX87654", 400, "Amarelo", 2021, 15000, 140000)

lancha1 = Lancha("Sea Ray", "SLX 400", "LMN45678", 350, "Branca", 2022, 500, 350000)
lancha2 = Lancha("Bayliner", "VR5", "OPQ87654", 280, "Azul", 2021, 300, 250000)


caminhao1 = Caminhao("Scania", "R 440", "JKL12345", 3, "Branco", 2019, 250000, 250000)
caminhao2 = Caminhao("Mercedes-Benz", "Actros 2545", "MNO98765", 4, "Preto", 2020, 200000, 280000)


