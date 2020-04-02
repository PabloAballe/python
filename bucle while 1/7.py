def main():
    print("ENTRE DOS VALORES")
    primero=int(input("Escriba un numero: "))
    segundo=int(input(f"Escriba un numero mayor que {primero}: "))
    contador=0

    while segundo<=primero:
        segundo=int(input(f"{segundo} no es mayor que {primero}. Intentelo de nuevo: "))
    while segundo>primero:
        numero=int(input(f"Escriba un numero entre {primero} y {segundo}: "))

        if numero>=primero and numero<=segundo:
            contador=contador+1

        else:
            print(f"Ha escrito {contador} numeros entre {primero} y {segundo}.")
            segundo=primero+segundo






if __name__ == "__main__":
    main()
