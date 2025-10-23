personas = {
    "Emmanuel" : 20,
    "Pablo" : 12,
    "Ana" : 50,
    "Julian" : 23,
    "Lucia" : 9,
    "Joel" : 48
}

persona_mayor = max(personas, key=personas.get)

print(f"La persona con mayor edad es: {persona_mayor} con {personas[persona_mayor]}")