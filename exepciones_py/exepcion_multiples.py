while(True):
    try:
        n = float(input("Introduce un numero: "))
        5 / n
        break
    except TypeError:
        print("No se puede dividir un nro con un string")
    #except Exception as e: --> para sacar el tipo de error
    except ValueError:
        print("Introducir cadena que sea un numero")
    except ZeroDivisionError:
        print("No se puede diidir un numero por cero")
