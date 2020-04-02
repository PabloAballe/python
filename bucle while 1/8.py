def main():
    print("CUENTA PARES (1)")
    numero=int(input("Escriba un numero par: "))
    par=0
    while numero%2!=0:
        numero=int(input(f"{numero} no es un numero par. Intentelo de nuevo: "))
    while numero%2==0:
        par=par+1
        pregunta=input("Quieres escribir otro numero par? (S/N): ")
        if pregunta.lower()=="s":
             numero=int(input("Escriba un numero par: "))
             while numero%2!=0:
                 numero=int(input(f"{numero} no es un numero par. Intentelo de nuevo: "))

        else:
             print(f"Ha escrito {par} numeros pares.")



if __name__ == "__main__":
    main()
