from Vehiculo import *  #importa vehiculo
class Carga(Vehiculo):  #crea una clase llamada vehiculo y herencia
    def __init__(self,placa,conductor,capacidad,ejes):
        Vehiculo.__init__(self,placa,conductor)
        self.__capacidad=capacidad
        self.__ejes=ejes    
    def getCapacidad(self):
        return self.__capacidad    
    def getEjes(self):
        return self.__ejes