from abc import ABC
from operator import index


class Validador(ABC):


    def validar(self):
        pass



class Usuario(Validador):

    def validar(self,usuario:str):
        print(f"{usuario} valido: ", end="")
        if  len(usuario) < 5 or len(usuario) > 20:
            print("Não", end="")
            return

        permitidos = "abcdefghijklmnopqrstuvwxyz0123456789_"
        for caractere in usuario:
            if caractere not in permitidos:
                print("Não", end="")
                return

        else:
            print("sim", )


class Senha(Validador):

    def validar(self,senha:str):

        print(f"{senha} valida: ", end="")
        if len(senha) < 8:
            print("Não", end="")
            return

        maiuscula = False
        numero = False
        simbolo = False

        for caractere in senha:
            if caractere.isupper():
                maiuscula = True
            elif caractere.isnumeric():
                numero = True
            elif not caractere.isalnum():
                simbolo = True

        if simbolo and maiuscula and numero:
            print("Sim")

        else:
            print("Nâp")


class Email(Validador):

    def validar(self, email:str):
        print(f"{email} valido: ",end="")
        if email.count("@") == 1:
            pass
        else:
            print("Não",end="")
            return

        pos_arroba = email.find("@")
        usuario = email[0:pos_arroba]
        if len(usuario) == 0:
            print("Não",end="")
            return

        dominio = email[pos_arroba + 1:]
        pos_ponto = dominio.rfind(".")

        if pos_ponto == -1:
            print("Não", end="")
            return

        extensao = dominio[pos_ponto + 1:]

        if len(extensao) >= 2 and extensao.isalpha():
            print("Sim", end="")
        else:
            print("Não", end="")
            return
def validar_dados(objeto:object , dado):

    try:
        objeto.validar(dado)

    except Exception as e:
        print(f"Erro: {e}")