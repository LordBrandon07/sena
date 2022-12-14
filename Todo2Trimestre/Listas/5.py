#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que
#posiciones esta. Si no está agréguelo al final de la lista.

import random

n = []
c = 0
s = 0



for i in range(1, random.randint(10,25)):
    n.insert(1,int(random.random()*100))