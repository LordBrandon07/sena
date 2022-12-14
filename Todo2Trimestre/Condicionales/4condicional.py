#calificacion de nota

n = float(input("introduzca la nota: "))

if(n<=10 and n>=9):
    print("la nota es perfecta")
elif(n<=8 and n>=7):
    print("la nota es casi perfecta")
elif(n<=6 and n>=5):
    print("la nota es regular")
elif(n<=4 and n>=3):
    print("la nota es mala")
elif(n<=2 and n>=0):
    print("la nota es insuficiente")
else:
    print("nota incorrecta")
