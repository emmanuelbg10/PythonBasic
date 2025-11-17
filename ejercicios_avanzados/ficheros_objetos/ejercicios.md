# Manipulación de Ficheros y Objetos con Python

---

## Ficheros TXT

### Gestión de notas simples en texto plano
- Crea una clase `Nota` con atributos `titulo` y `contenido`.
  - Permite crear varias instancias de la clase y guardarlas en un archivo de texto (`notas.txt`), de modo que cada línea contenga título y contenido separados por un guion.
  - Implementa un método de clase que lea el archivo y reconstruya las instancias de `Nota` a partir de su contenido.

### Registro de tareas con formato libre
- Diseña una clase `Tarea` con atributos `descripcion` y `completada`.
  - Crea varias tareas y guarda sus datos en un archivo de texto donde cada tarea ocupe varias líneas (por ejemplo, con etiquetas como “Descripción:” y “Completada:”).
  - Desarrolla un método que abra el archivo y devuelva una lista de objetos `Tarea` a partir de la información cargada.

---

## Ficheros CSV

### Inventario de productos
- Implementa una clase `Producto` con atributos `id`, `nombre` y `precio`.
  - Permite guardar una lista de productos en un archivo `productos.csv`, con encabezados de columna.
  - Agrega un método que lea el archivo CSV y reconstruya los objetos `Producto` automáticamente.

### Gestión de empleados
- Crea una clase `Empleado` con atributos `nombre`, `edad` y `departamento`.
  - Crea un conjunto de empleados y guárdalos en un CSV separado por punto y coma.
  - Implementa un método que lea ese CSV y genere una lista de objetos `Empleado`.
  - Añade una pequeña función que filtre los empleados de un departamento específico.

---

## Ficheros XML

### Catálogo de libros
- Diseña una clase `Libro` con atributos `titulo`, `autor` y `anio_publicacion`.
  - Crea varios objetos `Libro` y guarda sus datos en un archivo `libros.xml` estructurado (raíz `<catalogo>` con nodos `<libro>`).
  - Implementa un método que lea el XML y construya las instancias de `Libro` a partir de los nodos.

### Directorio de contactos
- Crea una clase `Contacto` con atributos `nombre`, `telefono` y `email`.
  - Genera un XML llamado `contactos.xml` que contenga todos los contactos como nodos individuales.
  - Añade un método que lea el archivo y devuelva una lista de objetos `Contacto`, mostrando además los nombres de todos los contactos almacenados.

---

## Ficheros JSON

### Gestión de pedidos
- Desarrolla una clase `Pedido` con atributos `id_pedido`, `cliente` y `productos` (lista de nombres).
  - Guarda varios pedidos en un archivo `pedidos.json`, donde cada uno se almacene como un objeto JSON.
  - Implementa un método que cargue el archivo y reconstruya los pedidos correctamente en objetos `Pedido`.

### Preferencias de usuario
- Define una clase `Usuario` con atributos `nombre` y `configuracion` (diccionario con claves como “tema”, “notificaciones”…).
  - Crea varias instancias y guárdalas en `usuarios.json`.
  - Implementa un método de lectura que cargue ese archivo y devuelva la lista de usuarios con sus configuraciones originales.

---

## Ficheros Binarios

### Almacenamiento binario de puntuaciones
- Crea una clase `Jugador` con atributos `nombre` y `puntuacion`.
  - Crea varios jugadores y guarda sus datos en un archivo binario usando el módulo `msgpack`.
  - Implementa un método que lea el archivo binario y reconstruya los objetos `Jugador` desde el almacenamiento.

### Historial de sensores
- Define una clase `LecturaSensor` con atributos `id_sensor`, `timestamp` y `valor`.
  - Genera varias lecturas y guárdalas en un archivo binario usando `struct` para escribir datos primitivos (enteros, flotantes, cadenas).
  - Implementa un método que lea el archivo binario y reconstruya las lecturas originales.
