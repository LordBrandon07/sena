def tipoPalabra(c):
    c = c.lower()
    tildes = ['á','é','í','ó','ú']
    for i in tildes:
        if c[-1] == i or c[-2] == i and c[-1] == 's' or c[-1] == 'n':
            print('Aguda')
tipoPalabra('café')