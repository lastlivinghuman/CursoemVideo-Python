from abc import ABC
from operator import index
import re 

class Validador(ABC):


    def validar(self):
        pass



class Usuario(Validador):

    def validar(self,usuario:str):
        print(f"{usuario} valido:  ", end="")
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex,usuario):
            print("Sim")
            
        else:
            print("Não")
        # if  len(usuario) < 5 or len(usuario) > 20:
        #     print("Não", end="")
        #     return

        # permitidos = "abcdefghijklmnopqrstuvwxyz0123456789_"
        # for caractere in usuario:
        #     if caractere not in permitidos:
        #         print("Não", end="")
        #         return

        # else:
        #     print("sim", )


class Senha(Validador):

    def validar(self,senha:str):

        print(f"{senha} valida: ",end="" )
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%?]).{8,} $"
        if re.fullmatch(regex,senha):
            print("Sim")
        else:
            print("Não")
 

class Email(Validador):

    def validar(self, email:str):
        print(f"{email} valido: ",end="")
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
        if re.fullmatch(regex, email):
            print("Sim")
        else:
            print("Não")

def validar_dados(objeto:object , dado):

    try:
        objeto.validar(dado)

    except Exception as e:
        print(f"Erro: {e}")