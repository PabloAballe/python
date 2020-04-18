def main():
    print("DÍGITO DE CONTROL CUENTA CORRIENTE")
    primero=int(input("Escriba el primer digito de la entidad: "))
    segundo=int(input("Escriba el segundo digito de la entidad: "))
    tercero=int(input("Escriba el tercero digito de la entidad: "))
    cuarto=int(input("Escriba el cuarto digito de la entidad: "))

    primero1=int(input("Escriba el primer digito de la entidad: "))
    segundo1=int(input("Escriba el segundo digito de la entidad: "))
    tercero1=int(input("Escriba el tercero digito de la entidad: "))
    cuarto1=int(input("Escriba el cuarto digito de la entidad: "))


    a=primero*4
    b=segundo*8
    c=tercero*5
    d=cuarto*10


    a1=primero1*9
    b1=segundo1*7
    c1=tercero1*3
    d1=cuarto1*6


    suma=a+b+c+d+a1+b1+c1+d1

    div=suma%11

    digito=11-div

    if primero  or  segundo  or tercero or cuarto or primero1 or segundo1 or tercero1 or cuarto1<0:
        print("Lo siento no ha escrito correctamente os digitos")
    elif primero or segundo or tercero or cuarto or primero1 or segundo1 or tercero1 or cuarto1>9:
        print("Lo siento no ha escrito correctamente os digitos")
    else:
        print(f"El digito de control es {digito}")


    print("Porgrama terminado")


if __name__ == "__main__":
    main()
