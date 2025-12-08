# ----------------------------------------------------------------------------
print("PASO1: Lista al cuadrado con compresion")
lista = list(range(1, 21))
lista_cuadrado = [num**2 for num in lista if num % 2 == 0]
print(lista_cuadrado)
# ----------------------------------------------------------------------------
print("PASO2: Diccionario con clave de num lista y valores cuadrados")
diccionario = {num: num**2 for num in lista}
print(diccionario)
# ----------------------------------------------------------------------------
