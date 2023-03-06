class Aprendiz:  #clase
    def __init__(self,nombre):  #constructor con dos parametros self(que es la misma clase) y nombre
        self.__nombre=nombre #propiedad privada que es el parametro
        self.__cursos=[] #propiedad que es una lista

    def agregarCurso(self,titulo): #un metodo con dos parametros
        self.__cursos.append(titulo) #propiedad que agrega datos a la lista (__cursos)

    def getCursos(self): #metodo get
        return self.__cursos

class Curso:
    def __init__(self,titulo): #constructor con dos parametros
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo
    
a=Aprendiz('Martha') #se instancia el objeto 'A' a la clase Aprendiz
c1=Curso('Python Intermedio') #se instancia el objeto 'c1' a la clase curso
c2=Curso('Python Basico')
c3=Curso('Introduccion a Java')

a.agregarCurso(c1) #se llama al metodo agregar curso de la clase 'Aprendiz'
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos()) 

for curso in a.getCursos(): #un bucle que recorre curso en el objeto 'a' con el metodo 'getcursos'
    print(curso.getTitulo())  #imprime las cadenas de texto dadas en la instancia de objetos a 'curso'