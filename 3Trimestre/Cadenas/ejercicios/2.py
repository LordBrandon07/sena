# Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto

cadena = input('ingrese una cadena: ')

def sumcad (cadena):
    count = 0

    for i in cadena:
        count += (ord(i))
            
    print('la suma de los codugos da: ',count)
    print('valor numerico de acuerdo al alfabeto',chr(count))    
    
sumcad(cadena)
