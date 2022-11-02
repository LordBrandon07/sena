#cuantos numeros primos hay entre 1 y 1000

n = 1

while n <=1000:
    c = 1
    a = 0
    while c <= n:
        if n % c == 0:
            a += 1
        c += 1
    if a == 2:
        print(n)
        
    n += 1


