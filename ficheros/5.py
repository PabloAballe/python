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

        print(' <circle cx="310" cy="160" r="20" stroke="black" stroke-width="20" fill="none" />', file=fichero)



        print(' <circle cx="310" cy="160" r="60" stroke-width="20" stroke="black" fill="none" />', file=fichero)
        print(' <circle cx="310" cy="160" r="100" stroke-width="20" stroke="black" fill="none" />', file=fichero)

        print("</svg>", file=fichero)
        print("</body>", file=fichero)
        print("</html>", file=fichero)

    webbrowser.open(ruta)


if __name__ == "__main__":
    main()
