def info(diccionario):
    partes = [] 
    
    for clave, valor in diccionario.items():
        partes.append(f"mi {clave} es: {valor}")
        
    return ", ".join(partes)

mi_diccionario = {
    "nombre": "Emmanuel",
    "edad": 20
}

print(info(mi_diccionario))
