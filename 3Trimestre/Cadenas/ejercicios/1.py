# Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

abecedario = 'abcdefghijklmnñopqrstuvwxyzabcxyzab'

count = 0

for i in abecedario:
    if i in abecedario :
        count += 1
    
print(count)