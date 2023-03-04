class Curso: #clase
    def __init__(self,titulo):  #constructor con dos parametros self(que es la misma clase) y nombre
        self.__titulo=titulo #propiedad privada que es el parametro

    def getTitulo(self): #metodo
        return self.__titulo

class Aprendiz: 
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[] #propiedad que es una lista

    def agregarCurso(self,nombreCursito): #metodo con dos parametros
        cursito=Curso(nombreCursito) #variable que se le asigna la clase 'curso' con el parametro 'nombrecursito'
        self.__cursos.append(cursito) #y losagrega en la lista '__cursos'

    def getCursos(self):
        return self.__cursos
    
ap=Aprendiz('Sofia')  #se instancia el objeto 'ap' a la clase Aprendiz
ap.agregarCurso('Python Basico') #se llama al metodo agregar curso de la clase 'Aprendiz'
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos(): #bucle que recorre c en el objeto 'ap' con el metodo 'getcursos'
    print(c.getTitulo())

