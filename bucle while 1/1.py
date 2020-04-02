def main():
    print("NÚMERO MAYOR")
    a=int(input("Escriba un numero: "))
    b=int(input(f"Escriba un numero mayor que {a}: "))

    # condion
    while b<=a:
        b=int(input(f"{b} no es mayor que {a}. Intentelo de nuevo: " ))



if __name__ == "__main__":
    main()
