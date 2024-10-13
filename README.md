# CI3641-examen1
## Universidad Simón Bolívar
### Lenguajes de Programación I
**Fredthery Castro 18-10783**

## Tarea 1

### Pregunta 1

El lenguaje de programación escogido fue F#.

#### i. Alcances y Asociaciones

**Alcances:**

- F# utiliza un sistema de alcance léxico (también conocido como estático). Esto significa que el alcance de las variables está determinado por la estructura del código, y no por el flujo de ejecución.

**Ventajas:**

- **Previsibilidad:** Facilita la comprensión del código, ya que el alcance de las variables es claro y no cambia durante la ejecución.
- **Mantenimiento:** Mejora la mantenibilidad del código, ya que las dependencias y las relaciones entre las variables son más evidentes.

**Desventajas:**

- **Limitaciones en Flexibilidad:** Puede ser menos flexible en situaciones donde se requiere cambiar dinámicamente el alcance de las variables, aunque esto no es un problema común en los escenarios típicos de F#.

**Asociaciones:**

- F# permite tanto la asociación implícita como explícita de tipos, lo que beneficia a los usuarios que desean aprovechar el tipado fuerte y estático del lenguaje sin tener que especificar siempre los tipos.

#### ii. Módulos

**Tipos de Módulos:**

- F# ofrece módulos que permiten agrupar funciones, tipos y valores. Los módulos son una forma de organizar el código y pueden anidarse.

**Importar y Exportar Nombres:**

- **Abrir Módulos:** Se usa la palabra clave `open` para importar nombres de un módulo.
- **Exportar Nombres:** Los nombres definidos en un módulo son accesibles desde fuera del módulo, a menos que se especifiquen como privados.

#### iii. Aliases, Sobrecarga y Polimorfismo

**Aliases:**

- F# permite crear aliases para tipos utilizando la palabra clave `type`.

  ```fsharp
  type StringAlias = string

**Sobrecarga:**

- F# soporta la sobrecarga de operadores, pero no de funciones en general. Se utiliza principalmente para operadores matemáticos.
  ```fsharp
  let sumar (x: int) (y: int) = x + y
  let sumar (x: float) (y: float) = x + y

**Polimorfismo:**

- F# admite polimorfismo paramétrico, lo que permite definir funciones y tipos que funcionan con cualquier tipo de dato.

  ```fsharp
  let identity x = x

### Herramientas para Desarrolladores

- **Compiladores:**  
  F# se compila utilizando el compilador F# (parte de .NET SDK).

- **Intérpretes:**  
  F# Interactive (fsi) permite la ejecución interactiva de código F#.

- **Debuggers:**  
  Visual Studio y JetBrains Rider ofrecen capacidades de depuración para F#.

- **Profilers:**  
  .NET profilers, como el de Visual Studio, son compatibles con F#.

- **Frameworks:**  
  F# se integra con .NET, lo que permite el uso de una amplia gama de frameworks como ASP.NET y Xamarin.

- **Otros:**  
  Herramientas como Paket para la gestión de paquetes y FAKE para la automatización de tareas son populares en el ecosistema F#.
