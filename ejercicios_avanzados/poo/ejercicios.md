# Programación Orientada a Objetos — Ejercicios de Abstracción, Encapsulamiento, Herencia y Polimorfismo

---

## 🧩 **Abstracción**

### 🛰️ Sistema de control de vehículos autónomos

Diseña una jerarquía de clases que modele distintos tipos de vehículos autónomos (por ejemplo, automóvil, dron y barco).

**Requerimientos:**
- Crea una clase abstracta `VehiculoAutonomo` con métodos abstractos:
  - `iniciar_sistema_navegacion()`
  - `mover()`
  - `detener()`
- Implementa subclases concretas que definan comportamientos diferentes según el tipo de vehículo.
- Agrega un método adicional en la clase base para **calcular la autonomía energética** según el tipo de motor (`eléctrico`, `híbrido`, etc.) con implementación específica por subclase.
- Crea una **simulación** que ejecute varios tipos de vehículos y muestre sus acciones en orden, demostrando la abstracción en el diseño.

---

### 💰 Gestor financiero con operaciones bancarias abstractas

**Requerimientos:**
- Crea una clase abstracta `OperacionFinanciera` con atributos genéricos:
  - `monto`
  - `fecha`
- Métodos abstractos:
  - `validar()`
  - `ejecutar()`
- Implementa subclases:
  - `Transferencia`
  - `Pago`
  - `Deposito`
- Crea una clase `CuentaBancaria` que gestione un **saldo** y aplique operaciones financieras de distintos tipos.
- Simula una **secuencia de operaciones** en una lista y muéstralas procesadas en orden con resultados concretos y errores de validación (si aplica).

---

## 🔒 **Encapsulamiento**

### 🛒 Sistema de gestión de pedidos con control de acceso

**Requerimientos:**
- Crea una clase `Pedido` con atributos privados:
  - `__productos`
  - `__total`
- Implementa métodos públicos para:
  - Agregar productos
  - Eliminar productos
  - Listar productos
  - Recalcular el total internamente
- Agrega **propiedades** para acceder al total sin permitir su modificación directa.
- Añade **validaciones** que impidan precios o cantidades negativas.
- Crea una clase `Cliente` que solo pueda **consultar el total** de su pedido, sin modificarlo directamente.

---

### ⚙️ Control de sensores industriales

**Requerimientos:**
- Crea una clase `Sensor` con propiedades privadas:
  - `__valor_actual`
  - `__umbral_maximo`
- Implementa **getters y setters** con validación (impedir que el valor actual supere el umbral).
- Añade un método `registrar_lectura(valor)` que actualice el valor si pasa las validaciones.
- Implementa una clase `CentralDeControl` que use varios sensores y genere **alertas** cuando detecte valores fuera del rango permitido.
- Integra todo con **impresiones o registros simulados en consola**.

---

## 🧬 **Herencia**

### 🚍 Simulador de transporte público

**Requerimientos:**
- Crea una clase base `VehiculoTransporte` con atributos:
  - `capacidad`
  - `velocidad_max`
  - `id`
- Diseña subclases:
  - `Autobus`
  - `Tren`
  - `Tranvia`
- Cada subclase debe tener **comportamientos específicos** (modos de embarque, sistemas de cobro, etc.).
- Implementa un método `iniciar_viaje()` en la clase base que se **sobrescriba parcialmente** en las subclases.
- Crea una clase `RedTransporte` que gestione una lista de vehículos e invoque sus viajes de forma **polimórfica**.

---

### 🦁 Ecosistema de animales

**Requerimientos:**
- Implementa una clase base `Animal` con métodos:
  - `alimentarse()`
  - `emitir_sonido()`
- Crea subclases:
  - `Leon`
  - `Elefante`
  - `Zebra`
- Cada una debe sobrescribir los métodos de alimentación y sonido.
- Añade una clase `Zoologico` que contenga una **colección de animales** y un método `actividad_diaria()` que invoque los comportamientos comunes.
- Extiende el ejercicio con un **contador de alimento consumido total por especie**.

---

## 🎭 **Polimorfismo**

### 🖼️ Sistema de renderizado gráfico

**Requerimientos:**
- Crea una clase abstracta `Forma` con un método `dibujar()`.
- Implementa subclases:
  - `Rectangulo`
  - `Circulo`
  - `Triangulo`
- Crea una función `dibujar_escena(formas)` que recorra una lista de formas y ejecute sus métodos sin importar el tipo.
- Agrega una subclase `GrupoDeFormas` que contenga varias formas y también implemente `dibujar()`, demostrando **polimorfismo compuesto**.

---

### 🎵 Procesador multimedia

**Requerimientos:**
- Diseña una clase base `ArchivoMultimedia` con un método `reproducir()`.
- Crea subclases:
  - `ArchivoAudio`
  - `ArchivoVideo`
  - `ArchivoImagen`
- Implementa la clase `Reproductor` que pueda recibir distintos tipos de archivos multimedia en una lista y reproducirlos en orden.
- Añade funcionalidades para **pausar o detener** la reproducción, mostrando la **flexibilidad polimórfica** de los objetos multimedia.

---
