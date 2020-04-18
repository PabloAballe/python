from random import randrange

def main():
    print("PRIMER PROGRAMA")

    for i in range(1, 11):
        print(f"{i*2}", end=" ")
    print()


    for i in range(20, 36,2):
        print(f"{i}", end=" ")

    print()


    for i in range(10, 31, 4):
        print(f"{i}", end=" ")
    print()


    for i in range(40, -1, -5):
        print(f"{i}", end=" ")
    print()

    for i in range(1, 11, 1):
        print(i, end=" ")
    print()
    print("PROGRAMA TERMINADO CON EXITO")



if __name__ == "__main__":
    main()
