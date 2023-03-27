import sqlite3  
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db') #crea una coneccion con la base datos 'ruta absoluta'
con=sqlite3.connect('conpython.db') #crea una coneccion con la base datos 'ruta relativa'
print(type(con)) #imprime que tipo de objeto es 'con'
micursor=con.cursor() #crea el cursor para manipular la base de datos
print(type(micursor))
sentencia="SELECT * from alumno;" #crea una sentencia sql
micursor.execute(sentencia) #ejecuta la sentencia
for fila in micursor.fetchall(): #bucle que recorre las filas de la base datos, y con fetchall imprime todas las filas
    print(fila[0]) #imprime el indice 0 de todas las filas
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)