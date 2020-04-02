def main():
    print("MAYOR, MENOR Y MEDIA ARITMÉTICA")
    valores=int(input("Cuantos valores va a introducir?: "))
    mayor=0
    suma=0
    menor=9999999999999
    if valores<=0:
        print("Imposible")
    else:
        for i in range(1,valores+1):
            numero=int(input(f"Escriba el numero {i}: "))
            suma=suma+numero
            if numero>mayor:
                mayor=numero
            elif numero<menor:
                menor=numero

        print(f"El numero mas grande que a introducido es {mayor}")
        print(f"El numero mas pequeño que a introducido es {menor}")
        print(f"La media de los numeros introducidos es {suma/valores}")


if __name__ == "__main__":
    main()
