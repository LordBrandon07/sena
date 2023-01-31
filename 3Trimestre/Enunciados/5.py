#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica
#no pude realizar este codigo sin ayuda


import statistics

sample_input = input("Ingrese una muestra de números separados por comas: ")
sample = tuple(map(float, sample_input.split(","))) # convierte cada número en un float y los almacena en una tupla

mean = statistics.mean(sample)
stdev = statistics.stdev(sample)

print("Media:", mean)
print("Desviación típica:", stdev)


