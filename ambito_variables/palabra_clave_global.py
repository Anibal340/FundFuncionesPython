y=20

def funcion():
    global y
    y=30
    print(y,"impresion dentro de la funcion")

funcion()
print(y,"impresion fuera de la funcion")