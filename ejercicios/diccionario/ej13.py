
estudiantes = {
    "Ana": [8, 7, 9, 10],
    "Emmanuel": [6, 5, 7, 8],
    "Maria": [9, 10, 9, 8],
    "Carlos": [7, 8, 6, 7]
}

for nombre, calificaciones in estudiantes.items():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre}: promedio = {promedio:.2f}")
