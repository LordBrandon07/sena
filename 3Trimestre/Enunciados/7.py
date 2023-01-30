#Crear un programa el cual indique la diferencia entre el valor menor y mayor de un número de 9 dígitos.

n = input('Ingrese un número de 9 dígitos: ')
if len(n) != 9:
    print('El número ingresado no tiene 9 dígitos.')
else:
    n = list(map(int, n)) 
    higher = max(n)
    minor = min(n)
    difference = higher - minor
    print('Valor máximo:', higher)
    print('Valor mínimo:', minor)
    print('Diferencia entre valor máximo y mínimo:', difference)
