from random import randrange

def main():
    print("JUEGO DE DADOS (3)")

    e1=randrange(1,7)
    e2=randrange(1,7)
    f1=randrange(1,7)
    f2=randrange(1,7)

    elena=max(e1, e2)
    fernando=max(f1, f2)


    em=min(e1, e2)
    fm=min(f1, f2)

    print(f"Elena a sacado un {e1} y un {e2} ")
    print(f"Fernando a sacado un {f1} y un {f2}")


    if elena>fernando:
        print("Ha ganado Elena")
    elif fernando>elena:
        print("Ha ganado fernando")

    else:
        if em>fm:
            print("Ha ganado Elena")
        elif fm>em:
            print("Ha ganado Fernando")
        else:
            print("Han empatado")




if __name__ == "__main__":
    main()
