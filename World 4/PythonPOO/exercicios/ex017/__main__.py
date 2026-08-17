from classes import *


def main():
    a = Numero(3)
    b = Casa()
    c = Papel()
    d = Lista([1,2,3])

    tentar_dobrar(a)
    tentar_dobrar(b)
    tentar_dobrar(c)
    tentar_dobrar(d)

    print(a)
    print(b)
    print(c)
    print(d)

if __name__ == "__main__":
    main()