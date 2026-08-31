from classes import *


def main():
    u = [
        Usuario("pedro", "pedro@gmail.com"),
        Aluno("dan", "ADM",16)
    ]

    exportar_dados(XML(), u)


if __name__ == "__main__":
    main()