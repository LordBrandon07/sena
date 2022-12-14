#un segundo despues

h = int(input("introduzca la hora: "))
m = int(input("introduzca los minutos: "))
s = int(input("introduzca los segundos: "))

h1 = h + 1
m1 = m + 1
s1 = s + 1

s1r = s1 % 60
m1r = m1 % 60

if (h<=23 and h>0 and m<=60 and m>=0 and s<=60) and s>=0:
    print("la hora un segundo despues es: ", h1, ":", m1r,":", s1r)
else:
    print("datos incorrectos")