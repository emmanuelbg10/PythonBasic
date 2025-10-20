import datetime

print("Escribe una fecha en dia, mes y año y te diré que dia de la semana era")
dia = int(input("Escribe un dia: "))
mes = int(input("Escribe un mes: "))
año = int(input("Escribe un año: "))

try:
    fecha = datetime.date(año, mes, dia)
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    print(f"Dia: {nombres_dias[fecha.weekday()]}")

except ValueError:
    print("La fecha ingresada no es válida.")
