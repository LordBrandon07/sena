import sqlite3

with sqlite3.connect('conpython.db')as con: #crea una coneccion con la base datos 'ruta relativa', con un bloque de codigo 'with' y le pone el nombre 'con'
    micursor=con.cursor() #crea el cursor para manipular la base de datos
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;" #crea una sentencia sql, ya con un where
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato): #crea una funcion con 5 parametros
    micursor=conexion.cursor() 
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'" #plantilla literal, con las variables deseadas a modificar
    print(sentencia)
    print(micursor.execute(sentencia).fetchall()) #ejecuta la sentencia, y con fetchall imprime todas las filas

# miselect(con,'alumno','email','=','dbrabon2@irs.gov') 

def modificar(conexion, tabla, campo, dato, id):
    micursor = conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo} = '{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit
    print('MODIFICACION EXITOSA!!!')
    
#modificar(con, 'alumno','nombre','vegeta',1)
#DELETE FROM table_name WHERE condition;
    
def eliminar(conexion, tabla, campo, dato):
    micursor = conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='dato"
    micursor.execute(sentencia)
    con.commit
    print('ELIMINACION EXITOSA!!!')
        

