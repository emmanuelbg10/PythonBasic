import datetime

ahora = datetime.date.today()
nacimiento = datetime.date(2005, 2, 10)

dias_transcurridos = (ahora - nacimiento).days


edad = ahora.year - nacimiento.year

# Ajustar si aún no ha pasado el cumpleaños este año
if (ahora.month, ahora.day) < (nacimiento.month, nacimiento.day):
    edad = edad -1

print(f"Hoy estamos a: {ahora}")
print(f"Nací en esta fecha: {nacimiento}")
print(f"Han pasado estos días: {dias_transcurridos}")
# es un extra pero tenia curiosidad de como se haria
print(f"En años sería esto: {edad}")