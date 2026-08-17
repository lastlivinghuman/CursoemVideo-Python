from classes import *


def main():
    c1 = Carteira(120)
    print(c1)
    c2 = Carteira(100)
    c2 += 20
    if (c1 == c2):
        print("As carteiras possuem valores iguais")
    else:
        print("Valores diferentes")


if __name__ == "__main__":
    main()