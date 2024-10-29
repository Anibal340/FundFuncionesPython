
def cuadrado(x):
    return x*x

def cubo(x):
    return x**3

def aplicar(funcion,valor):
    return funcion(valor)

resultado=aplicar(cubo,5)
print(resultado)
