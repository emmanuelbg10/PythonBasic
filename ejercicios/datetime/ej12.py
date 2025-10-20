from datetime import datetime

fecha_str = "2024-12-25"

# Convertir la cadena en un objeto date
fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()

print("Fecha:", fecha_obj)

# Obtener el día de la semana
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dia_semana = dias_semana[fecha_obj.weekday()]

print("Día de la semana:", dia_semana)
