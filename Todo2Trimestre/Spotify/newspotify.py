print ("""🎧🎤🎹Welcome to spotify🎧🎤🎹""")

def artist(play, arti, gene, canc, dura):
    play.update({arti:{gene:{canc:dura}}})

lista = {}
arti = {}
gene = {}
canc = {}
dura = {}


def new_artist(lista, arti, gene, canc, dura):
    arti = input ("introduzca el artista: ")
    gene = input("introduzca el genero: ")
    canc = input("introduzca una cancion: ")
    dura = input("introduzca la duracion: ")
    lista.update({arti:{gene:{canc: dura}}})
    print(lista)
    return lista

def song(lista, arti, gene, canc, dura):
    arti = input ("introduzca el artista: ")
    if arti not in lista:
        print("artista no encontrado: ")
        return lista
    else:
        gene = input("introduzca el genero: ")
        canc = input("introduzca una cancion: ")
        dura = input("introduzca la duracion: ")
        lista.update({arti:{gene:{canc: dura}}})
        print(lista)
        return lista

def delate(arti, lista):
    arti = input ("introduzca el artista: ")
    if arti in list:
        del lista[arti]
        print(lista)
    else:
        print("artista no encontrado: ")

def search(lista):
    arti = input ("introduzca el artista: ")
    if arti in lista:
        print(lista)
    else:
        return lista
    












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
      """,)
    
    o = int(input("seleccione una opcion: "))
    match o:
        case 1:
            new_artist(lista, arti, gene, canc, dura)
        case 2:
            song(lista, arti, gene, canc, dura)
        case 3:
            delate(arti, lista)
        case 4:
            search(lista)
    #     case 5:
    #         searchsong(lista)
    #     case 6:
    #         songshort(lista)
    #     case 7:
    #         songlarge(lista)
    #     case _:
    #         print("ocpion invalida")
    #         exit()