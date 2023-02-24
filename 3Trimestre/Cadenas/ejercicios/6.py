# Determinar en que tiempo esta conjugado un verbo

cadena = input('ingrese una cadena: ')


def time(cadena):

    cadena = cadena.upper()

    presente = ['AR', 'ER', 'IR', 'NO', 'AN']
    pasado = ['BA', 'IA', 'AMOS', 'VE', 'VO']
    futuro = ['EMOS', 'ERE', 'ERAS', 'ARE', 'RAN']

    for i in presente:
        if cadena.endswith(i):
            print('el verbo esta en presente ')
    for i in pasado:
        if cadena.endswith(i):
            print('el verbo esta en pasado ')
    for i in futuro:
        if cadena.endswith(i):
            print('el verbo esta en futuro ')
        else:
            print('el sistema no supo el tiempo del verbo')

time(cadena)