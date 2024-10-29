def operaciones_basicas(a,b):
    """
    Realiza operaciones basicas entre dos numeros.
    :param a: (int o float) primer numero
    :param b: (int o float) segundo numero
    :return: Una tupla con los resultados de las operaciones
            -suma(int o float) suma de a y b
            -resta(int o float) suma de a y b
            -multiplicacion(int o float) suma de a y b
            -division(float) cociente de a dividido por b (si b no es cero)
    """
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return suma,resta,multiplicacion,division

resultado=operaciones_basicas(8,4)
print(resultado)

#help(operaciones_basicas)
print(operaciones_basicas.__doc__)