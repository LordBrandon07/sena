#paga de obrero

p = float(input("introduzca horas trabajadas: "))
s = p * 2600
e = (p - 40) * 5000

if(p<=40):
    print("la paga es de ", s )
else:
    s = 40* 2600
    print("la paga es", (s + e))
