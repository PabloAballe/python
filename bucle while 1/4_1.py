def main():
    print("NÚMEROS POSITIVOS")
    numeros=int(input("Escriba la cantidad de numeros positivos a escribir: "))
    positivos=0
    contador=0
    while numeros<=0:
        numeros=int(input("La cantidad debe ser mayor que 0. Intentelo de nuevo: "))

    while positivos<numeros:
        numero=int(input("Escriba un numero: "))
        contador=contador+1

        if numero>=0:
            positivos=positivos+1
    if positivos==1:
        print("Ha escrito 1 numero positivo")
    elif positivos==0:
        print("No ha escrito ningun numero positivo")
    else:
        print(f"Ha escrito {contador} numeros, {positivos} de ellos positivos")


if __name__ == "__main__":
    main()
