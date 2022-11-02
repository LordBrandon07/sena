#multiplos de 5

n = int(input("introduzca un numero: "))

for i in range(1,n+1,1):
    if i % 5 == 0:
        print(i)