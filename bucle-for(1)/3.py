from random import *

def main():
    print("MAYORES QUE EL PRIMERO")
    valores=int(input("Cuantos valores va a introducir: "))

    if valores<=0:
        print("Imposible!")
    else:
        numero=int(input("Escriba un numero: "))
        for _ in range(1,valores):
            segundo=int(input(f"Escriba un numero mas grande que {numero}: "))

            if segundo<numero:
                print(f"{segundo} no es mayor que {numero}!")

        print("Gracias por su coolaboracion!")



if __name__ == "__main__":
    main()
