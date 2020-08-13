def valores_cuadrado(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

nueva_lista = [10, 25, 50]
valores_cuadrado(nueva_lista)
print(nueva_lista)
