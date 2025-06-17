class BotaoWindows:
    def desenhar(self):
        print("Botão estilo Windows")

class BotaoMac:
    def desenhar(self):
        print("Botão estilo Mac")

class JanelaWindows:
    def abrir(self):
        print("Janela estilo Windows")

class JanelaMac:
    def abrir(self):
        print("Janela estilo Mac")

def criar_ui(sistema):
    if sistema == "windows":
        botao = BotaoWindows()
        janela = JanelaWindows()
    elif sistema == "mac":
        botao = BotaoMac()
        janela = JanelaMac()
    else:
        raise ValueError("Sistema não suportado")

    botao.desenhar()
    janela.abrir()

# Uso
criar_ui("windows")
criar_ui("mac")
