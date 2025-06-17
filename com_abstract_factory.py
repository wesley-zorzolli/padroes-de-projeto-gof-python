from abc import ABC, abstractmethod

# Produtos abstratos
class Botao(ABC):
    @abstractmethod
    def desenhar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def abrir(self):
        pass

# Produtos concretos
class BotaoWindows(Botao):
    def desenhar(self):
        print("Botão estilo Windows")

class BotaoMac(Botao):
    def desenhar(self):
        print("Botão estilo Mac")

class JanelaWindows(Janela):
    def abrir(self):
        print("Janela estilo Windows")

class JanelaMac(Janela):
    def abrir(self):
        print("Janela estilo Mac")

# Fábrica abstrata
class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

# Fábricas concretas
class WindowsFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

class MacFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return BotaoMac()

    def criar_janela(self) -> Janela:
        return JanelaMac()

# Uso
def criar_ui(factory: UIFactory):
    botao = factory.criar_botao()
    janela = factory.criar_janela()

    botao.desenhar()
    janela.abrir()

# Teste
criar_ui(WindowsFactory())
criar_ui(MacFactory())
