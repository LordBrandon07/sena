#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Encuentre la suma y el promedio de los números de la lista

import random

n = []
c = 0
s = 0


def lista(n, c, s):
    for i in range(1, random.randint(10,25)):
        n.insert(1,int(random.random()*100))

    for i in range (len(n)):
        c += 1
        s += n[i]
        p = s // c

    print(n)
    print("la suma de los numeros es: ", s)
    print("el promedio de los numeros es: ",p)
    
lista(n,c,s)