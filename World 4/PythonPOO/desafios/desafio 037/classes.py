from rich import print
from rich.panel import Panel
from rich.console import Console

class Mensagem:

    def __init__(self, msg:str):
        self._mensagem:str = msg
        self._tipo:str = self.__class__.__name__
        self._icone:str = ""


    def mostrar(self):
        titulo = ":speech_balloon: Aviso :speech_balloon:"
        conteudo = f"{self._mensagem}"
        caixa:str = Panel(conteudo, title=titulo,  width=50, style="white on black")
        print(caixa)




class Alerta(Mensagem):

    def mostrar(self):
        titulo = f":warning: {self._tipo} :warning:"
        conteudo = f"{self._mensagem}"
        caixa: str = Panel(conteudo, title=titulo, width=50, style="black on yellow")
        print(caixa)



class Erro(Mensagem):


    def mostrar(self):
        titulo = f":no_entry_sign: {self._tipo} :no_entry_sign:"
        conteudo = f"{self._mensagem}"
        caixa: str = Panel(conteudo, title=titulo, width=50, style="white on red")
        print(caixa)
