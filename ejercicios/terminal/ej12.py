from datetime import datetime

year = int(input("Escribe tu año de nacimiento: "))
actual_year = int(datetime.now().year)
age = actual_year - year

print(f"Tienes {age} años")
if age < 100:
    print(f"Cumplirás 100 años en el año {year + 100}")
