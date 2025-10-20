import datetime

fecha_actual = datetime.datetime.now()
proximo_ano_nuevo = datetime.datetime(fecha_actual.year + 1, 1 , 1)
tiempo_restante = proximo_ano_nuevo - fecha_actual
print(f"Falta: {tiempo_restante} tiempo para año nuevo!!!")
