from random import randrange
import webbrowser


def main():
    ruta = "1.html"

    numero=randrange(1,8)
    with open(ruta, mode="w", encoding="utf-8") as fichero:
        print("<!DOCTYPE html>", file=fichero)
        print('<html lang="es">', file=fichero)
        print("<head>", file=fichero)
        print('  <meta charset="utf-8">', file=fichero)
        print("  <title>Primera web con python</title>", file=fichero)
        print(
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
            file=fichero,
        )
        print("</head>", file=fichero)
        print("", file=fichero)
        print("<body>", file=fichero)
        print(f"  <p>Hola {numero}</p>", file=fichero)
        print("</body>", file=fichero)
        print("</html>", file=fichero)

    webbrowser.open(ruta)


if __name__ == "__main__":
    main()
