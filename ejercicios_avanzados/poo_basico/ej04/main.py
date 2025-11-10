from persona import Persona
from empleado import Empleado
from jefe import Jefe

def main():
    persona = Persona("Ana", 30)
    empleado1 = Empleado("Luis", 28, 1500, "Marketing")
    empleado2 = Empleado("Jorge", 22, 1200, "Publicidad")
    jefe = Jefe("Carlos", 40, 3000, "Ventas", [empleado1, empleado2])

    print(persona.info_persona())
    print(empleado1.info_persona())
    print(empleado2.info_persona())
    print(jefe.info_persona())

if __name__ == "__main__":
    main()
