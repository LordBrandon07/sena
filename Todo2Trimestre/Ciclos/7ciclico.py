#suma mayor a un numero natural

n = int(input("introduzca un numero: "))

a = 0

for i in range (1, n, 1):
    print (i)
    a += i
    if a > n :
        break
    
print("la suma es", a) 