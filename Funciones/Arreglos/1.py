# Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
# del promedio o es igual al promedio de todos los números de la lista.


import random

n = []
c = 0
s = 0
p = 0

def lista(n, c, s, p):
    for i in range(random.randint(10,25)):
        n.insert(0,int(random.random()*100))

    for i in range(len(n)):
        c += 1
        s += n[i]
        p = s // c
        
        
    print("el promedio es: ",p)
    for i in n:
        if i > p:
            print(i, "el numero es mayor al promedio")
        elif i < p:
            print(i, "el numero es menor al promedio")
        else:
            print(i, "el numero es igual al promedio")

lista(n, c, s, p)