#Spotify conjunto

print ("""🎧🎤🎹Welcome to spotify🎧🎤🎹""")

lista = {}
songg = {}

def new_artist(lista):
    artista = input ("introduzca el artista: ")
    if artista not in lista:
        lista.update({artista:{}})
        return lista
    else:
        exit()
        
def song(lista):
    artista = input ("introduzca el artista: ")
    if artista not in lista:
        print("artista no encontrado: ")
        return lista
    else:
        cancion = input("introduzca una cancion: ")
        genero = input("introduzca el genero: ")
        duracion = input("introduzca la duracion: ")
        lista.update({artista:{genero:{cancion:duracion}}})
        
def delate(lista):
    artista = input ("introduzca el artista: ")
    if artista in lista:
        del lista[artista]
    print(lista)  
        
def search(lista):
    artista = input ("introduzca el artista: ")
    if artista in lista:
        print(lista[artista])
    else:
        return lista
        
        
        
        
def searchsong(lista):
    pass

def songshort(lista):
    pass

def songlarge(lista):
    pass
        







def exitt():
    print("""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣠⠤⣖⣾⣭⡍⠉⠹⣿⣗⣦⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠶⢶⣶⣿⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣾⣕⡦⣄⡀⠀⠀⠀⠀
⠀⠈⣧⣧⣉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢹⣿⡿⣿⣿⣷⣯⣳⡀⠀⠀
⠀⠀⠘⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠿⠃⠀⣿⡆⠀⢹⣿⣿⠛⣷⡀⠀
⠀⠀⡴⠉⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠆⠀⣿⣇⣸⣿⠟⠁⠀⠉⣧⠀
⠀⠀⣷⠂⠀⠘⣮⠙⠛⠒⠒⠛⠀⠀⢠⡏⠀⢰⣿⣿⣿⠏⠀⠀⠀⠂⢸⠀
⠀⠰⡏⠀⠀⢰⣿⣷⣤⣄⢀⣀⣤⡜⠋⢀⣠⣿⣿⣿⡟⠀⠀⠀⠀⠀⢸⠀
⠀⢸⣇⡀⠀⠈⠛⢿⣿⣿⣷⣶⠯⢭⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢸⡄
⠀⢺⣉⡍⢹⡆⠀⠀⠀⠉⠀⠈⠀⠀⠻⠛⠟⠛⠛⠋⣁⠀⠀⠀⠀⠀⣈⣿
⠀⡟⠂⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠶⠤⠀⠐⠀⢸⡟
⢀⣧⡀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠀⠀⠀⠀⢸⡇
⣼⣃⡀⠀⠀⠻⠻⢿⣿⣷⣤⣤⣤⣄⣀⠀⣀⣀⣀⣴⡆⠀⠀⠀⠀⠀⢸⣇
⣿⢀⠁⠀⢠⡆⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠃⠀⠀⠀⠀⠀⠀⡏
⢻⡜⠳⢶⣼⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⡇
⢸⣿⡀⠀⠀⣿⣿⣿⣿⣿⢗⡶⢤⣤⣀⣀⣀⣀⣀⣀⡁⠀⠀⠀⠀⠀⠀⣿
⠸⣏⢇⠀⠀⣿⣿⣿⣿⣿⠀⠉⠉⠉⠛⠾⣿⣿⣿⣿⣷⣤⣤⣤⡴⠤⢤⣿
⠀⠘⢮⣁⣰⣿⣿⣿⡟⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⣸⣻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠸⡿⣿⡟⠁⣰⠇⠀⠀⠀⡀⣿
⠀⠀⠀⡰⣻⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠹⡽⣿⡿⠋⢀⡄⠴⣚⡵⠛
⠀⠀⣾⣿⣿⣿⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⠖⠋⠉⠀⠀
⠀⠀⠹⡽⣿⣿⣿⢏⠟⠀⠀⠀⠀⠀⠀⣠⢞⣽⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠉⠛⠉⠀⠀⠀⠀⠀⠀⢸⣱⣿⣿⣿⣿⣿⡿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⡿⠿⠿⠽⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ADIOS
          """)



while True:
    
    print("""
      Elija una opcion
      
      1-crear artista
      2-Crear cancion
      3-eliminar artista
      4-buscar artista
      5-buscar cancion
      6-cancion mas corta
      7-cancion mas larga
      0-Salir
      """,)
    
    o = int(input("seleccione una opcion: "))
    match o:
        case 1:
            new_artist(lista)
        case 2:
            song(lista)
        case 3:
            delate(lista)
        case 4:
            search(lista)
        case 5:
            searchsong(lista)
        case 6:
            songshort(lista)
        case 7:
            songlarge(lista)
        case 0:
            exitt()
            exit()
        case _:
            print("ocpion invalida")
            exit()
