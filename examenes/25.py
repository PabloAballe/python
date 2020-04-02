from random import randrange

def main():
    print("JUEGO DADO A TIERRA")
    print("Cubitus: ", end="")
    c=randrange(1,101)
    c2=randrange(1,101)
    print(c ,end=" ")
    ccont=0
    hcont=0
    while c2 < c:
        print(c2, end=" ")
        c2=randrange(1,101)
        ccont=ccont+1
    print()
    print("Humerus: ", end="")
    h=randrange(1,101)
    h2=randrange(1,101)
    print(h, end=" ")

    while h2 < h:
        print(h2, end=" ")
        h2=randrange(1,101)
        hcont=hcont+1

    print()

    if ccont>hcont:
        print("Ha ganado Cubitus")
    elif hcont>ccont:
        print("Ha ganado Humerus")
    else:
        print("Han empatado")







if __name__ == "__main__":
    main()
