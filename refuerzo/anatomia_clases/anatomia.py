class NombreClase:
    """
    Docstring de la clase: Documentación que describe el propósito de la clase.
    Esta es una buena práctica profesional.
    """
    
    # 1. ATRIBUTOS DE CLASE (compartidos por todas las instancias)
    atributo_clase = "Valor compartido por todos los objetos"
    contador_instancias = 0
    
    # 2. MÉTODO CONSTRUCTOR (__init__)
    def __init__(self, parametro1, parametro2, parametro3="valor_por_defecto"):
        """
        Constructor: Se ejecuta automáticamente al crear un objeto.
        self: referencia a la instancia actual del objeto.
        """
        # Atributos de instancia (únicos para cada objeto)
        self.atributo1 = parametro1
        self.atributo2 = parametro2
        self.atributo3 = parametro3
        
        # Atributos privados (convención: prefijo _ o __)
        self._atributo_protegido = "No debería accederse desde fuera"
        self.__atributo_privado = "Atributo 'privado' (name mangling)"
        
        # Incrementar contador de clase
        NombreClase.contador_instancias += 1
    
    # 3. MÉTODOS DE INSTANCIA
    def metodo_instancia(self, parametro):
        """
        Método de instancia: Opera sobre los datos del objeto específico.
        Siempre recibe 'self' como primer parámetro.
        """
        # Puede acceder y modificar atributos de instancia
        self.atributo1 = parametro
        # Puede acceder a atributos de clase
        print(f"Atributo de clase: {NombreClase.atributo_clase}")
        return self.atributo2
    
    # 4. MÉTODOS DE CLASE
    @classmethod
    def metodo_clase(cls, parametro):
        """
        Método de clase: Opera sobre la clase, no sobre instancias específicas.
        Recibe 'cls' (la clase) como primer parámetro.
        Útil para métodos de fábrica o constructores alternativos.
        """
        # Puede acceder y modificar atributos de clase
        cls.atributo_clase = parametro
        # Puede crear instancias de la clase
        return cls(parametro, "valor2")
    
    # 5. MÉTODOS ESTÁTICOS
    @staticmethod
    def metodo_estatico(parametro):
        """
        Método estático: No recibe ni self ni cls.
        No puede acceder a atributos de instancia ni de clase directamente.
        Útil para funciones auxiliares relacionadas con la clase.
        """
        # Solo realiza operaciones con los parámetros recibidos
        return parametro * 2
    
    # 6. PROPIEDADES (GETTERS Y SETTERS)
    @property
    def atributo_calculado(self):
        """
        Getter: Permite acceder a un atributo como si fuera público,
        pero ejecutando código personalizado.
        """
        return f"{self.atributo1} - {self.atributo2}"
    
    @atributo_calculado.setter
    def atributo_calculado(self, valor):
        """
        Setter: Permite modificar un atributo con validación o procesamiento.
        """
        partes = valor.split(" - ")
        if len(partes) == 2:
            self.atributo1, self.atributo2 = partes
        else:
            raise ValueError("Formato incorrecto")
    
    @atributo_calculado.deleter
    def atributo_calculado(self):
        """
        Deleter: Se ejecuta al usar 'del objeto.atributo_calculado'
        """
        del self.atributo1
        del self.atributo2
    
    # 7. MÉTODOS MÁGICOS (DUNDER METHODS)
    def __str__(self):
        """
        Representación legible para humanos (usado por print() y str()).
        """
        return f"NombreClase({self.atributo1}, {self.atributo2})"
    
    def __repr__(self):
        """
        Representación oficial del objeto (usado en consola interactiva).
        Debería permitir recrear el objeto si es posible.
        """
        return f"NombreClase('{self.atributo1}', '{self.atributo2}', '{self.atributo3}')"
    
    def __len__(self):
        """Permite usar len() sobre el objeto."""
        return len(self.atributo1)
    
    def __eq__(self, otro):
        """Define cómo comparar dos objetos con =="""
        if isinstance(otro, NombreClase):
            return self.atributo1 == otro.atributo1
        return False
    
    def __add__(self, otro):
        """Define cómo sumar dos objetos con +"""
        return NombreClase(
            self.atributo1 + otro.atributo1,
            self.atributo2 + otro.atributo2
        )
    
    def __getitem__(self, indice):
        """Permite acceder al objeto como si fuera una lista: objeto[indice]"""
        return [self.atributo1, self.atributo2][indice]
    
    def __call__(self, *args, **kwargs):
        """Permite llamar al objeto como si fuera una función: objeto()"""
        print(f"Objeto llamado con args={args}, kwargs={kwargs}")
    
    def __enter__(self):
        """Para usar la clase con context manager (with statement)"""
        print("Entrando al contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Saliendo del context manager"""
        print("Saliendo del contexto")
        return False
    
    # 8. MÉTODO DESTRUCTOR
    def __del__(self):
        """
        Destructor: Se ejecuta cuando el objeto va a ser eliminado.
        Raramente necesario en Python por el garbage collector.
        """
        NombreClase.contador_instancias -= 1
        print(f"Objeto destruido. Instancias restantes: {NombreClase.contador_instancias}")