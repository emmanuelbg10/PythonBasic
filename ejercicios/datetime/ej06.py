import datetime

ahora = datetime.date.today()
nueva_fecha = ahora + datetime.timedelta(days=100)


print(f"Hoy es: {ahora}")
print(f"Dentro de 100 dias será: {nueva_fecha}")