# Escriba una clase Empleado que tenga como propiedades
# nombre, cargo, salario
# escriba metodos contructores, setters y getters
# escriba un método que permita calcular cuanto gana el empleado en una hora
# un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
# Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
#poner un contador cada vez que se instancie un objeto

class Empleado:
    count = 0
    def __init__(self, nombre, cargo, salario):
        if salario < 1160000:
            print('no puede ganar menos de un minimo')
        else:
            self.__nombre = nombre
            self.__cargo = cargo
            self.__salario = salario
            # Empleado.count += 1
            # print(f'el total de objetos es: {Empleado.count}')
            
    def getDatos(self):
        try:
            return self.__nombre, self.__cargo, self.__salario
        except:
            exit
    
    def setNombre(self, nombre):
        self.__nombre=nombre
        
    def setCargo(self, cargo):
        self.__cargo=cargo
    
    def setSalario(self, salario):
        try:
            self.__salario=salario
        except:
            exit

    def calcular(self):
        try:
            salario = self.__salario
            self.__salario=salario
            calcDia = (salario//30)
            calcHora = (calcDia//8)
            return calcHora
        except:
            exit
    
    def incremento(self):
        try:
            salario = self.__salario
            if salario > 1160000:
                salario *= 0.13
                print(f'el IPC aumento el 13%: {salario}')
            else:
                salario *= 0.16
                print(f'el IPC aumento el 16%: {salario}')
        except:
            exit
    
    def extra(self, horas):
        try:
            salario = self.__salario
            calcDia = (salario//30)
            calcHora = (calcDia//8)
            if horas <= 40:
                sum = horas * calcHora
                salario += horas * calcHora
                print(f'trabajo horas extra: {sum}')
                print(f'salario con horas extra: {salario}')
            elif horas > 40:
                print('no se pueden poner mas de 40 horas mensuales')
            else:
                print('dato incorrecto')
        except:
            exit
        
ob = Empleado('pepe', 'transportador', 1160000)
print(ob.getDatos())
print(ob.calcular())
ob.incremento()
ob.extra(40)
print('-------------------------------')

# ob.setNombre('pablo')
# print(ob.getDatos())
# print('--------------------------------')

ob1 = Empleado('ramiro', 'diseñador', 2000000)
print(ob1.getDatos())

