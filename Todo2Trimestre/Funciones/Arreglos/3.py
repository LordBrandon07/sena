#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Sume los pares y saque el promedio de los impares

import random

n = []
c = 0
s = 0
p = []
sp = 0
im = []
sim = 0
def lista (n, p, sp, im, sim):
    for i in range(1, random.randint(10,25)):
        n.insert(i,round(random.random()*100))

    print(n)
        

    for i in range(len(n)):
        if n[i] % 2 == 0:
            p.append (n[i])
            sp += n[i]
        else:
            im.append (n[i])
            sim += n[i]

    print("cantidad de pares:",p,"\n la suma de los pares es de:", sp)
    print("cantidad de impares:",im,"\n el promedio de impares es de:", sim // len(im))

lista(n, p, sp, im, sim)