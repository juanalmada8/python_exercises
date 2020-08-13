def super_funcion (*args, **kwargs):
    total = 0
    for arg in args:
        total+=arg
    print("sumatoria indeterminada es:", total)

    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])


super_funcion(10,50,-1,1.56,nombre="Juan Martin",edad=25)