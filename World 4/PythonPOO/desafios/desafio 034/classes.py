from abc import ABC

class Funcionario(ABC):

    def __init__(self, nome: str, salario: float):
        self.nome: str = nome
        self.__salario:float = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float):
        if valor < 0:
            raise ValueError("Valor tem que ser maior que 0")

        if valor < self.__salario:
            raise PermissionError("Valor não pode ser menor que o salario!")

        self.__salario = valor


    def calcular_bonus(self):
        pass





class Gerente(Funcionario):
    porcentagem_bonus = 15


    def calcular_bonus(self):
        return self.salario * Gerente.porcentagem_bonus/ 100

    def __str__(self):
        return(f"O {self.nome} é um {__class__.__name__} e ganha R${self.salario} e tem R${self.calcular_bonus():.2f} de bonus")




class Designer(Funcionario):
    porcentagem_bonus = 8


    def calcular_bonus(self):
        return self.salario * Designer.porcentagem_bonus/ 100

    def __str__(self):
        return(f"O {self.nome} é um {__class__.__name__} e ganha R${self.salario} e tem R${self.calcular_bonus():.2f} de bonus")




class Desenvolvedor(Funcionario):
    porcentagem_bonus = 10


    def calcular_bonus(self):
        return self.salario * Desenvolvedor.porcentagem_bonus/ 100

    def __str__(self):
        return(f"O {self.nome} é um {__class__.__name__} e ganha R${self.salario} e tem R${self.calcular_bonus():.2f} de bonus")