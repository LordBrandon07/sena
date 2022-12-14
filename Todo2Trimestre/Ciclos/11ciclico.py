# cociente y residuo

d1 = int(input("introduzca un numero(dividiendo): "))
d2 = int(input("introduzca un numero(divisor): "))

c = 0

while d1 >= d2:
    d1 -= d2
    c += 1
    
print("el residuo es", d1)
print("el cociente es", c)