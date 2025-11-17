import os

class Tarea:
    def __init__(self, descripcion, completada):
        self.descripcion = descripcion
        self.completada = completada


    @classmethod
    def tareas_desde_fichero(cls):
        tareas = []
        ruta_actual = os.path.dirname(__file__)
        archivo = os.path.join(ruta_actual, "tareas.txt")

        try:
            with open(archivo, "r") as file:
                descripcion = None
                completada = None
                for line in file:
                    line = line.strip()
                    if line.startswith("Descripción: "):
                        descripcion = line.replace("Descripción: ", "")
                     
                    elif line.startswith("Completada:"):                        
                        completada = line.replace("Completada: ", "")

                    if descripcion is not None and completada is not None:
                        tareas.append(cls(descripcion, completada))
                        descripcion = None
                        completada = None        
        except OSError:
            print('No fue posible leer el archivo')

        return tareas

tarea1 = Tarea("Comprar leche para la semana", False)
tarea2 = Tarea("Terminar el ejercicio de ficheros", True)
tarea3 = Tarea("Llamar a mi hermana", False)

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "tareas.txt")

try:
    with open(archivo, "w") as file:
        for tarea in tarea1, tarea2, tarea3:
            file.write(f"Descripción: {tarea.descripcion}\nCompletada: {tarea.completada}\n\n")
except OSError:
    print('No fue posible crear el archivo')


tareas = Tarea.tareas_desde_fichero()

for tarea in tareas:
    print(f"{tarea.descripcion}: {tarea.completada}")