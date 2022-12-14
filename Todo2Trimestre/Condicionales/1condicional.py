#numero del medio

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el segundo número: "))

if n1> n2:
    m = n1
    b = n2
else:
    m = n2
    b = n1
if m > n3:
    m = n3
if m < b:
    m = b

print("el numero del medio es : ", m)