from random import randrange

def main():
    print("JUEGO DE DADOS")
    alberto=randrange(1,7)
    barbara=randrange(1,7)


    print(f"Alberto a sacado un {alberto}")
    print(f"Barbara ha sacado un {barbara}")
    if alberto>barbara:
        print("Alberto es el ganador")
    elif barbara>alberto:
        print("Barbara es la ganadora")
    else:
        print("Han empatado")



if __name__ == "__main__":
    main()
