#salida en orden descendente 

def orden(n):
    for i in range (n):
        for j in range(1, n+1):
            print(j,"",end="")
        n -= 1
        print ("")

n = int(input("introduzca un numero: "))

orden(n)