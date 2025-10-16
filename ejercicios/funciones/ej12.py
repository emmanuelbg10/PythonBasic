def frecuencia_caracter(text):
    diccionario = {}
    for c in text:
        if c in diccionario:
            diccionario[c] +=1
        else:
            diccionario[c] = 1
        
    return diccionario

print(frecuencia_caracter("Hola que tal"))