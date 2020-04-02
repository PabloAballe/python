def main():
    print("SUMA DE NÚMEROS")
    contador=0
    numero=int(input("Escriba un numero: "))

    while numero>=0:
        contador=contador+numero
        numero=int(input("Escriba un numero: "))

    if numero<0:
        print(f"La suma de los numeros positivos introducidos es {contador}")







if __name__ == "__main__":
    main()
