# numeros al reves

n = int(input("introduzca un numero: "))

i = 0

while n > 0:
    r = n % 10
    i = (i*10) + r
    n //=10
    
print("el inverso es", i)