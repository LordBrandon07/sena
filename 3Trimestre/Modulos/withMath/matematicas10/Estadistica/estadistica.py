def promedio():
    datos=[]
    while True:
        n=int(input("Ingresa los datos : "))
        datos.append(n)
        if n == 0:
            prom=sum(datos)/len(datos)
            print('el promedio es: ', prom)
            break

def mediana():
    lista=[]
    while True:
        n=int(input("Ingresa los datos : "))
        lista.append(n)
        if n == 0:
            for i in range (len(lista)):
                for j in range (i+1,len(lista)):
                    if lista[i] > lista[j]:
                        lista[i],lista[j] = lista[j],lista[i]

                med = int(len(lista))
                if med % 2 == 0:
                    med2 = lista[med//2]
                    med -= 1
                    med1 = lista[med//2]
                    print ("Las medianas son",med1,"y",med2)
                    break
                    
                else:
                    med1 = lista[med//2]
                    print ("La mediana es",med1)
                    break
            break