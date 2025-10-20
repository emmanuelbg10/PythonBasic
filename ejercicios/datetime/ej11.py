from datetime import time, datetime, timedelta

def sumar_horas_minutos(hora, horas=0, minutos=0):
    dt = datetime.combine(datetime.today(), hora)  # convertimos a datetime
    dt += timedelta(hours=horas, minutes=minutos)  # sumamos el tiempo
    return dt.time()                               # devolvemos solo la hora

hora_inicial = time(14, 20)
hora_nueva = sumar_horas_minutos(hora_inicial, horas=2, minutos=30)

print("Hora inicial:", hora_inicial)
print("Hora nueva (2h30m después):", hora_nueva)
