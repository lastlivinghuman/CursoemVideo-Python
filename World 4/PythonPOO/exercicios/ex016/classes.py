

class Porta:

    def abrir(self):
        print("girando maçaneta e abrindo a porta")



class Empresa:

    def abrir(self):
        print("Ir ao portal do empreendedor com toda a documentação papelada")


class Ovo:

    def abrir(self):
        print("Quebre o ovo com a faca na frigideira e o espalhe sobre ela")


class Pedra:
    pass



def tentar_abrir(objeto:object):
    try:
        objeto.abrir()
    except:
        print(f"Houve um erro ao tentar abrir {objeto.__class__.__name__}")