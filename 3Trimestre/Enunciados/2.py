#Comprobar si una palabra o frase es palíndromo.(Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.)

def palindrome(p):
    p = p.replace(' ', '')
    p = p.lower()
    p_inver = p[::-1]
    if p == p_inver:
        return True
    else:
        return False

def run():
    p = input('introduzca una palabra: ')
    is_palindrome = palindrome(p)
    if is_palindrome == True:
        print('es palindromo')
    else:
        print('no es palindromo')

run()