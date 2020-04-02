def main():
    print("NÚMEROS NEGATIVOS")
    valores=int(input("Cuantos valores va a introducir?: "))
    contador=0
    if valores<0:
        print("Imposible")
    elif valores==0:
        print("No ha escrito ningun numero negativo")
    else:
        for i in range(1, valores+1):
            primero=int(input(f"Escriba el numero {i}: "))
            i=i+1

            if primero<0:
                contador=contador+1
        print(f"Ha escrito {contador} numeros negativos")



if __name__ == "__main__":
    main()
