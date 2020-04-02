def main():
    print("NÚMEROS POSITIVOS")
    numeros=int(input("Escriba la cantidad de numeros positivos a escribir: "))
    positivos=0
    negativos=0
    while numeros<=0:
        numeros=int(input("La cantidad debe ser mayor que 0. Intentelo de nuevo: "))

    for _ in range(1, numeros+1):
        numero=int(input("Escriba un numero: "))

        if numero>0:
            positivos=positivos+1
        else:
            negativos=negativos+1
    if negativos==0:
        print(f"Ha escrito {positivos} numeros positivos")
    elif positivos==0:
        print(f"Ha escrito {negativos} numeros negativos")
    else:
        print(f"Ha escrito {positivos} numeros positivos y {negativos} numeros negativos de un total de {numeros}")

if __name__ == "__main__":
    main()
