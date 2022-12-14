# divisores de un numero

n = int(input("introduzca un numero: "))

for i in range(1, n+1):
    if n%i==0:
        print("los divisores son:", i)
