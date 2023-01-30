#solicitar  2 nombres y edad, para  calcular si es mayor de edad o menor para entrar al concierto, si no cumple con esta saldrá un mensaje que dirá no fue admitido para entrar al concierto.
# también, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra o si terminan con la misma letra. Si no es así, imprimir no hay coincidencia.

def coincidence (name1, name2):
    if name1[0] == name2[0] or name1[-1] == name2[-1]:
        print('coincidencia')
    else:
        print('no hay coincidencia')


name1 = input('ingrese un nombre: ')
years1 = int(input ('ingrese la edad: '))
name2 = input('ingrese un nombre: ')
years2 = int(input ('ingrese la edad: '))

if years1 < 18:
    print(name1, 'no fue admitido para entrar al concierto.')
else: 
    print(name1 ,'fue admitido para entrar al concierto.')
    
if years2 < 18:
    print(name2, 'no fue admitido para entrar al concierto.')
else: 
    print(name2 ,'fue admitido para entrar al concierto.')

coincidence(name1, name2)
    
