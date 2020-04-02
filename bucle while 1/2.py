def main():
    print("NÚMEROS MAYORES")
    primero=float(input("Escriba un numero: "))
    segundo=float(input(f"Escriba un numero mayor que {primero}: "))

    if segundo<=primero:
        print(f"{segundo} no es mayor que {primero}")
    else:
        while segundo>primero:
            segundo=float(input(f"Escriba otro numero mayor que {primero}"))
        if segundo<=primero:
            print(f"{segundo} no es mayor que {primero}")


if __name__ == "__main__":
    main()
