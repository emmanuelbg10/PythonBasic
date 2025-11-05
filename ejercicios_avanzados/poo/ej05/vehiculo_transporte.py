class VehiculoTransporte:
    def __init__(self, capacidad, velocidad_max, metodos_aceptados, id):
        self.capacidad = capacidad
        self.velocidad_max = velocidad_max
        self.metodos_aceptados = metodos_aceptados
        self.id = id

    def iniciar_viaje(self):
        return "Esta iniciando el viaje"
    
    def sistema_cobro(self, metodo_cobro, cantidad):
        if metodo_cobro not in self.metodos_aceptados:
            return f"El cobro no se puede realizar porque no estas implementando un metodo de cobro valido"
        if cantidad <= 0:
            return f"El cobro no se puede realizar porque no tienes dinero"
        
        return f"Cobro de {cantidad:.2f}€ realizado con {metodo_cobro}."