# divisores de un numero

def divisor(n):

    for i in range(1, n+1):
        if n%i==0:
            print("los divisores son:", i)

n = int(input("introduzca un numero: "))

divisor(n)