import webbrowser
from random import randrange

def main():
    ruta = "1.html"

    with open(ruta, mode="w", encoding="utf-8") as fichero:
        print("<!DOCTYPE html>", file=fichero)
        print('<html lang="es">', file=fichero)
        print("<head>", file=fichero)
        print('  <meta charset="utf-8">', file=fichero)
        print("  <title>Ficheros (3). SVG. Ejercicios. Python</title>", file=fichero)
        print('  <meta name="viewport" content="width=device-width, initial-scale=1.0">',file=fichero)
        print("</head>", file=fichero)
        print("<body>", file=fichero)
        print('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="620" height="320" viewBox="-10 -10 620 320" style="border: black 1px solid">',file=fichero)

        print('<line x1="0" y1="10" x2="1000" y2="11" stroke-width="2" stroke="Red"/>', file=fichero)
        print('<line x1="10" y1="0" x2="10" y2="1000" stroke-width="2" stroke="Red"/>', file=fichero)



        print("</svg>", file=fichero)
        print("</body>", file=fichero)
        print("</html>", file=fichero)

    webbrowser.open(ruta)


if __name__ == "__main__":
    main()
