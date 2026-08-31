from abc import ABC, abstractmethod


class Arquivo(ABC):


    def __init__(self, nome:str,ext:str,  tamanho:float):
        self.nome:str = nome
        self.tamanho:float = tamanho
        self._extensao = None
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao


    @extensao.setter
    def extensao(self, ext:str):
        formatos = ["pdf", "doc", "docx"]

        if ext.lower().strip() in formatos:
            self._extensao = ext

        else:
            raise AttributeError("O arquivo esta em um formato não suportado!")


    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1_000_000}MB)"



class DOC(Arquivo):

    def __init__(self, nome:str, tam:float):
        super().__init__(nome, "docx", tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word!")


class PDF(Arquivo):

    def __init__(self, nome:str, tam:float):
        super().__init__(nome, "pdf", tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader!")

def abrir_arquivo(objeto:object):
    try:
        objeto.abrir()
    except:
        return