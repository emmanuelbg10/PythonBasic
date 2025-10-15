lista = list(range(1, 11))

def num_maximo(lista):
    maximo = lista[0]
    for i in lista:
        maximo = i if i > maximo else maximo
    return maximo

print(num_maximo(lista))