# Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última

cadena = input('ingrese una cadena: ')

def sub(cadena):
    word = len(cadena)
    count = -1
    for i in range (word):
        su = cadena [:2 + count]
        count += 1
        print(su)

sub(cadena)