def comprueba(lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
    return False

lista1 = [1, 7, 3, 4]
lista2 = [2, 4, 6]

print(comprueba(lista1, lista2))
