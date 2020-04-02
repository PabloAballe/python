def main():
    print("SUMA ENTRE VALORES")
    numero=int(input("Escriba un numero entero positivo: "))
    suma=0
    if numero<=0:
        print("Imposible")
    else:
        mayor=int(input(f"Escriba un numero entero mayor que {numero}: "))

        if numero>=mayor:
            print(f"Le he pedido un numero entero mayor que {numero}")
        else:
            for i in range(numero, mayor+1):
                suma=suma+i
            print(f"La suma desde {numero} hasta {mayor} es {suma}")


if __name__ == "__main__":
    main()
