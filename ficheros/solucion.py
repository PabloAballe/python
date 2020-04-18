import webbrowser


def main():
    ruta = "svg-ficheros-3-1-1.html"

    with open(ruta, mode="w", encoding="utf-8") as fichero:
        print("<!DOCTYPE html>", file=fichero)
        print('<html lang="es">', file=fichero)
        print("<head>", file=fichero)
        print('  <meta charset="utf-8">', file=fichero)
        print("  <title>Ficheros (3) 1-1. SVG. Ejercicios. Python</title>", file=fichero)
        print('  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
              file=fichero)
        print("</head>", file=fichero)
        print("", file=fichero)
        print("<body>", file=fichero)
        print('  <svg version="1.1" xmlns="http://www.w3.org/2000/svg"', file=fichero)
        print('    width="620" height="320" viewBox="-10 -10 620 320"', file=fichero)
        print('    style="border: black 1px solid">', file=fichero)
        for i in range(4):
            for j in range(11):
                print(f'    <circle cx="{30 * j}" cy="{30 * i}" r="5" fill="black" />',
                      file=fichero)
        print(" </svg>", file=fichero)
        print("</body>", file=fichero)
        print("</html>", file=fichero)

    webbrowser.open(ruta)


if __name__ == "__main__":
    main()
