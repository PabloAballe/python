def main():
    print("MAYORES QUE EL ANTERIOR")
    valores=int(input("Cuantos valores va  aintroducir?? "))

    if valores<=1:
        print("Imposible!")
    else:
        numero=int(input("Escriba un número: "))
        for _ in range(1,valores):
            segundo=int(input(f"Escriba un numero mas grande que {numero}: "))


            if numero>=segundo:
                print(f"{segundo} no es mayor que {numero} ")
            numero=segundo

        print("Gracias por su coolaboracion!!")




if __name__ == "__main__":
    main()
