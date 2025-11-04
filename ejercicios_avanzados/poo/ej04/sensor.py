class Sensor: 
    def __init__(self, valor_actual=0, umbral_maximo=100):
        if valor_actual > umbral_maximo:
            raise ValueError("El valor_actual no puede ser mayor que el umbral_maximo al crear el sensor.")
        self.__valor_actual = valor_actual
        self.__umbral_maximo = umbral_maximo

    @property
    def valor_actual(self):
        return self.__valor_actual
    
    @valor_actual.setter
    def valor_actual(self, nuevo_valor):
        self.registrar_lectura(nuevo_valor)

    @property
    def umbral_maximo(self):
        return self.__umbral_maximo
    
    @umbral_maximo.setter
    def umbral_maximo(self, nuevo_umbral):
        if nuevo_umbral < self.__valor_actual:
            print("El nuevo umbral no puede ser menor que el valor actual.")
            return False
        self.__umbral_maximo = nuevo_umbral
        return True

    def registrar_lectura(self, valor):
        if valor > self.__umbral_maximo:
            print("Lectura rechazada: valor supera el umbral máximo.")
            return False
        self.__valor_actual = valor
        return True
    
if __name__ == "__main__":

    s = Sensor(10, 20)
    print(s.registrar_lectura(25))  
    print(s.registrar_lectura(15))  
    print(s.umbral_maximo)          

    s.umbral_maximo = 5             
    print(s.umbral_maximo)          
