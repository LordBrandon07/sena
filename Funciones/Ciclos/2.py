# numero primo o no

n = int(input("introduzca un numero: "))

def primo(n):
    v = range(2, n)
    c = 0
    
    for i in v:
        if n % i == 0:
            c += 1

    if c > 0:
        print("el numero no es primo")
    else:
        print("el numero es primo")

primo(n)