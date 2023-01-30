#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica

# import statistics

# sample_input = input("Ingrese una muestra de números separados por comas: ")
# sample = tuple(map(float, sample_input.split(","))) # convierte cada número en un float y los almacena en una tupla

# mean = statistics.mean(sample)
# stdev = statistics.stdev(sample)

# print("Media:", mean)
# print("Desviación típica:", stdev)

sample_input = input("Ingrese una muestra de números separados por comas: ")
sample = list(map(float, sample_input.split(","))) # convierte cada número en un float y los almacena en una lista

mean = sum(sample) / len(sample)

sum_of_squared_diff = sum((x - mean) ** 2 for x in sample)
stdev = (sum_of_squared_diff / (len(sample) - 1)) ** 0.5

print("Media:", mean)
print("Desviación típica:", stdev)
