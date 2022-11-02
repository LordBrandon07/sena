#numero positivos


i = 1
c = 0

while True:
    n = int(input("introduzca un numero: "))
    if n <= -1:
        break
    c += 1

print("la cantidad de numeros postivos ingresados son", c)
