from random import randrange

def main():
    print("SOLITARIO DE DADOS")
    print()
    print("Tirada: ", end="")
    dado=randrange(1,7)
    contador=0
    print(dado, end=" ")
    while dado%2==0:
        dado=randrange(1,7)
        print(dado, end=" ")

        contador=contador+1

    print()

    if contador>1:
        print(f"Ha obtenido {contador} numeros pares")
    elif contador==1:
        printf(f"Ha obtenido 1 numero par")
    else:
        print("No ha obtenido ningun numero par")

if __name__ == "__main__":
    main()
