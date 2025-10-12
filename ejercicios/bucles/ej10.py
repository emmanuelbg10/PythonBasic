text = input("Escribe una frase: ")

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

result = 0

for caracter in text:
    if caracter in vocales:
        result += 1

print(f"Tiene {result} vocales")
