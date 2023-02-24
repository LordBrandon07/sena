values = (1, 0) #una tupla
#x,y=19,30      #formas de asignar datos a unas variables en una misma linea
#print(divmod(10,3)) #'divmod'es una operacion en la cual se necesitan dos parametros, los divide y da el cociente y el residuio
try:
    q, r = divmod(*values)  #'*' el asterisco separa los elementos de la tupla
    #print('q=',q) #metodo clasico de hacer el print 
    print(f'q={q}') #forma de hacer el print para tener una cadena, y una variable, sin salirse de esta
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e: #mete varias excepciones en una sola linea, y les cambia el nombre
    print(type(e), e) #muestra el nombre del error