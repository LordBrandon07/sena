# Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

cadena = input('ingrese una cadena: ')

def maymin (cadena):

    print(cadena.upper())
    print(cadena.lower())
    print(cadena.capitalize())
    print(cadena.title())
    print(cadena.swapcase())
    
    
maymin(cadena)