#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Muestre cuales y cuantos son primos

import random

n = []
c = 0
s = 0



for i in range(1, random.randint(10,25)):
    n.insert(1,int(random.random()*100))
    
for i in n:
    for j in range (1,i+1):
        if i % j == 0:
            c += 1
    if c == 2:
        print(i,"es primo")
        s += 1
    else:
        print(i,"no es primo")
print("cantidad de primos", s)


