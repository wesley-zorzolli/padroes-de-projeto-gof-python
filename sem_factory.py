class CarroPopular:
    def exibir_info(self):
        print("Carro popular: Econômico e compacto.")

class CarroEsportivo:
    def exibir_info(self):
        print("Carro esportivo: Potente e veloz.")

class Cliente:
    def solicitar_carro(self, tipo):
        if tipo == "popular":
            return CarroPopular()
        elif tipo == "esportivo":
            return CarroEsportivo()
        else:
            raise ValueError("Tipo de carro inválido.")

# Uso
cliente = Cliente()

carro1 = cliente.solicitar_carro("popular")
carro1.exibir_info()

carro2 = cliente.solicitar_carro("esportivo")
carro2.exibir_info()
