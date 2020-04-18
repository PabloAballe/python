import webbrowser

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
        print('<body style="background-color:green">', file=fichero)

        print('<h1 style="color:red; font-size: 400px">Hola mundo</h1>', file=fichero)




        print("</body>", file=fichero)
        print("</html>", file=fichero)

    webbrowser.open(ruta)


if __name__ == "__main__":
    main()
