from random import randrange

def main():
    print("JUEGO DE DADOS(2)")
    c1=randrange(1,7)
    c2=randrange(1,7)
    d1=randrange(1,7)
    d2=randrange(1,7)

    print(f"Carmen ha sacado un {c1} y un {c2}")
    print(f"David ha sacado un {d1} y un {d2}")


    david=max(d1, d2)
    barbara=max(c1, c2)

    if david>barbara:
        print("A ganado David")
    elif barbara>david:
        print("A ganado Barbara")
    else:
        pritn("Han empatado")




if __name__ == "__main__":
    main()
