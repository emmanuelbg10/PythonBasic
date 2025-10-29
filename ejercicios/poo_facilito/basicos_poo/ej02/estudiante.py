class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

estudiante01 = Estudiante("Emmanuel", 10)
estudiante02 = Estudiante("Cesar", 0)

for estudiante in estudiante01, estudiante02:
    print(f"El estudiante {estudiante.nombre} tiene esta nota: {estudiante.nota}")
