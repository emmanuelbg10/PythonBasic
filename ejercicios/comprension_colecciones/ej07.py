frase = "Hola que tal Emmanuel"

vocales = {letra for letra in frase.lower() if letra in "aeiou"}

print(vocales)