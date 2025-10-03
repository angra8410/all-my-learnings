# Módulo 2: ¿Qué es .NET? Instalación y configuración del entorno

## ¿Qué es .NET?

Imagina que quieres construir una casa. Podrías fabricar cada ladrillo, cada ventana y cada puerta desde cero... ¡pero eso tomaría años! En cambio, usas **materiales y herramientas** que ya existen. .NET es exactamente eso para el desarrollo de software: una **plataforma** que te proporciona todas las herramientas y componentes necesarios para construir aplicaciones de manera rápida y eficiente.

**.NET** es una plataforma de desarrollo **gratuita y de código abierto** creada por Microsoft que te permite construir diferentes tipos de aplicaciones:
- APIs web (¡lo que aprenderemos!)
- Aplicaciones de escritorio
- Aplicaciones móviles
- Juegos
- Aplicaciones en la nube
- Y mucho más...

### ¿Por qué usar .NET para APIs?

1. **Rendimiento excepcional**: .NET es una de las plataformas más rápidas para construir APIs
2. **Multiplataforma**: Funciona en Windows, Linux y macOS
3. **Comunidad grande**: Millones de desarrolladores usan .NET, hay mucha ayuda disponible
4. **Herramientas gratuitas**: Todo lo que necesitas es gratuito (Visual Studio Code, .NET SDK)
5. **Soporte empresarial**: Microsoft y grandes empresas lo respaldan

### Analogía: .NET como una Caja de Herramientas

Piensa en .NET como una **caja de herramientas profesional**:
- **SDK (Software Development Kit)**: Las herramientas básicas (martillo, destornillador)
- **Runtime**: El motor que hace que tu aplicación funcione (como la electricidad para tus herramientas)
- **Bibliotecas**: Componentes prefabricados (tornillos, clavos, bisagras)
- **ASP.NET Core**: Herramientas especializadas para construir APIs y aplicaciones web

## Componentes principales de .NET

### 1. .NET SDK (Kit de Desarrollo)
El SDK incluye todo lo que necesitas para **desarrollar** aplicaciones:
- Compilador (traduce tu código a lenguaje que la computadora entiende)
- Herramientas de línea de comandos (CLI)
- Bibliotecas base

### 2. .NET Runtime (Tiempo de Ejecución)
El runtime es lo que necesitas para **ejecutar** aplicaciones .NET:
- Ejecuta tu código compilado
- Gestiona memoria automáticamente
- Proporciona servicios básicos

### 3. ASP.NET Core
Es el framework específico para construir **aplicaciones web y APIs**:
- Sistema de enrutamiento
- Manejo de peticiones HTTP
- Inyección de dependencias
- Middleware y configuración

## ¿C# o .NET? ¿Cuál es la diferencia?

Esta es una pregunta común que confunde a muchos principiantes:

- **.NET**: Es la **plataforma** (como Android)
- **C#**: Es el **lenguaje de programación** (como Java o Kotlin para Android)

**Analogía**: 
- .NET es como un **automóvil** (la plataforma)
- C# es como el **volante y pedales** (la forma en que lo controlas)

Usarás C# para escribir código que se ejecuta en la plataforma .NET.

## Versiones de .NET: Una breve historia

No te preocupes por los detalles históricos, solo necesitas saber:

- **.NET Framework** (antiguo): Solo funcionaba en Windows
- **.NET Core** (2016-2020): Rediseño moderno y multiplataforma
- **.NET 5/6/7/8+** (actual): La evolución de .NET Core (eliminaron "Core" del nombre)

**¡Usaremos .NET 8!** Es la versión LTS (Long Term Support) más reciente, lo que significa que tendrá soporte por varios años.

## Requisitos del sistema

Antes de instalar, asegúrate de tener:

### Requisitos mínimos:
- **Sistema Operativo**: Windows 10/11, macOS 10.15+, o Linux (Ubuntu, Debian, etc.)
- **RAM**: 4GB mínimo (8GB recomendado)
- **Espacio en disco**: Al menos 2GB libres
- **Conexión a internet**: Para descargar instaladores y paquetes

## Instalación paso a paso

### Paso 1: Descargar .NET SDK

1. Ve a la página oficial: **https://dotnet.microsoft.com/download**
2. Descarga **.NET 8.0 SDK** (no solo el Runtime)
3. Elige la versión para tu sistema operativo

**Importante**: Descarga el **SDK**, no solo el Runtime. El SDK incluye todo lo necesario para desarrollar.

### Paso 2: Instalar .NET SDK

**En Windows:**
1. Ejecuta el instalador descargado (.exe)
2. Sigue el asistente (Next, Next, Install)
3. Espera a que termine la instalación

**En macOS:**
1. Abre el archivo .pkg descargado
2. Sigue las instrucciones del instalador
3. Es posible que necesites permisos de administrador

**En Linux (Ubuntu/Debian):**
```bash
# Agrega el repositorio de Microsoft
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

# Instala el SDK
sudo apt-get update
sudo apt-get install -y dotnet-sdk-8.0
```

### Paso 3: Verificar la instalación

Abre una **terminal** o **línea de comandos** y ejecuta:

```bash
dotnet --version
```

Deberías ver algo como: `8.0.xxx`

Si ves la versión, ¡felicidades! .NET está instalado correctamente.

### Paso 4: Verificar que todo funciona

Ejecuta este comando para ver información completa:

```bash
dotnet --info
```

Verás información sobre:
- Versión del SDK instalado
- Versión del Runtime
- Tu sistema operativo
- Arquitectura (x64, ARM, etc.)

## Instalación del Editor de Código

Necesitas un editor para escribir código. **Visual Studio Code** es perfecto para empezar:

### Instalar VS Code

1. Ve a: **https://code.visualstudio.com/**
2. Descarga la versión para tu sistema operativo
3. Instala siguiendo el asistente

### Extensiones esenciales para VS Code

Una vez instalado VS Code, instala estas extensiones:

1. **C# (Microsoft)**
   - Abre VS Code
   - Ve a la pestaña de Extensiones (Ctrl+Shift+X)
   - Busca "C#" y selecciona la de Microsoft
   - Haz clic en "Install"

2. **C# Dev Kit (Microsoft)** - Opcional pero recomendado
   - Proporciona más herramientas para trabajar con C#

Estas extensiones te darán:
- Autocompletado de código
- Detección de errores en tiempo real
- Depuración
- Snippets y atajos útiles

## Tu primer comando .NET

Vamos a crear un proyecto de prueba para asegurarnos de que todo funciona:

```bash
# Crea una carpeta para tus proyectos
mkdir mis-proyectos-dotnet
cd mis-proyectos-dotnet

# Crea un proyecto de consola simple
dotnet new console -n HolaMundo

# Entra a la carpeta del proyecto
cd HolaMundo

# Ejecuta el proyecto
dotnet run
```

Deberías ver en la terminal: `Hello, World!`

¡Felicidades! Acabas de ejecutar tu primer programa en .NET 🎉

## Estructura de un proyecto .NET

Cuando creas un proyecto, .NET genera varios archivos:

```
HolaMundo/
├── HolaMundo.csproj    # Archivo de configuración del proyecto
├── Program.cs          # Tu código principal
└── obj/                # Archivos temporales de compilación (no los toques)
```

- **`.csproj`**: Define las propiedades del proyecto (versión de .NET, dependencias)
- **`Program.cs`**: Aquí escribes tu código C#
- **`obj/` y `bin/`**: Carpetas generadas automáticamente (no las edites)

## Comandos básicos de .NET CLI

La CLI (Command Line Interface) de .NET es muy poderosa. Aquí están los comandos esenciales:

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `dotnet new` | Crea un nuevo proyecto | `dotnet new webapi -n MiAPI` |
| `dotnet run` | Compila y ejecuta el proyecto | `dotnet run` |
| `dotnet build` | Compila el proyecto | `dotnet build` |
| `dotnet restore` | Descarga dependencias | `dotnet restore` |
| `dotnet clean` | Limpia archivos compilados | `dotnet clean` |
| `dotnet --help` | Muestra ayuda | `dotnet new --help` |

## Tipos de proyectos que puedes crear

.NET tiene plantillas para diferentes tipos de proyectos:

```bash
# Ver todas las plantillas disponibles
dotnet new list
```

Algunos tipos importantes:
- **`console`**: Aplicación de consola simple
- **`webapi`**: API RESTful (¡esto es lo que aprenderemos!)
- **`mvc`**: Aplicación web MVC
- **`classlib`**: Biblioteca de clases
- **`xunit`**: Proyecto de pruebas

## Solución de problemas comunes

### Problema: "dotnet no se reconoce como comando"

**Solución**:
1. Cierra y vuelve a abrir la terminal
2. Verifica que .NET esté en el PATH del sistema
3. Reinicia tu computadora si es necesario

### Problema: Error al ejecutar `dotnet run`

**Solución**:
1. Asegúrate de estar en la carpeta correcta del proyecto
2. Ejecuta `dotnet restore` primero
3. Verifica que el archivo `.csproj` existe

### Problema: VS Code no reconoce C#

**Solución**:
1. Instala la extensión C# de Microsoft
2. Reinicia VS Code
3. Abre una carpeta con un proyecto .NET

## Conceptos clave para recordar

- 🔑 **.NET**: Plataforma de desarrollo gratuita y multiplataforma
- 🔑 **SDK**: Kit de desarrollo con todas las herramientas
- 🔑 **Runtime**: Lo que necesitas para ejecutar aplicaciones
- 🔑 **C#**: Lenguaje de programación que usamos con .NET
- 🔑 **ASP.NET Core**: Framework para APIs y aplicaciones web
- 🔑 **CLI**: Herramienta de línea de comandos (`dotnet`)
- 🔑 **VS Code**: Editor de código recomendado

## Recursos adicionales

- **Documentación oficial**: https://docs.microsoft.com/dotnet/
- **Tutorial interactivo**: https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial
- **Comunidad**: https://dotnet.microsoft.com/platform/community

## Próximos pasos

Ahora que tienes .NET instalado y configurado:
- Completa las actividades interactivas para reforzar conceptos
- Familiarízate con la terminal y los comandos básicos
- En el próximo módulo crearás tu primera API REST

¡Estás listo para empezar a construir! 🚀
