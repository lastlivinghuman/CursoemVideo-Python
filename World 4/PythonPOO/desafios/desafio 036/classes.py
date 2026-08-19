from abc import ABC



class Pagamento(ABC):


    def __init__(self, valor:float=0):
        self._valor:float = valor


    @property
    def fvalor(self):
        from locale import currency, setlocale, LC_ALL

        setlocale(LC_ALL, 'Portuguese_Brazil.1252')
        return currency(self._valor, grouping=True)

    @fvalor.setter
    def fvalor(self, valor:float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Valor menor que 0 ")

    def pagar(self):
        pass




class Boleto(Pagamento):

    def pagar(self):
        print(f"Pagamento confirmado de {self.fvalor} via Boleto!")



class PIX(Pagamento):

    def pagar(self):
        print(f"Pagamento confirmado de {self.fvalor} via PIX!")




class Cartao_credito(Pagamento):

    def pagar(self):
        print(f"Pagamento confirmado de {self.fvalor} via CARTÂO DE CREDITO!")



def finalizar_compra(tipo_depag:Pagamento, valor:float):
    try:
        tipo_depag.fvalor = valor
        tipo_depag.pagar()

    except:
        print("Houve um erro")
