from auto import Auto
from motocicleta import Motocicleta

def main():
    mi_auto = Auto("Toyota", "Corolla", 2020, 4)
    mi_moto = Motocicleta("Honda", "CB500", 2021, "Deportivo")

    print(mi_auto.info_vehiculo())
    print(mi_moto.info_vehiculo())

if __name__ == "__main__":
    main()
