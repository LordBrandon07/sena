from Datos import *
import csv
list = []
with open('enterprises.csv') as ccc:
    leer = csv.reader(ccc)
    for i in leer:
        a = Datos(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        list.append(a)
        
print(list)
for a in list:
    print(a.others())
    
def EmYo():
    b = Datos