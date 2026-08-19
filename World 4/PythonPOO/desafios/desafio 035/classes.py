from abc import ABC


class Arquivo(ABC):


    def __init__(self, nome:str, tamanho:float):
        self.nome:str = nome
        self.tamanho:float = tamanho / 1_000_000
        self._extensao:float = 0.0


    @property
    def nome_completo(self):
        return f"'{self.nome}.{self._extensao}'({self.tamanho:.2f}MB)"

    @nome_completo.setter
    def nome_completo(self, nome:str):
        raise PermissionError("Voce não pode alterar o nome!")


    def abrir_arquivo(self):
        pass


class DOC(Arquivo):

    def abrir_arquivo(self):
        self._extensao = "docx"
        return f"Abrindo o arquivo {self.nome_completo} no Microsoft Word"



class PDF(Arquivo):

    def abrir_arquivo(self):
        self._extensao = "pdf"
        return f"Abrindo o arquivo {self.nome_completo} no Microsoft Word"



def abrir_arquivo(objeto:object):
    try:

        print(objeto.abrir_arquivo())
    except:
        return