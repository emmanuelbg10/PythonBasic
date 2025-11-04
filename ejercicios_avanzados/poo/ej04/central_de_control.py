
from sensor import Sensor

class CentralDeControl:

    def __init__(self):
        self._sensores: dict[str, Sensor] = {}

    def agregar_sensor(self, sensor_id: str, sensor: Sensor):
        if sensor_id in self._sensores:
            print(f"[INFO] Sensor '{sensor_id}' ya existe.")
            return False
        self._sensores[sensor_id] = sensor
        print(f"[INFO] Sensor '{sensor_id}' agregado (valor={sensor.valor_actual}, umbral={sensor.umbral_maximo}).")
        return True

    def eliminar_sensor(self, sensor_id: str):
        if sensor_id not in self._sensores:
            print(f"[WARN] Sensor '{sensor_id}' no encontrado.")
            return False
        del self._sensores[sensor_id]
        print(f"[INFO] Sensor '{sensor_id}' eliminado.")
        return True

    def procesar_lectura(self, sensor_id: str, valor: float):

        if sensor_id not in self._sensores:
            print(f"[ERROR] Lectura para sensor desconocido '{sensor_id}'.")
            return

        sensor = self._sensores[sensor_id]
        aceptada = sensor.registrar_lectura(valor)
        if not aceptada:
           
            print(f"[ALERTA] Sensor '{sensor_id}': lectura {valor} rechazada (umbral={sensor.umbral_maximo}).")
        else:
            print(f"[OK] Sensor '{sensor_id}': lectura {valor} registrada correctamente.")
            
            distancia = sensor.umbral_maximo - sensor.valor_actual
            if distancia == 0:
                print(f"[CRÍTICO] Sensor '{sensor_id}' alcanzó el umbral máximo ({sensor.umbral_maximo}).")
            elif distancia <= max(1, sensor.umbral_maximo * 0.1):
                
                print(f"[ADVERTENCIA] Sensor '{sensor_id}' cerca del umbral (falta {distancia}).")

    def revisar_todos(self, margen_advertencia: float = 0):
        if not self._sensores:
            print("[INFO] No hay sensores registrados en la central.")
            return

        for sid, sensor in self._sensores.items():
            v = sensor.valor_actual
            u = sensor.umbral_maximo
            if v > u:
                print(f"[CRÍTICO] Sensor '{sid}': valor_actual={v} supera umbral={u}.")
            else:
                faltante = u - v
                if faltante <= margen_advertencia:
                    print(f"[ADVERTENCIA] Sensor '{sid}': cerca del umbral (faltan {faltante}).")
                else:
                    print(f"[INFO] Sensor '{sid}': OK (valor={v}, umbral={u}).")



central = CentralDeControl()

s1 = Sensor(valor_actual=10, umbral_maximo=20)
s2 = Sensor(valor_actual=5, umbral_maximo=50)
s3 = Sensor(valor_actual=0, umbral_maximo=10)

central.agregar_sensor("sensor_1", s1)
central.agregar_sensor("sensor_2", s2)
central.agregar_sensor("sensor_3", s3)

print("\n--- Procesando lecturas entrantes ---")
central.procesar_lectura("sensor_1", 15)   # aceptada
central.procesar_lectura("sensor_2", 60)   # rechazada (fuera de rango)
central.procesar_lectura("sensor_3", 10)   # aceptada y llega justo al umbral
central.procesar_lectura("sensor_4", 1)    # sensor desconocido

print("\nRevisión completa de sensores (margen_advertencia=2)")
central.revisar_todos(margen_advertencia=2)

print("\n--- Cambio de umbral y nueva lectura de prueba ---")
s2.umbral_maximo = 4  
central.procesar_lectura("sensor_2", 4)

print("\n--- Fin de la simulación ---")