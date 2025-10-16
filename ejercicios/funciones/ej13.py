def palabra_larga(palabras):
    result = palabras[0]
    for palabra in palabras:
        result = palabra if len(palabra) > len(result) else result
    return result


lista = ["Hola", "buenas", "que", "tal"]

print(palabra_larga(lista))
