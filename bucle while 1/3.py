def main():
    print("CADA VEZ MÁS GRANDES")
    primero=int(input("Escriba un numero: "))
    segundo=int(input(f"Escriba un numero mayor que {primero}: "))

    if segundo<=primero:
        print(f"{segundo} no es mayor que {primero}")
    else:
        while segundo>primero:
            primero=segundo
            segundo=int(input(f"Escriba un numero mayor que {primero}: "))

            if segundo<=primero:
                print()
                print(f"{segundo} no es mayor que {primero}")

if __name__ == "__main__":
    main()
