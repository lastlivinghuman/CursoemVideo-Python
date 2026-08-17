from hashlib import sha256



class ContaBancaria:

    def __init__(self, id: int, nome: str, saldo: float=100, chave=None) -> None:
        self._titular:str = nome
        self._id:int = id
        self.__saldo:float = saldo
        if chave is not None:
            self.__hash = sha256(chave.encode()).hexdigest()
        else:
            self.__hash = self.pede_senha()

        print(f"Conta {self._id} criada com sucesso. Com saldo disponivel de R${self.__saldo }")


    #Pede a senha para o usuario
    def pede_senha(self) -> str:
        from pwinput import pwinput
        while true:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        senha = self.criptografar(senha)
        return senha
    
    # VAlida a senha passado pelo usuario
    def validar_senha(self,chave) -> bool:
        hash_chave = self.criptografar(chave)
        if hash_chave == self.__hash:
            return True
        else:
            return False

    # Deposita um valor
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor


    # Saca um valor
    def sacar(self, valor , chave=None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        else:
            chave = self.criptografar(chave)

        if self.validar_senha(chave):
            print("Senha correta")
            if valor > self.__saldo:
                print("O valor de saque desejado não esta disponivel!")
            else:
                self.__saldo -= valor
                print(f"Saque de {valor} autorizado!")
        else:
            print("Senha incorreta")


    #Criptografa a string passada
    @staticmethod
    def criptografar(chave) -> str:
        return sha256(chave.encode()).hexdigest()


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = nome
        else:
            print("senha incorreta")

