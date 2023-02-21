# Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez.

cadena = input('ingrese una cadena: ')

def alfabeto(cadena):
    cad = ''
    for i in cadena:
        if i not in cad:
            cad += i
    return len(cad)


print(alfabeto(cadena))