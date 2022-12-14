#spotify

print ("""

🥵🥵🥵Welcome to spotify🥵🥵🥵

""")


print("""
1 - crear playlist
2 - abrir playlist 

    """)

lista = {}


def crear_playlist(lista):
    playlis = input("insertar nombre de la playlist: ")
    lista.update({"playlist":playlis})
    return lista

def seleccionar_pl():
    o = input("elige una opcion: ")

    if o == "1":
        crear_playlist(lista)
    elif o == "2":
        pass
    else:
        print("Escribe opcion valida")
        return 

seleccionar_pl()
print(lista)
    




    
    


