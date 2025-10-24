palabras = ["Python", "Pera", "Manzana", "Emmanuel"]

diccionario = {x : len(x) for x in palabras if len(x) > 4}

print(diccionario)