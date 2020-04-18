def main():
    print("CÁLCULO DEL DÍA DE LA SEMANA")
    dia=int(input("Escriba el numero de dias: "))
    mes=int(input("Escriba el numero de mes: "))
    año=int(input("Escriba el numero de año(a partir de 1583): "))


    if año<1583:
        print("Le he pedido un año posterior a 1582")

    else:
        a=(14-mes)/año
        b=año-a
        c=mes+((a*12)-2)
        d=b/4
        e=b/100
        f=b/400
        g=(c*31)/12
        h=dia+b+d-e+f+g
        i=h%7
        resultado=""

        if i==0:
            resultado="Domingo"
        elif i==1:
            resultado="Lunes"
        elif i==2:
            resultado="Martes"
        elif i==3:
            resultado="Miercoles"
        elif i==4:
            resultado="Jueves"
        elif i==5:
            resultado="Viernes"
        else:
            resultado="Sabado"





        print(f"El dia {dia} del mes {mes} de {año} es {resultado}")

if __name__ == "__main__":
    main()
