# Ejercicios de Programación Orientada a Objetos - Nivel Introductorio

## ENCAPSULAMIENTO

### Ejercicio 1.1: Cuenta Bancaria Simple

**Enunciado:**  
Crea una clase `CuentaBancaria` que tenga un atributo privado `saldo` que no pueda ser modificado directamente desde fuera de la clase. Implementa métodos públicos `depositar(cantidad)` y `retirar(cantidad)` que permitan modificar el saldo de forma controlada. El retiro solo debe permitirse si hay saldo suficiente.

**Pistas para abordarlo:**
- Usa el prefijo `_` (o `__` para privacidad más estricta) para marcar el atributo como privado.
- En el método `retirar()`, valida que el saldo sea suficiente antes de realizar la operación.
- Implementa un método `obtener_saldo()` para que el usuario pueda consultar el saldo sin modificarlo.
- Prueba creando una cuenta, depositando dinero, retirando dinero y consultando el saldo final.

---

### Ejercicio 1.2: Estudiante con Calificaciones Protegidas

**Enunciado:**  
Crea una clase `Estudiante` con atributos privados `nombre`, `matricula` y `calificaciones` (lista). Implementa métodos para:
- Agregar una calificación (debe estar entre 0 y 10)
- Obtener el promedio de calificaciones
- Obtener la información del estudiante sin permitir modificación externa

**Pistas para abordarlo:**
- Define los atributos como privados.
- En el método de agregar calificación, valida que esté en el rango 0-10.
- Crea un método que retorne el promedio calculado (sin permitir modificación).
- Implementa un método `obtener_info_
