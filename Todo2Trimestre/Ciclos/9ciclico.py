#exponente sin pow

n = int(input("introduzca un numero: "))
p = int(input("introduzca la potencia: "))

pi = p
e = n

while p>1:
    e *= n
    p -= 1
    
print("el numero", n,"elevado a", pi, "es", e)

