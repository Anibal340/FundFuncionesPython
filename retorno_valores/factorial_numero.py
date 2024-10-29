def factorial(n):
    """
    Funcion que calcula el factorial de un numero no negativo

    :param n: (int) Numero entero no negativo
    :return: (int) El factorial de n.
    :raises RecursionError: Si n es un numero  negativo
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


res_factorial = factorial(2)
print(res_factorial)

help(factorial)