from math import sqrt


def formula():
    lista = []
    try:
        a = float(input("introduzca un numero A: "))
        b = float(input("introduzca un numero B: "))
        c = float(input("introduzca un numero C: "))
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        lista.append([x1, x2])
        print("las soluciones de la ecuacion son: ", lista)
        print(x1)
        print(x2)
    except ZeroDivisionError:
        print("la division por cero no se puede realizar")
    except ValueError:
        print("La ecuación de segundo grado no tiene soluciones!")
    except:
        print("ingrese numeros reales")
        
formula()
