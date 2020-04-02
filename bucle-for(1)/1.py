from random import *

def main():
    print("Pares e impares!!")
    numero=int(input("Escriba un numero entero: "))
    segundo=int(input(f"Escriba un numero mayor o igual que {numero}: "))


    if segundo<numero:
        print(f"Le he pedido un numero mayor o igual que {numero}")

    else:
        for i in range(numero,segundo+1):
            print(f"El numero {i} es " ,end="")
            if i%2==0:
                print("par")
            else:
                print("impar")



if __name__ == "__main__":
    main()
