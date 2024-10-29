def exterior():
    a=50 #a es de ambito local de exterior

    def interior():
        nonlocal a
        a=20


    interior()
    print(a)


exterior()