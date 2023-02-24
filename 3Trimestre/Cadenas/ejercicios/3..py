# cuantas veces se repite un caracter dado

cadena = input('ingrese una cadena: ')
caracter = input('ingrese el carecter: ')

def rep (cadena, caracter):


    count = 0

    for i in cadena:
        if i == caracter:
            count += 1
            
    print(count)
    
rep(cadena, caracter)