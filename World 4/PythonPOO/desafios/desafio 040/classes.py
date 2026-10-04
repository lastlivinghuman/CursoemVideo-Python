
import json
import xml.etree.ElementTree as ET


class Usuario:

    def __init__(self, nome: str, email: str):
        self.nome: str = nome
        self.email: str = email


class Aluno:

    def __init__(self, nome: str, curso: str, serie: int):
        self.nome: str = nome
        self.curso: str = curso
        self.serie: int = serie


class JSON:

    def exportar(self, dados):
        dados_convertidos = [objeto.__dict__ for objeto in dados]
        texto_json = json.dumps(dados_convertidos, indent=4)
        print(texto_json)


class XML:

    def exportar(self, dados):
        raiz = ET.Element("root")

        for objeto in dados:
            elemento = ET.SubElement(raiz, objeto.__class__.__name__)

            for chave, valor in objeto.__dict__.items():
                campo = ET.SubElement(elemento, chave)
                campo.text = str(valor)

        xml = ET.tostring(raiz, encoding="unicode")
        print(xml)


def exportar_dados(objeto: object, dados):
    try:
        objeto.exportar(dados)
    except Exception as e:
        print(e)