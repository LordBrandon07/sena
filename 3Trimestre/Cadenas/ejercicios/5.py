# Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula

cadena = input('ingrese una cadena: ')

if cadena.find('é', -2):
    print('es aguda')
    
elif not cadena.endswith('n'):
    print('grave')
else:
    print('other')