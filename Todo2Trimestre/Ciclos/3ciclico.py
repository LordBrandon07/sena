#el numero es perfecto

n = int(input("introduzca un numero: "))

i = 1
a = 0

while(i<n):
    if n%i == 0:
        a += i
    i += 1

if a == n:
    print("el numero es perfecto")
else:
    print("el numero no es perfecto")
