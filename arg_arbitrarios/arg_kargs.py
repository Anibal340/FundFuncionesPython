def funcion_combinada(*args,**kwargs):
    print("argumentos posicionales",args)
    print("Argumentos palabra clave:",kwargs)


funcion_combinada(1,2,3,nombre="Juan",edad=25)
