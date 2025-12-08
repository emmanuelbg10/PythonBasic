# ----------------------------------------------------------------------------
print("PASO1: Crear diccionario con 5 palabras como clave y valores")
diccionario = {
    "huevo": len("huevo"),
    "manzana": len("manzana"),
    "pera": len("pera"),
    "arroz": len("arroz"),
    "aguacate": len("aguacate"),
}
print(diccionario)
# ----------------------------------------------------------------------------
print("PASO2: Agregar 2 elementos nuevos al diccionario")
elemento1 = input("Escribe el primer elemento: ")
elemento2 = input("Escribe el segundo elemento: ")
diccionario[elemento1] = len(elemento1)
diccionario[elemento2] = len(elemento2)
print(diccionario)
# ----------------------------------------------------------------------------
print("PASO3: Solo palabras mayor a 4")
print(list(filter(lambda palabra: len(palabra) > 4, diccionario)))
# ----------------------------------------------------------------------------
print("PASO4: Invertir claves y valores con comprension")
invertido = {valor: clave for clave, valor in diccionario.items()}
print(invertido)
# ----------------------------------------------------------------------------
