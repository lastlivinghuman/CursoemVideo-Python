from functools import singledispatchmethod
from locale import currency, setlocale, LC_ALL

class Produto:

    def __init__(self, nome:str, preco:float) -> None:
        self.nome:str = nome
        self.preco:float = preco

    singledispatchmethod
    def __add__(self, other):
        carrinho = Carrinho()


        if isinstance(other, Produto):
            carrinho.produtos.extend([self,other])
            return carrinho

        elif isinstance(other, Carrinho):
            carrinho.produtos.append(self)
            carrinho.produtos.extend(other.produtos)
            return carrinho






    def __str__(self) -> str:
        setlocale(LC_ALL, 'Portuguese_Brazil.1252')
        return f"{self.nome}({currency(self.preco, grouping=True)})"



class Carrinho:

    def __init__(self):
        self.produtos:[] = []


    @property
    def total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total


    @singledispatchmethod
    def __add__(self, other):

        if isinstance(other, Produto):
            self.produtos.append(other)
            return self

        elif isinstance(other, Carrinho):
            self.produtos.extend(other.produtos)
            return self

        return NotImplemented


    def __str__(self)-> None:
        texto = ""
        for produto in self.produtos:
            texto += f"{produto}\n"

        texto += f"Total: {self.total}"
        return texto