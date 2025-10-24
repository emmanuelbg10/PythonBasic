palabras = ["Buenas", "Que", "Tal", "Emmanuel"]
print(f"Lista normal: {palabras}")

lista_filtrada = list(filter(lambda x: len(x) > 5, palabras))


print(f"\nLista filtrada: {lista_filtrada}")