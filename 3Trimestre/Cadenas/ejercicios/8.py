# Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

cadena = input('ingrese una cadena: ')

c = ''

for i in cadena:
    if not i.isalpha():
        continue
    i = i.upper()
    co = ord(i) + 1
    if co > ord('Z'):
        co = ord('A')
    c += chr(co)

print(c)