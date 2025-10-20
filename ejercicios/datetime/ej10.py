import datetime

# Pedir fecha de nacimiento
año = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Día: "))

fecha_nac = datetime.date(año, mes, dia)
hoy = datetime.date.today()

# años
años = hoy.year - fecha_nac.year
if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
    años -= 1

# meses
meses = hoy.month - fecha_nac.month
if hoy.day < fecha_nac.day:
    meses -= 1
if meses < 0:
    meses += 12

# dias 
dias = hoy.day - fecha_nac.day
if dias < 0:
    dias += 30  

print(f"Tienes {años} años, {meses} meses y {dias} días.")
