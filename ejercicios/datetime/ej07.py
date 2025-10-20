import datetime

def fecha():
    print("\n")
    año = int(input("Escribe un año: "))
    mes = int(input("Escribe un mes: "))
    dia = int(input("Escribe un dia: "))
    return datetime.date(año, mes, dia)

print("Escribe dos fechas y te dire cuantos dias ha pasado entre ellos")

try:
    fecha1 = fecha()
    fecha2 = fecha()
    print(f"Hay {(fecha1 - fecha2).days} dia/s entre estas 2 fechas: \nfecha1: {fecha1}\nfecha2: {fecha2}")
except ValueError:
    print("Fecha no valida")

