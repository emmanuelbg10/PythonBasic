letras = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

frase = input("Escribe una frase: ")

for caracter in frase:

    if caracter.lower() in letras:
        letras[caracter.lower()] += 1


print(letras)
