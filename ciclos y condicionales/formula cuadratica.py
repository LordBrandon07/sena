#formula cuadratica

a = float(input("introduzca un numero A "))
b = float(input("introduzca un numero B "))
c = float(input("introduzca un numero C "))

x1 = (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
x2 = (-b-(((b**2)-(4*a*c))**0.5))/(2*a)

print("x1 es igaul a: ", x1)
print("x2 es igual a: ", x2)


