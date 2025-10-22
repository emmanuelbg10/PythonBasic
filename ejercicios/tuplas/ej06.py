coordenadas = (10, 20, 30)
print("Tupla original:", coordenadas)

lista_coord = list(coordenadas)


lista_coord[1] = 50
print("Lista modificada:", lista_coord)

coordenadas_modificadas = tuple(lista_coord)
print("Tupla modificada:", coordenadas_modificadas)
