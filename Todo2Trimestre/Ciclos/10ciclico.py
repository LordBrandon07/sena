# M.C.D.

n1 = int(input("introduzca un numero: "))
n2 = int(input("introduzca un numero: "))

while n1 % n2 != 0:
    mcd = n1 % n2
    n1 = n2
    n2 = mcd
    
print(n2)                                                                                                                                                                                              