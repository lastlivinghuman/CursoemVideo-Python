from classes import *



def main():
    p1 = Produto("Mouse",325)
    p2 = Produto("Teclado", 244)
    c1 = Carrinho()
    c2 = Carrinho()
    c1 = p1 + p2
    c2 = c2 + c1
    print(c2)



if __name__ == "__main__":
    main()