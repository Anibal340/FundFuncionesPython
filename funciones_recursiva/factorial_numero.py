def factorial(n):
    """
    
    :param n:
    :return:
    """
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

res_factorial=factorial(2)
print(res_factorial)
