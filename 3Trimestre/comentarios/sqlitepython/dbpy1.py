import sqlite3
with sqlite3.connect('conpython.db')as con: #crea una coneccion con la base datos 'ruta relativa', con un bloque de codigo 'with' y le pone el nombre 'con'
    micursor=con.cursor() #crea el cursor para manipular la base de datos
    sentencia="SELECT nombre,apellido FROM alumno;" #crea una sentencia sql
    print(micursor.execute(sentencia).fetchmany(10)) #ejecuta la sentencia, y con fetchmany imprime la cantidad de filas deseadas

#print()

