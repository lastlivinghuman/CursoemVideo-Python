class Retangulo:

    def __init__(self, altura= 1, base= 8):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura


    #getter base
    @property
    def base(self):
        return self._base


    # setter base
    @base.setter
    def base(self,valor):
        if not isinstance(valor,int) and  isinstance(valor, float):
            raise ValueError("Base tem que ser um valor numerico!")

        if valor < 0:
            raise ValueError("Valor deve ser maior que 0")
        else:
            self._base = valor



    #getter altura
    @property
    def altura(self):
        return self._altura


    #setter altura
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, int) and isinstance(valor, float):
            raise ValueError("Altura tem que ser um valor numerico!")

        if valor < 0:
            raise ValueError("Valor deve ser maior que 0")
        else:
            self._altura = valor


    #getter area
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    #setter area
    @area.setter
    def area(self, valor):
        raise PermissionError("Area não pode ser mudada dessa forma")


    # getter medidas
    @property
    def medidas(self):
        return f"Base: {self._base} \nAltura: {self._altura} \nÁrea: {self.area}"


    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise SyntaxError("Voce precisa passar uma tupla!")

        if len(valores) != 2:
            raise ValueError("Voce precisa passar 2 valores na tupla!")
        else:
            if isinstance(valores[0], int) or isinstance(valores[0], float):
                self.base = valores[0]
            else:
                print("A base precisa ser numerica ")
            if isinstance(valores[1], int) or isinstance(valores[1], float):
                self.altura = valores[1]
            else:
                print("A altura precisa ser numerica ")