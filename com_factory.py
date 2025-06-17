from abc import ABC, abstractmethod

# Produto
class Carro(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

class CarroPopular(Carro):
    def exibir_info(self):
        print("Carro popular: Econômico e compacto.")

class CarroEsportivo(Carro):
    def exibir_info(self):
        print("Carro esportivo: Potente e veloz.")

# Criador
class FabricaCarro(ABC):
    @abstractmethod
    def criar_carro(self) -> Carro:
        pass

class FabricaPopular(FabricaCarro):
    def criar_carro(self) -> Carro:
        return CarroPopular()

class FabricaEsportivo(FabricaCarro):
    def criar_carro(self) -> Carro:
        return CarroEsportivo()

# Uso
fabrica = FabricaPopular()
carro = fabrica.criar_carro()
carro.exibir_info()

fabrica2 = FabricaEsportivo()
carro2 = fabrica2.criar_carro()
carro2.exibir_info()
