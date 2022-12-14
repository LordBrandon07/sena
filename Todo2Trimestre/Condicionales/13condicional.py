#pasar segundos a minutos y segundos

s = int(input("introduzca segundos: "))

m =  s // 60 
sr =  s % 60

h =  m // 60
mr = m % 60


print("los minutos y segundos son: ", h,":", mr, ":", sr)
