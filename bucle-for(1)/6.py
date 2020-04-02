def main():
    print("CONTADOR DE PARES E IMPARES")
    valores=int(input("Cuantos valores va a introducir?: "))
    par=0
    impar=0
    if valores<=0:
        print("Imposible")
    else:
        for i in range(1, valores+1):
            numero=int(input(f"Escriba el valor {i}: "))
            operacion=numero%2

            if operacion==0:
                par=par+1
            else:
                impar=impar+1
        print(f"Ha escrito {par} numeros pares y {impar} numeros impares")
        print("Gracias por su colaboracion")


if __name__ == "__main__":
    main()
