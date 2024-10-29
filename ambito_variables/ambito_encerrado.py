def exterior():
    a=50 #a es de ambito local de exterior

    def interior():
        print(a) #interior puede acceder a la variable a de exterior


    interior()


exterior()