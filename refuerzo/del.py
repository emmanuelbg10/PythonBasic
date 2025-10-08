# DEL (especifica valor devuelto por una funcion)

lista = ["Uno", "Dos", "Tres"]
del lista[1]
print(lista) # Salida: ['Uno', 'Tres']
del lista
print(lista) # Salida: NameError: name 'lista' is not defined.