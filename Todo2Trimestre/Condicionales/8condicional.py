#costos llamada telefonica

t = float(input("introduzca duracion de la llamada en minutos: "))
b = 200
n = (((t - 3)*50 + b)+(-1*t))

if(t<=3):
    print("el costo de la llamada es de", b )
else:
    print("el costo de la llamada es dela paga es", (t + n))

