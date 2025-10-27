class Persona:
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def gritar(self):
        return f"{self.nombre} está gritando"
    
        
emmanuel = Persona("Emmanuel", "Barral", "123456789W", "emmanuel@gmail.com")

print(emmanuel.gritar())