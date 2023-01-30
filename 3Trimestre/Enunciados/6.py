# Durante el desarrollo de un pequeño videojuego hay que configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debe cumplir las siguientes condiciones:
# El caballero tiene el doble de vida y defensa que un guerrero.
# El guerrero tiene el doble de ataque y alcance que un caballero.
# El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
# Escribir un programa que muestre como quedan las propiedades de los tres personajes.
# Utilice los siguientes diccionarios:
# caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
# guerrero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
# arquero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

# caballero = { 'vida':4, 'ataque':2, 'defensa': 4, 'alcance':2 }
# guerrero = { 'vida':2, 'ataque':4, 'defensa': 2, 'alcance':4 }
# arquero = { 'vida':2, 'ataque':4, 'defensa': 1, 'alcance':8 }

caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

caballero['vida'] = 2*2
caballero['defensa'] = 2*2

guerrero['ataque'] = 2*2
guerrero['alcance'] = 2*2

arquero['ataque'] = 2*2
arquero['defensa'] = guerrero['defensa'] /2
arquero['alcance'] = guerrero['alcance'] *2

print(caballero)
print(guerrero)
print(arquero)