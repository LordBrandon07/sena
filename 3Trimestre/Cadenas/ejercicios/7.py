#  De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

cadena = input('ingrese una cadena: ')

def tipos(cadena):
    vocales = 0
    consonantes = 0
    tilde = 0
    caracteres = 0
    
    cadena = cadena.upper()
    
    for i in cadena:
        if i.isalpha():
            if i in 'AEIOU':
                vocales +=1
            elif i in 'ÁÉÍÓÚ':
                tilde += 1
            else:
                consonantes += 1
            
        if i not in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ':
            caracteres += 1
    print(cadena)
    print('vocales: ',vocales,'\nvocales con tilde: ',tilde,'\nconsonantes: ',consonantes,'\ncaracteres: ',caracteres)

tipos(cadena)
