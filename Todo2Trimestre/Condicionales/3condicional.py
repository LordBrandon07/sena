#cantidad de digitos de un numero


n = int(input("introduzca un numero: "))


if(n<=9999 and n>=1000):
    print("el numero tiene 4 digitos")
elif(n<=999 and n>=100):
    print("el numero tiene 3 digitos")
elif(n<=99 and n>=10):
    print("el numero tiene 2 digitos")
elif(n<=9 and n>=0):
    print("el numero tiene 1 digito")
else:
    print("el numero tiene mas de 4 digitos")
    
