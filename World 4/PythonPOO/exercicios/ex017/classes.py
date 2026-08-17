class Numero:


    def __init__(self, valor:int):
        self.valor = valor


    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o numero {self.valor}"

class Casa:

    def dobrar(self):
        raise PermissionError

    def __str__(self):
        return "Uma mansão????"



class Papel:

    def __init__(self):
        self.dobrado = False


    def dobrar(self):
        self.dobrado = True


    def __str__(self):
        return f"O papel esta ? {self.dobrado}"




class Lista:

    def __init__(self, lista:list[int]):
        self.lista:list[int] = lista


    def dobrar(self):
        self.lista += self.lista


    def __str__(self):
        return f"Tenho a lista {self.lista}"



#DUCK TYPYNG

def tentar_dobrar(objeto:object):

    try:
        objeto.dobrar()

    except:
        print(f"Houve um erro ao tentar dobrar {objeto.__class__.__name__}")