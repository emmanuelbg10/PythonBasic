lista = list(range(1, 21))
print("Lista normal:")
print(lista)

lista2 = list(filter(lambda x: x % 3, lista))
print("Lista sin multiplos de 3:")
print(lista2)