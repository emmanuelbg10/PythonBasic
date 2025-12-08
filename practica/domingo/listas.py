# --------------------------------
print("PASO1: Lista del 1 al 20")
lista = list(range(1, 21))
print(lista)
# --------------------------------

# -------------------------------
print("PASO2: Invertir lista")
print(lista[::-1])
# -------------------------------

# ---------------------------------------------------------
print("PASO3: Lista de pares")
lista_pares = list([par for par in lista if par % 2 == 0])
print(lista_pares)
# ---------------------------------------------------------

# --------------------------------------------------
print("PASO4: Sumar todos los numeros de la lista")
print(sum(lista))
# --------------------------------------------------

# --------------------------------------------------------
print("PASO5: Encontrar el num max y el min de la lista")
# print("Min:", min(lista))
# print("MAX:", max(lista))


def mayor_o_menor(lista, decision):
    numero = lista[0]
    for x in lista:
        if decision == "max":
            if x > numero:
                numero = x
        elif decision == "min":
            if x < numero:
                numero = x
        else:
            return "OPCION NO VALIDA"
    return numero


decision = input("Escribe (min o max): ").lower()

print(f"{decision.upper()}: {mayor_o_menor(lista, decision)}")
# --------------------------------------------------------
