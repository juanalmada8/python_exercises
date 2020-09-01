def primer_funcion(lista):
    l = []
    for i in lista:
        l.append((i,i*2))
    return l


lista = [1,2,3]
print(primer_funcion(lista))