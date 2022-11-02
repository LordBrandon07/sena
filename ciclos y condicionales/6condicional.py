#pida un número al usuario (0 a 365) y diga a qué mes y dia corresponde del año.

n = int(input("introduzca dia del año: "))

if n < 0:
    print("número erroneo")
elif n < 31:
    print("es",n,"de enero")
elif n < 60:
    print("es",n - 31,"de febrero") 
elif n < 91:
    print("es",n - 59,"de marzo") 
elif n < 121:
    print("es",n - 90,"de abril") 
elif n < 152:
    print("es",n - 120,"de mayo") 
elif n < 182:
    print("es",n - 151,"de junio") 
elif n < 213:
    print("es",n - 181,"de julio") 
elif n < 244:
    print("es",n - 212,"de agosto") 
elif n < 274:
    print("es",n - 243,"de septiembre") 
elif n < 305:
    print("es",n - 273,"de octubre") 
elif n < 335:
    print("es",n - 304,"de noviembre") 
elif n < 366:
    print("es",n - 334,"de diciembre") 
elif n > 365:
    print("numero incorrecto")
    
