

class Carteira:

    def __init__(self, valor:int|float):
        self.__saldo = valor


    def __str__(self):
        return f"A carteira tem R${self.__saldo:,.2f}"
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor:int|float):
        raise PermissionError("Voce não pode alterar o saldo usando este metodo!")


    def __eq__(self, outro) -> bool:
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False


    def __iadd__(self, valor:int|float):
        self.__saldo += valor
        return self

    def __isub__(self, valor:int|float):
        self.__saldo -= valor
        return self