# Retroalimentación y Soluciones - Módulo 2: .NET y Configuración

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es .NET?
**Respuesta correcta: B) Una plataforma de desarrollo**

**Explicación**: .NET es una plataforma completa que incluye herramientas, bibliotecas y un runtime para desarrollar diferentes tipos de aplicaciones. No es un lenguaje (eso es C#), ni un sistema operativo, ni un editor.

---

### Pregunta 2: ¿Cuál es la diferencia entre .NET SDK y .NET Runtime?
**Respuesta correcta: B) SDK es para desarrollar, Runtime es para ejecutar aplicaciones**

**Explicación**: El SDK (Software Development Kit) incluye todas las herramientas para desarrollar: compilador, CLI, bibliotecas. El Runtime solo contiene lo necesario para ejecutar aplicaciones ya compiladas. Como desarrollador, necesitas el SDK.

---

### Pregunta 3: ¿Qué lenguaje de programación se usa principalmente con .NET?
**Respuesta correcta: C) C#**

**Explicación**: C# (pronunciado "C Sharp") es el lenguaje principal de .NET. Aunque también puedes usar F# y VB.NET, C# es el más popular y el que usaremos en este curso.

---

### Pregunta 4: ¿Qué framework de .NET se usa específicamente para crear APIs web?
**Respuesta correcta: B) ASP.NET Core**

**Explicación**: ASP.NET Core es el framework diseñado para aplicaciones web y APIs. Entity Framework es para bases de datos, Xamarin es para móviles, y .NET Framework es la versión antigua.

---

### Pregunta 5: ¿En qué sistemas operativos puede funcionar .NET actualmente?
**Respuesta correcta: C) Windows, Linux y macOS**

**Explicación**: .NET moderno (desde .NET Core) es completamente multiplataforma. Puedes desarrollar y ejecutar aplicaciones en los tres sistemas operativos principales.

---

### Pregunta 6: ¿Qué comando usas para verificar la versión de .NET instalada?
**Respuesta correcta: B) `dotnet --version`**

**Explicación**: El comando correcto incluye dos guiones antes de "version". Este es el estándar para flags en CLI. Aunque `dotnet --info` también funciona, `--version` es más directo.

---

### Pregunta 7: ¿Qué comando crea un nuevo proyecto de API web?
**Respuesta correcta: C) `dotnet new webapi`**

**Explicación**: La sintaxis es `dotnet new [plantilla]`. Las plantillas usan nombres compuestos como "webapi", "console", "mvc", etc.

---

### Pregunta 8: ¿Qué archivo contiene la configuración de un proyecto .NET?
**Respuesta correcta: B) `.csproj`**

**Explicación**: El archivo .csproj (C# Project) es un archivo XML que define las propiedades del proyecto, dependencias, versión de .NET, etc.

---

## Sección 2: Respuestas a Analogías

### Analogía 1: .NET es a desarrollo de software como __________ es a construcción
**Respuesta correcta: C) Caja de herramientas**

**Explicación**: Así como una caja de herramientas te proporciona todo lo necesario para construir, .NET te proporciona todo lo necesario para desarrollar software.

---

### Analogía 2: SDK es a desarrollador como __________ es a conductor
**Respuesta correcta: B) Automóvil completo con manual**

**Explicación**: El SDK es el paquete completo con todo lo necesario para desarrollar, igual que un auto completo es todo lo que necesita un conductor. El Runtime sería solo la gasolina.

---

### Analogía 3: C# es a .NET como __________ es a automóvil
**Respuesta correcta: B) Volante y pedales**

**Explicación**: C# es la interfaz que usas para controlar la plataforma .NET, igual que el volante y pedales son la interfaz para controlar un automóvil.

---

### Analogía 4: Runtime es a aplicación como __________ es a electrodoméstico
**Respuesta correcta: B) Electricidad**

**Explicación**: El Runtime proporciona el "poder" necesario para que tu aplicación funcione, igual que la electricidad para un electrodoméstico.

---

### Analogía 5: ASP.NET Core es a APIs como __________ es a construcción
**Respuesta correcta: B) Herramientas especializadas para plomería**

**Explicación**: ASP.NET Core es un conjunto especializado de herramientas dentro de .NET específicamente para construir APIs y aplicaciones web.

---

## Sección 3: Asociación de Términos con Definiciones

**Respuestas correctas**:
1 → C (SDK = Kit de desarrollo con compilador y herramientas)  
2 → H (Runtime = Motor que ejecuta aplicaciones .NET)  
3 → A (C# = Lenguaje de programación orientado a objetos)  
4 → E (ASP.NET Core = Framework para APIs y aplicaciones web)  
5 → G (CLI = Herramienta de línea de comandos)  
6 → B (.csproj = Archivo de configuración del proyecto)  
7 → F (Visual Studio Code = Editor de código gratuito)  
8 → D (LTS = Versión con soporte a largo plazo)  

---

## Sección 4: Verdadero o Falso

1. **F (Falso)** - .NET ahora es multiplataforma (Windows, Linux, macOS)

2. **V (Verdadero)** - El SDK contiene todo lo necesario para desarrollar

3. **F (Falso)** - El Runtime solo sirve para ejecutar, no para desarrollar

4. **F (Falso)** - C# es el lenguaje, .NET es la plataforma

5. **F (Falso)** - VS Code es completamente gratuito y de código abierto

6. **V (Verdadero)** - `dotnet run` compila y ejecuta en un solo comando

7. **V (Verdadero)** - .NET 8 es una versión LTS con soporte extendido

8. **F (Falso)** - ASP.NET Core sirve principalmente para APIs y aplicaciones web

---

## Sección 5: Ejercicio Práctico - Comandos de Terminal

### Tarea 1: Verificar versión instalada
**Comando correcto**: `dotnet --version`

---

### Tarea 2: Ver información detallada
**Comando correcto**: `dotnet --info`

---

### Tarea 3: Crear proyecto de API web
**Comando correcto**: `dotnet new webapi -n TiendaAPI`

**Nota**: El flag `-n` especifica el nombre del proyecto.

---

### Tarea 4: Ejecutar proyecto
**Comando correcto**: `dotnet run`

**Nota**: Debes estar dentro de la carpeta del proyecto.

---

### Tarea 5: Ver plantillas disponibles
**Comando correcto**: `dotnet new list` o `dotnet new --list`

---

### Tarea 6: Compilar sin ejecutar
**Comando correcto**: `dotnet build`

---

## Sección 6: Identificación de Componentes

### Escenario 1: Ejecutar una aplicación descargada
**Respuesta correcta: B) Solo .NET Runtime**

**Explicación**: Para solo ejecutar aplicaciones, el Runtime es suficiente. El SDK es necesario solo para desarrollo.

---

### Escenario 2: Crear y modificar tu propia API
**Respuesta correcta: B) .NET SDK + Editor de código**

**Explicación**: Para desarrollar necesitas el SDK (herramientas de desarrollo) y un editor para escribir código cómodamente.

---

### Escenario 3: Escribir código con autocompletado
**Respuesta correcta: C) VS Code con extensión de C#**

**Explicación**: El autocompletado y detección de errores lo proporciona la extensión de C# en VS Code, que utiliza el SDK instalado.

---

## Sección 7: Solución de Problemas

### Problema 1: "comando no reconocido"
**Respuesta correcta: B) Cerrar y abrir de nuevo la terminal**

**Explicación**: Al instalar .NET, se actualiza el PATH del sistema, pero las terminales abiertas no detectan el cambio hasta que se reinician. Esta es la solución más rápida y común.

---

### Problema 2: "No se pudo encontrar el proyecto"
**Respuesta correcta: B) No estás en la carpeta correcta del proyecto**

**Explicación**: `dotnet run` busca el archivo .csproj en la carpeta actual. Si no lo encuentra, muestra este error. Usa `cd` para navegar a la carpeta correcta.

---

### Problema 3: No hay autocompletado en VS Code
**Respuesta correcta: B) Instalar la extensión de C# de Microsoft en VS Code**

**Explicación**: VS Code por sí solo no sabe trabajar con C#. Necesitas la extensión oficial de Microsoft que proporciona IntelliSense y otras características.

---

## Evaluación de tu Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
¡Felicitaciones! Has comprendido muy bien los fundamentos de .NET y cómo configurar tu entorno. Estás más que listo para comenzar a desarrollar APIs.

**Próximos pasos**:
- Familiarízate con los comandos de terminal
- Explora VS Code y sus atajos de teclado
- Prepárate para crear tu primera API en el próximo módulo

---

### Si acertaste entre 70% y 89%: 💪 ¡Muy bien!
Has captado la mayoría de los conceptos importantes. Solo necesitas aclarar algunos detalles.

**Recomendaciones**:
- Repasa las diferencias entre SDK y Runtime
- Practica los comandos básicos de .NET CLI
- Asegúrate de entender qué es cada componente (.NET, C#, ASP.NET Core)

---

### Si acertaste entre 50% y 69%: 📚 Sigue adelante
Tienes una comprensión básica, pero necesitas reforzar conceptos fundamentales.

**Recomendaciones**:
- Lee de nuevo el README.md con calma
- Enfócate en las analogías (caja de herramientas, automóvil, electricidad)
- Practica instalando .NET y ejecutando comandos básicos
- No avances hasta sentirte cómodo con la instalación

---

### Si acertaste menos de 50%: 🔄 Repaso necesario
No te preocupes, la configuración de entornos puede ser confusa al principio.

**Recomendaciones**:
- Vuelve al README.md y sigue los pasos de instalación uno por uno
- Practica cada comando en tu terminal
- Pide ayuda si tienes problemas con la instalación
- Ve videos tutoriales sobre instalación de .NET en tu sistema operativo específico
- No avances al siguiente módulo sin tener .NET funcionando correctamente

---

## Consejos Generales para Avanzar

### 💡 Para todos los niveles:

1. **Practica los comandos**: Abre tu terminal y ejecuta comandos hasta que te sientas cómodo.

2. **Experimenta creando proyectos**: Crea varios proyectos de prueba con diferentes plantillas.

3. **Familiarízate con VS Code**: Aprende los atajos básicos (Ctrl+P para buscar archivos, Ctrl+Shift+P para comandos).

4. **Documenta tus problemas**: Si algo no funciona, anota el error exacto en el archivo `progreso.md`.

5. **No te frustres**: Todos tienen problemas con la configuración inicial. Es normal.

---

## Recursos Adicionales Recomendados

### Videos (búscalos en YouTube):
- "Cómo instalar .NET 8 en [tu sistema operativo]"
- "Primeros pasos con .NET - Tutorial en español"
- "Configurar VS Code para .NET"

### Documentación:
- Guía oficial de instalación: https://docs.microsoft.com/dotnet/core/install/
- Tutoriales de .NET: https://dotnet.microsoft.com/learn
- Documentación de VS Code: https://code.visualstudio.com/docs

### Comunidades:
- Stack Overflow (etiqueta `.net`)
- Reddit: r/dotnet
- Discord de .NET en español

---

## Verificación de Prerequisitos para el Siguiente Módulo

Antes de avanzar al Módulo 3 (Tu primera API), asegúrate de:

✅ Tener .NET 8 SDK instalado (`dotnet --version` funciona)  
✅ Tener Visual Studio Code instalado  
✅ Tener la extensión de C# instalada en VS Code  
✅ Poder ejecutar `dotnet new console -n Test`  
✅ Poder ejecutar `dotnet run` en un proyecto de prueba  
✅ Entender la diferencia entre SDK y Runtime  
✅ Conocer los comandos básicos de .NET CLI  

---

## Preparación para el Siguiente Módulo

En el Módulo 3 vas a:
- Crear tu primera API REST desde cero
- Entender la estructura de un proyecto de API
- Hacer peticiones HTTP a tu propia API
- Ver tu API funcionando en el navegador

**¿Qué necesitas tener listo?**
- Una carpeta organizada para tus proyectos .NET
- Postman o navegador para probar APIs
- Ganas de escribir tu primer código C#

---

¡Excelente trabajo completando este módulo! La configuración del entorno es el primer paso importante. Ahora estás listo para crear cosas increíbles. 🚀

**¿Listo para crear tu primera API?** ¡Nos vemos en el Módulo 3! 💙
