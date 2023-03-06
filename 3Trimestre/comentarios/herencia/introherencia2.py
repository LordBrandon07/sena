class A1:  #clase 
    def __init__(self):  #constructror
        pass
    def saludo(self):      #metodo
        print('Hola desde A1')  

class A2:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A2')

                
class B(A2,A1): #clase con herencia multiple 'subclase'
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):  
        return 'Soy un objeto de la clase B'
obj=B() #se instancia el objeto a la clase 'B'
print(obj.__str__()) #se imprime el metodo  __str__ de la clase B
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())