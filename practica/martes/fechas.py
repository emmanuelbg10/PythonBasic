import datetime

# --------------------------------------------------------------------------
print("PASO1: Calcula los dias restantes para tu cumpleaños")
cumple = datetime.date(2005, 2, 10)
hoy = datetime.date.today()

proximo_cumple = datetime.date(hoy.year, cumple.month, cumple.day)

if proximo_cumple < hoy:
    proximo_cumple = datetime.date(hoy.year + 1, cumple.month, cumple.day)

dias_faltan = (proximo_cumple - hoy).days
print(f"Faltan {dias_faltan} días para tu cumpleaños")
# --------------------------------------------------------------------------
print("PASO2: Ordenar lista de fechas")

fecha1 = datetime.date(2002, 8, 10)
fecha2 = datetime.date(2025, 12, 9)
fecha3 = datetime.date(2005, 2, 10)

lista = [fecha1, fecha2, fecha3]
lista.sort()
print(lista)
# --------------------------------------------------------------------------
print("PASO3: Suma 7 dias a la fecha de hoy")

hoy += datetime.timedelta(days=7)
print(hoy)
