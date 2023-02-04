import random

def division():
    a = random.randint(1,100)
    b = random.randint(1,100)
    res = a/b
    print(a,'/',b)
    return round(res,2)

def multiplicacion(a):
    s=1
    for i in range(a):
        n = random.randint(1,50)
        s *= n
        print(n,"* ",end="")
    print('')
    return s

def suma(a):
    s=0
    for i in range(a):
        n = random.randint(1,100)
        s += n
        print(n,"+ ",end="")
    print('')
    return s

def resta():
    a = random.randint(0,100)
    b = random.randint(0,100)
    res = a-b
    print(a,'-',b)
    return res