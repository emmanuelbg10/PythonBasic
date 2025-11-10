class Estudiante:
    def __init__(self, nombre, matricula, calificaciones = None):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__calificaciones = calificaciones if calificaciones is not None else []


    def agregar_calificacion(self, nueva_calificacion: float):
        if 0 <= nueva_calificacion <= 10: 
            self.__calificaciones.append(nueva_calificacion) 
            print("Se ha añadido la nueva calificacion a la lista")
            return
        print("No se ha podido añadir la nueva calificacion a la lista")

    def eliminar_calificacion(self, id: int):
        del(self.__calificaciones[id])

    def promedio(self):
        if len(self.__calificaciones) == 0:
            return 0
        return sum(self.__calificaciones) / len(self.__calificaciones)

    def obtener_info(self): 
        return f"El estudiante se llama {self.__nombre}, su matricula: {self.__matricula} y estas son sus calificaciones: {self.__calificaciones}"


est1 = Estudiante("Ana", "A123")
est2 = Estudiante("Luis", "B456")
est3 = Estudiante("Carla", "C789")

est1.agregar_calificacion(8.5)
est1.agregar_calificacion(9.0)
est1.agregar_calificacion(11)  # Fuera de rango

est2.agregar_calificacion(7.0)
est2.agregar_calificacion(6.5)

est3.agregar_calificacion(10)
est3.agregar_calificacion(9.5)
est3.agregar_calificacion(8.0)

print("\n--- Información de los estudiantes ---")
print(est1.obtener_info())
print(est2.obtener_info())
print(est3.obtener_info())


print("\n--- Eliminando calificaciones ---")
est3.eliminar_calificacion(1)  # Elimina la segunda calificación de Carla
print(est3.obtener_info())
