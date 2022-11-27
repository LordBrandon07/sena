#paga de obrero

def paga(p, s, e):
    if(p<=40):
        print("la paga es de ", s )
    else:
        s = 40* 2600
        print("la paga es", (s + e))

p = float(input("introduzca horas trabajadas: "))
s = p * 2600
e = (p - 40) * 5000

paga(p, s, e)