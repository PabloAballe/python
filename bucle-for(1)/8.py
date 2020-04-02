def main():
    print("SUMA DE VALORES")
    valores=int(input("Cuantos valores va a introducir?: "))
    suma=0
    if valores<=0:
        print("Imposible")
    else:
        for i in range(1,valores+1):
            numero=float(input(f"Escriba el numero {i}: "))
            suma=suma+numero

        print(f"La suma de tus numeros es {suma}")


if __name__ == "__main__":
    main()
