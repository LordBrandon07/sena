#https://docs.python.org/es/3/library/exceptions.html
a=int(input("ingrese un valor menor a 20 "))
# IndentationError
def error(psdf):
try:
    if a <=20:
            print("error")
    else:
            print("esta bien")
except IndentationError:
            print("esta mal")
    
  
error(a)


