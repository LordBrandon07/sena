def try_syntax(numerator, denominator):  #una funcion con dos parametros
    try:
        print(f'In the try block: {numerator}/{denominator}') #forma de hacer el print sin salirse de la cadena
        result = numerator / denominator #variable
    except ZeroDivisionError as zde: #cambio de nombre de la ecepcion
        print(zde)
    else: #si no pasa la excepcion llega a este else
        print('The result is:', result) #resultado de la operacion
        return result #returna 'result' al final de todo el bloque try
    finally: #se ejecuta siempre si esta en el bloque try
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(10, 2)) 