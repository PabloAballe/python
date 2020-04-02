def main():
    print("HASTA EL LÍMITE")
    cuenta=0
    limite=float(input("Escriba el valor limite: "))

    while limite<=0:
        limite=float(input("El limite debe ser mayor que 0. Intentelo de nuevo: "))

    while cuenta<limite:
        numero=float(input("Escriba un numero: "))
        cuenta=cuenta+numero
    print(f"Ha superado el limite. La suma de los numeros introducidos es {cuenta}")



if __name__ == "__main__":
    main()
