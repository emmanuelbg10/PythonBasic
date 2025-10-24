lista = [9, 2, 10, 21, 11, 3, 34]

print("Lista normal:", lista)

lista_filtrada = list(filter(lambda x: x > 10, lista))

print("Lista filtrada:", lista_filtrada)