#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)

import random

n = []
c = 0
s = 0


def lista(n):
    for i in range(1, random.randint(10,25)):
        n.insert(1,int(random.random()*100))

    print(n)

    for i in range(len(n) -1):
        for j in range(len(n) -1 -i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

    print("de menor a mayor: ",n)

    for i in range (len(n)- 1):
        for j in range(len(n)- 1 - i):
            if n[j] < n [j + 1]:
                n[j], n[j + 1] = n [j + 1], n[j]
    print("de mayor a menor: ", n)
    
lista(n)