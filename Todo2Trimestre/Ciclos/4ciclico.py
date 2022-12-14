#cuantos numeros perfectos hay entre 1 a 1000

c = 0

for n in range (1, 1001):
    a = 0
    for i in range (1, n):
    
        if n%i == 0:
            a += i
    if a == n:
        c += 1
        print("el numero",n, "es perfecto")
            
print("total de numeros perfectos", c)
    
    