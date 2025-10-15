frutas = ["pera", "manzana", "mandarina", "platano"]
respuesta = input("Escribe el nombre de una fruta y de dire si esta en la lista: ").lower()

solucion = "SI" if respuesta in frutas else "NO"
print(f"La fruta {respuesta} {solucion} esta en la lista: {frutas}")
