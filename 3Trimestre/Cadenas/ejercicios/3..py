# cuantas veces se repite un caracter dado

def rep ():
    cadena = input('ingrese una cadena: ')
    caracter = input('ingrese el carecter: ')

    count = 0

    for i in cadena:
        if i == caracter:
            count += 1
            
    print(count)
    
rep()