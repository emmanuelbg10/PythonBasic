# ------------------------------------------------------------------------
print("PASO1: Devuelve una lista con los cuadrados de los numeros pares")
lista = list(range(1, 21))
print("Numeros:", lista)


def funcion1(lista):
    return [num**2 for num in lista if num % 2 == 0]


print("Cuadrados de numeros pares:", funcion1(lista))
# ------------------------------------------------------------------------
print("\nPASO2: Nuevo diccionario con valores multiplicados por 2")
diccionario = {"dato1": 1, "dato2": 2, "dato3": 3, "dato4": 4}
print("Diccionario:", diccionario)


def funcion2(diccionario: dict):
    return {clave: valor * 2 for clave, valor in diccionario.items()}


print("Diccionario por 2:", funcion2(diccionario))


# ------------------------------------------------------------------------
