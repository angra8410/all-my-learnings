# Módulo 1: Introducción a Docker

## Introducción

¡Bienvenido al emocionante mundo de Docker! En este primer módulo aprenderás:

- ¿Qué es Docker y por qué revolucionó el desarrollo de software?
- Conceptos fundamentales: contenedores vs máquinas virtuales
- La arquitectura de Docker
- Instalación y primeros pasos
- Tu primer contenedor

## ¿Por qué es importante?

Docker ha transformado la forma en que desarrollamos, distribuimos y ejecutamos aplicaciones. Permite:

- **Consistencia**: "Funciona en mi máquina" ya no es excusa
- **Portabilidad**: La misma aplicación corre en cualquier lugar
- **Eficiencia**: Uso óptimo de recursos
- **Velocidad**: De código a producción en minutos
- **Aislamiento**: Cada aplicación en su propio entorno

## Conceptos Principales

### 1. ¿Qué es Docker?

**Docker** es una plataforma que permite empaquetar aplicaciones y sus dependencias en contenedores ligeros y portables.

**Analogía**: Imagina que Docker es como un contenedor de transporte marítimo. No importa qué haya dentro (ropa, electrónicos, muebles), el contenedor tiene un tamaño estándar que puede ser transportado por cualquier barco, tren o camión. De la misma manera, Docker empaqueta tu aplicación (código, librerías, configuración) en un formato estándar que puede ejecutarse en cualquier servidor.

**Ejemplo básico:**
```bash
# Ejecutar tu primera aplicación en Docker
docker run hello-world
```

Este simple comando descarga una imagen de prueba y ejecuta un contenedor que imprime un mensaje de bienvenida.

### 2. Contenedores vs Máquinas Virtuales

**Máquinas Virtuales (VMs):**
```
┌─────────────────────────────────────┐
│         Aplicación A                │
│    ┌──────────────────────┐         │
│    │   Sistema Operativo  │         │
│    │     Completo (GB)    │         │
│    └──────────────────────┘         │
│         Hypervisor                  │
│    Hardware Físico                  │
└─────────────────────────────────────┘
```

**Contenedores Docker:**
```
┌─────────────────────────────────────┐
│  App A  │  App B  │  App C          │
│ (Solo lo│ (Solo lo│ (Solo lo        │
│necesario)│necesario)│necesario)      │
├─────────┴─────────┴─────────────────┤
│      Motor de Docker                │
│    Sistema Operativo Host           │
│    Hardware Físico                  │
└─────────────────────────────────────┘
```

**Diferencias clave:**

| Característica | Máquina Virtual | Contenedor Docker |
|---------------|----------------|-------------------|
| **Tamaño** | GBs | MBs |
| **Arranque** | Minutos | Segundos |
| **Recursos** | Alto consumo | Ligero |
| **Aislamiento** | Completo (OS separado) | Proceso aislado |
| **Portabilidad** | Limitada | Alta |

### 3. Arquitectura de Docker

```
┌──────────────────────────────────────────────┐
│           Docker Client (CLI)                │
│         docker build, run, push              │
└────────────────┬─────────────────────────────┘
                 │
                 ↓
┌──────────────────────────────────────────────┐
│          Docker Daemon (Engine)              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Container │  │Container │  │Container │   │
│  │    1     │  │    2     │  │    3     │   │
│  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│         Docker Registry (Docker Hub)         │
│           Almacén de Imágenes                │
└──────────────────────────────────────────────┘
```

**Componentes principales:**

1. **Docker Client**: La interfaz de línea de comandos que usas
2. **Docker Daemon**: El motor que ejecuta los contenedores
3. **Docker Registry**: Repositorio de imágenes (como Docker Hub)
4. **Imágenes**: Plantillas de solo lectura
5. **Contenedores**: Instancias en ejecución de imágenes

### 4. Conceptos Fundamentales

**Imagen:**
- Plantilla de solo lectura
- Contiene el sistema de archivos y configuración
- Se construye por capas
- Ejemplo: `nginx:latest`, `python:3.9`, `ubuntu:22.04`

**Contenedor:**
- Instancia en ejecución de una imagen
- Tiene su propio filesystem, networking y proceso
- Es efímero por defecto
- Puedes tener múltiples contenedores de la misma imagen

**Analogía de imagen vs contenedor:**
- **Imagen** = Receta de cocina (instrucciones)
- **Contenedor** = Plato preparado (resultado ejecutándose)

### 5. Ciclo de Vida de un Contenedor

```
Crear → Iniciar → Ejecutar → Pausar → Detener → Eliminar
  ↓        ↓         ↓         ↓         ↓         ↓
Created  Running   Running  Paused   Stopped   Removed
```

**Comandos básicos:**

```bash
# Crear y ejecutar contenedor
docker run -d --name mi-contenedor nginx

# Listar contenedores en ejecución
docker ps

# Listar todos los contenedores
docker ps -a

# Detener contenedor
docker stop mi-contenedor

# Iniciar contenedor detenido
docker start mi-contenedor

# Eliminar contenedor
docker rm mi-contenedor
```

## Implementación Práctica

### Ejercicio 1: Instalación de Docker

**En Linux (Ubuntu/Debian):**
```bash
# Actualizar paquetes
sudo apt-get update

# Instalar dependencias
sudo apt-get install ca-certificates curl gnupg

# Agregar clave GPG de Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Agregar repositorio
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Verificar instalación
docker --version
```

**En macOS/Windows:**
- Descargar Docker Desktop desde https://www.docker.com/products/docker-desktop
- Instalar y seguir el asistente
- Verificar con `docker --version`

### Ejercicio 2: Tu primer contenedor

```bash
# Ejecutar contenedor de prueba
docker run hello-world

# Salida esperada:
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

**¿Qué pasó?**
1. Docker buscó la imagen `hello-world` localmente
2. No la encontró, así que la descargó de Docker Hub
3. Creó un nuevo contenedor de esa imagen
4. Ejecutó el contenedor, que mostró el mensaje
5. El contenedor terminó su ejecución

### Ejercicio 3: Servidor web con Nginx

```bash
# Ejecutar servidor Nginx
docker run -d -p 8080:80 --name mi-servidor-web nginx

# Explicación:
# -d: Ejecutar en segundo plano (detached)
# -p 8080:80: Mapear puerto 8080 del host al 80 del contenedor
# --name: Dar un nombre al contenedor
# nginx: La imagen a usar
```

**Probar:**
- Abre tu navegador en `http://localhost:8080`
- ¡Deberías ver la página de bienvenida de Nginx!

**Comandos útiles:**
```bash
# Ver logs del contenedor
docker logs mi-servidor-web

# Ejecutar comando dentro del contenedor
docker exec -it mi-servidor-web bash

# Ver información detallada
docker inspect mi-servidor-web

# Detener y eliminar
docker stop mi-servidor-web
docker rm mi-servidor-web
```

### Ejercicio 4: Explorar imágenes disponibles

```bash
# Buscar imágenes en Docker Hub
docker search python

# Descargar una imagen sin ejecutarla
docker pull python:3.9

# Ver imágenes descargadas
docker images

# Eliminar una imagen
docker rmi python:3.9
```

### Ejercicio 5: Contenedor interactivo

```bash
# Ejecutar contenedor de Ubuntu de forma interactiva
docker run -it ubuntu bash

# Ahora estás dentro del contenedor
# Prueba comandos:
ls
pwd
cat /etc/os-release
apt-get update
apt-get install curl -y
curl --version

# Salir del contenedor
exit
```

## Mejores Prácticas

1. **Usa nombres descriptivos para contenedores**
   ```bash
   # ❌ Evitar
   docker run -d nginx
   
   # ✅ Mejor
   docker run -d --name blog-frontend nginx
   ```

2. **Especifica versiones de imágenes**
   ```bash
   # ❌ Evitar (usa 'latest')
   docker run nginx
   
   # ✅ Mejor (versión específica)
   docker run nginx:1.24
   ```

3. **Limpia contenedores e imágenes no usados**
   ```bash
   # Eliminar contenedores detenidos
   docker container prune
   
   # Eliminar imágenes sin usar
   docker image prune
   
   # Limpieza completa (¡cuidado!)
   docker system prune -a
   ```

4. **No ejecutes como root en producción**
   - Usa usuarios no privilegiados dentro de contenedores
   - Aprenderás más sobre esto en módulos avanzados

5. **Monitorea recursos**
   ```bash
   # Ver uso de recursos
   docker stats
   
   # Ver uso por contenedor
   docker stats mi-servidor-web
   ```

## Comandos Esenciales - Referencia Rápida

```bash
# IMÁGENES
docker images                    # Listar imágenes
docker pull <imagen>             # Descargar imagen
docker rmi <imagen>              # Eliminar imagen
docker search <término>          # Buscar imágenes

# CONTENEDORES
docker run <opciones> <imagen>   # Crear y ejecutar
docker ps                        # Listar en ejecución
docker ps -a                     # Listar todos
docker stop <contenedor>         # Detener
docker start <contenedor>        # Iniciar
docker restart <contenedor>      # Reiniciar
docker rm <contenedor>           # Eliminar
docker logs <contenedor>         # Ver logs
docker exec -it <contenedor> bash # Entrar al contenedor

# INFORMACIÓN
docker version                   # Versión de Docker
docker info                      # Información del sistema
docker inspect <contenedor>      # Detalles del contenedor
docker stats                     # Uso de recursos

# LIMPIEZA
docker container prune           # Limpiar contenedores detenidos
docker image prune              # Limpiar imágenes sin usar
docker system prune             # Limpieza general
```

## Conceptos clave para recordar

- 🔑 **Docker**: Plataforma para ejecutar aplicaciones en contenedores
- 🔑 **Contenedor**: Instancia ligera y portable de una aplicación
- 🔑 **Imagen**: Plantilla de solo lectura para crear contenedores
- 🔑 **Docker Hub**: Registro público de imágenes Docker
- 🔑 **Aislamiento**: Contenedores corren independientemente
- 🔑 **Portabilidad**: El mismo contenedor corre en cualquier lugar
- 🔑 **Eficiencia**: Más ligero que máquinas virtuales

## Términos Importantes

- **Container**: Entorno aislado para ejecutar aplicaciones
- **Image**: Plantilla inmutable con el código y dependencias
- **Registry**: Repositorio de imágenes (Docker Hub, privados)
- **Daemon**: Servicio que gestiona contenedores
- **Client**: CLI para interactuar con Docker
- **Layer**: Capa de filesystem en una imagen
- **Tag**: Versión/etiqueta de una imagen (ej: `latest`, `1.0`)

## Próximos pasos

En el Módulo 2 aprenderás sobre:
- Trabajar con imágenes en profundidad
- Cómo funcionan las capas de imágenes
- Gestión avanzada de contenedores
- Networking básico entre contenedores
- Persistencia de datos

**¿Qué necesitas saber antes de continuar?**
✅ Tener Docker instalado y funcionando  
✅ Entender qué es un contenedor  
✅ Poder ejecutar `docker run` básico  
✅ Saber listar y eliminar contenedores  
✅ Comprender la diferencia entre imagen y contenedor  

## Recursos Adicionales

- 📚 [Documentación oficial de Docker](https://docs.docker.com/)
- 🎥 [Docker 101 Tutorial](https://www.docker.com/101-tutorial)
- 🐳 [Docker Hub](https://hub.docker.com/)
- 💡 [Play with Docker](https://labs.play-with-docker.com/) - Laboratorio gratuito online
- 📖 [Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)

---

**¡Felicidades por dar tus primeros pasos en Docker! 🐳**

La containerización es una habilidad fundamental en el desarrollo moderno. Sigue practicando y pronto estarás creando tus propias imágenes y orquestando aplicaciones complejas.

**¡Nos vemos en el Módulo 2!** 🚀
