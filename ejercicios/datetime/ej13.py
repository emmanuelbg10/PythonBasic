from datetime import datetime

# Pedir al usuario que ingrese la hora de inicio y fin en formato HH:MM:SS
inicio_str = input("Ingrese la hora de inicio (HH:MM:SS): ")
fin_str = input("Ingrese la hora de fin (HH:MM:SS): ")

# Convertir las cadenas a objetos datetime usando cualquier fecha
inicio = datetime.strptime(inicio_str, "%H:%M:%S")
fin = datetime.strptime(fin_str, "%H:%M:%S")

# Calcular la duración
duracion = fin - inicio
duracion_segundos = duracion.total_seconds()

print(f"La duración de la tarea fue de {duracion_segundos} segundos.")
