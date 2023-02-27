def edad():
    try:
        tuedad=int(input("introduce tu edad")) # un input que pide un entero
        print(f'tu edad es  {tuedad}') # una impresion de la cadena anterior
        #print('Tu edad es ',tuedad)
    except ValueError as e:   # cambia el nombre del error
        print(e) #imprime el nombre del error
        print("La edad debe ser un valor numerico...")
        edad() #vuelve a llamar la funcion y crea un bucle, hasta dar un dato correcto
    else: #si no pasa la excepcion llega a este else
        print('Viene por el else')

edad()