from abc import ABC

class Pessoa(ABC):
    from datetime import date
    ano_atual = date.today().year


    def __init__(self, nome, nascimento) -> None:
        self._nome:str = nome
        self._nascimento:int = None
        self.nascimento = nascimento

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano) -> None:
        if (Pessoa.ano_atual - 100) <= ano <= Pessoa.ano_atual:
            raise ValueError(f"Ano {ano} é invalido!")
        else:
            self._nascimento = ano


    @property
    def idade(self) -> int:
        return Pessoa.ano_atual - self._nascimento

    @idade.setter
    def idade(self, valor) -> None:
        raise PermissionError("Você não pode alterar a idade ,mude o ano de nascimento!")



class Aluno(Pessoa):

    def __init__(self,nome,nascimento, curso) -> None:
        super().__init__(nome, nascimento)
        self._curso:str = curso
        self.cursos_oficiais:list[str] = ["ADM", "ADS", "ENG", "CONT "]
        if self._curso not in self.cursos_oficiais:
            raise ValueError(f"{self._curso} não esta nos cursos oficiais")


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in self.cursos_oficiais:
            raise ValueError(f"{curso} não esta nos cursos oficiais")
        else:
            self._curso = curso


    def add_curso(self, curso):
        if 3 <= len(curso) <= 5:
            if curso not in self.cursos_oficiais:
                self.cursos_oficiais.append(curso)
            else:
                raise ValueError("O curso ja existe")
        else:
            raise ValueError("O curso deve ter entre 3 a 5 letras")