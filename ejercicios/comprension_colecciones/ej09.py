palabras = ["Hola", "avellana", "que", "tal", "estas"]

lista_filtrada = [x for x in palabras if x[0].lower() in "aeiou"]

print(f"Lista normal: {palabras}")

print(f"Lista filtrada: {lista_filtrada}")