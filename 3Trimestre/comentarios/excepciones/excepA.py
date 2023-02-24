try:
    #print(1/1))  # ocaciona un syntax error, pero el except no es capaz de manejarlo
    raise SyntaxError  #ocacionar un syntax error
except SyntaxError:
    print('Cierra el parentesis')