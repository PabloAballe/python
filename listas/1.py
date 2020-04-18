def main():
    palabras=int(input("Digame cuantas palabras tiene la lista: "))
    lista =[]
    if palabras<=0:
        print("Esto es imposible")

    else:
        for i in range(1, palabras+1):
            cuenta=input(f"Digame la palabra {i}: ")
            lista.append(cuenta)

        limpieza=", ".join(lista)

        print(f"La lista creada es: {limpieza} ")


if __name__ == "__main__":
    main()
