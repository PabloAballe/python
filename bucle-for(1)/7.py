def main():
    print("NÚMERO PRIMO")
    numero=int(input("Escriba un numero mayor que 1: "))
    contador=0
    if numero<=1:
        print("Le he pedido un numero entero mayor que 1")
    else:
        for i in range(1, numero+1):
            operacion=numero%i

            if operacion==0:
                contador=contador+1
        if contador==2:
            print(f"El numero {numero} es primo")
        else:
            print(f"El numero {numero} no es primo")



if __name__ == "__main__":
    main()
