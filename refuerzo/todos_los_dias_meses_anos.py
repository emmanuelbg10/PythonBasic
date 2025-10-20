import datetime

print("Escribe tu fecha de nacimiento: ")
try:
    año = int(input("Escribe tu año: "))
    mes = int(input("Escribe tu mes: "))
    dia = int(input("Escribe tu dia: "))

    fecha_usuario = datetime.date(año, mes, dia)

except:
    print("Fecha no válida")
    exit()

fecha_actual = datetime.date.today()

año_usuario = fecha_actual.year - fecha_usuario.year
if (fecha_actual.month, fecha_actual.day) < (fecha_usuario.month, fecha_usuario.day):
    año_usuario -= 1

# Calcular meses
mes_usuario = fecha_actual.month - fecha_usuario.month
if fecha_actual.day < fecha_usuario.day:
    mes_usuario -= 1
if mes_usuario < 0:
    mes_usuario += 12

# Calcular días totales
total_dias = (fecha_actual - fecha_usuario).days
total_meses = año_usuario * 12 + mes_usuario

print(f"Tienes {año_usuario} años, o {total_meses} meses, o {total_dias} días vivo")
