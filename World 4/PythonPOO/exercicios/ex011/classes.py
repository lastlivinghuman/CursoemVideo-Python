from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nome:str=""):
        self.nome:str = nome


    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} e esta emitindo som!")



class Dog(Animal):

    def emitir_som(self):
        print(f"{self.nome} esta dizendo, !AU, AU, AU! ")


class Pitbull(Dog):

    def emitir_som(self):
        print(f"{self.nome} esta dizendo, !ROF,ROF,ROF! ")


class Cat(Animal):


    def emitir_som(self, nome:str):
        print(f"{self.nome} esta dizendo !MIAU, MIAU!")


class Chiken(Animal):

    def emitir_som(self):
        print(f"{self.nome} esta dizendo !PO PO PO !")