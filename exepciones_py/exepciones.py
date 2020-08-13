while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Introduce un numero, el valor ingresado no es correcto")
    else:
        print("Todo funciono correctamente")
        break #para frenar el while
    finally:
        print("Fin del while")