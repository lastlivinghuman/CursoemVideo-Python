from functools import singledispatchmethod


class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possivel analisar {valor}")


    @analisar.register
    def _(self,valor:int):
        print(f"{valor} é um inteiro!")


    @analisar.register
    def _(self, valor:float):
        print(f"{valor} é um float")


    @analisar.register
    def _(self, valor:str):
        print(f"{valor} é uma cadeia de caractres")


    @analisar.register
    def _(self, valor: tuple | list | dict):
        print(f"{valor} é uma coleção de dados")