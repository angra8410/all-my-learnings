# Actividades Interactivas - Módulo 1: Introducción a Docker

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es Docker?**

A) Un sistema operativo  
B) Una plataforma para ejecutar aplicaciones en contenedores  
C) Un lenguaje de programación  
D) Una base de datos

---

### Pregunta 2
**¿Cuál es la principal ventaja de Docker sobre las máquinas virtuales?**

A) Es más bonito  
B) Es más ligero y arranca más rápido  
C) Solo funciona en Linux  
D) No necesita sistema operativo

---

### Pregunta 3
**¿Qué es una imagen de Docker?**

A) Una foto del contenedor  
B) Una plantilla de solo lectura para crear contenedores  
C) Un contenedor en ejecución  
D) Un archivo de configuración

---

### Pregunta 4
**¿Qué comando usas para ejecutar un contenedor?**

A) docker start  
B) docker create  
C) docker run  
D) docker execute

---

### Pregunta 5
**¿Dónde se almacenan las imágenes de Docker públicas?**

A) Docker Store  
B) GitHub  
C) Docker Hub  
D) Docker Cloud

---

## Sección 2: Verdadero o Falso

### Afirmación 1
**Los contenedores Docker son más pesados que las máquinas virtuales.**

- [ ] Verdadero
- [ ] Falso

**Tu respuesta**: _______________________________________________

---

### Afirmación 2
**Un contenedor puede ejecutarse en cualquier máquina que tenga Docker instalado.**

- [ ] Verdadero
- [ ] Falso

**Tu respuesta**: _______________________________________________

---

### Afirmación 3
**Una imagen de Docker puede usarse para crear múltiples contenedores.**

- [ ] Verdadero
- [ ] Falso

**Tu respuesta**: _______________________________________________

---

### Afirmación 4
**El comando 'docker ps' muestra todos los contenedores, incluso los detenidos.**

- [ ] Verdadero
- [ ] Falso

**Tu respuesta**: _______________________________________________

---

### Afirmación 5
**Los contenedores comparten el kernel del sistema operativo host.**

- [ ] Verdadero
- [ ] Falso

**Tu respuesta**: _______________________________________________

---

## Sección 3: Completa la Analogía

### Analogía 1
**Docker es a aplicaciones como __________ es a productos físicos**

A) Un almacén  
B) Un contenedor de transporte marítimo  
C) Un camión  
D) Una fábrica  

**Tu respuesta**: _______________________________________________

**¿Por qué elegiste esa respuesta?**
_______________________________________________
_______________________________________________

---

### Analogía 2
**Imagen de Docker es a Contenedor como __________ es a __________**

Opciones:
- Receta → Plato preparado
- Libro → Lectura
- Plano → Casa construida
- Código → Programa ejecutándose

**Tu respuesta**: _______________________________________________

---

### Analogía 3
**Máquina Virtual es a Casa completa como Contenedor es a __________**

A) Apartamento (comparte estructura pero aislado)  
B) Terreno vacío  
C) Hotel  
D) Oficina  

**Tu respuesta**: _______________________________________________

---

## Sección 4: Asocia Comandos con Acciones

**Comandos:**
1. `docker run`
2. `docker ps`
3. `docker stop`
4. `docker rm`
5. `docker images`
6. `docker pull`
7. `docker logs`
8. `docker exec`

**Acciones:**
A) Ver logs de un contenedor  
B) Descargar una imagen sin ejecutarla  
C) Listar contenedores en ejecución  
D) Crear y ejecutar un contenedor  
E) Eliminar un contenedor  
F) Listar imágenes descargadas  
G) Detener un contenedor en ejecución  
H) Ejecutar un comando dentro de un contenedor  

**Tus respuestas:**
1 → ___  
2 → ___  
3 → ___  
4 → ___  
5 → ___  
6 → ___  
7 → ___  
8 → ___  

---

## Sección 5: Ejercicio Práctico - Comandos Docker

### Parte 1: Instalación y Verificación

**¿Instalaste Docker exitosamente?** (Sí/No)
_______________________________________________

**¿Qué versión de Docker tienes instalada?**
```bash
# Ejecuta: docker --version
```
Versión: _______________________________________________

**¿El comando `docker run hello-world` funcionó?** (Sí/No)
_______________________________________________

Si hubo errores, descríbelos:
_______________________________________________
_______________________________________________

---

### Parte 2: Ejecutar Nginx

**Ejecutaste el contenedor de Nginx con:**
```bash
docker run -d -p 8080:80 --name mi-servidor-web nginx
```

- [ ] Sí, funcionó correctamente
- [ ] No, tuve errores

**¿Pudiste ver la página de Nginx en http://localhost:8080?** (Sí/No)
_______________________________________________

**¿Qué ID tiene tu contenedor?**
```bash
# Ejecuta: docker ps
```
ID del contenedor: _______________________________________________

---

### Parte 3: Explorar el Contenedor

**Ejecuta estos comandos y anota los resultados:**

```bash
# 1. Ver logs
docker logs mi-servidor-web
```
**¿Qué viste en los logs?**
_______________________________________________
_______________________________________________

```bash
# 2. Ver estadísticas
docker stats mi-servidor-web --no-stream
```
**¿Cuánta memoria usa el contenedor?**
_______________________________________________

**¿Cuánto CPU?**
_______________________________________________

---

### Parte 4: Limpieza

**Detuviste y eliminaste el contenedor?**
```bash
docker stop mi-servidor-web
docker rm mi-servidor-web
```

- [ ] Sí, comandos ejecutados
- [ ] Tuve problemas

**¿Qué dice `docker ps -a` ahora?**
_______________________________________________

---

## Sección 6: Escenario Práctico

**Situación:**
Eres desarrollador en una startup. Tu equipo tiene:
- 3 desarrolladores con Windows
- 2 desarrolladores con macOS
- 1 desarrollador con Linux
- Un servidor de producción con Ubuntu

Todos necesitan ejecutar la misma aplicación Node.js con MongoDB.

**Preguntas:**

1. **¿Qué problemas podrías enfrentar sin Docker?**
_______________________________________________
_______________________________________________
_______________________________________________

2. **¿Cómo Docker resolvería estos problemas?**
_______________________________________________
_______________________________________________
_______________________________________________

3. **¿Qué imágenes de Docker necesitarías?**
- [ ] node
- [ ] mongodb
- [ ] nginx
- [ ] mysql

4. **¿Cuál sería el beneficio principal para tu equipo?**
_______________________________________________
_______________________________________________

---

## Sección 7: Diagrama de Flujo

**Completa el flujo de ejecución de `docker run nginx`:**

```
Usuario ejecuta: docker run nginx
        ↓
1. Docker busca la imagen localmente
        ↓
2. ¿Imagen encontrada?
   → No: _____________________
   → Sí: _____________________
        ↓
3. _____________________
        ↓
4. Contenedor en estado: _____________________
```

**Completa los espacios:**

Espacio en paso 2 (No encontrada): _______________________________________________

Espacio en paso 2 (Sí encontrada): _______________________________________________

Espacio en paso 3: _______________________________________________

Espacio en paso 4: _______________________________________________

---

## Sección 8: Resolución de Problemas

**Para cada error, identifica la solución:**

### Error 1
```
docker: Cannot connect to the Docker daemon. Is the docker daemon running?
```

**Causa probable**: _______________________________________________

**Solución**: _______________________________________________

---

### Error 2
```
docker: Error response from daemon: Conflict. The container name "/mi-web" is already in use.
```

**Causa probable**: _______________________________________________

**Solución**: _______________________________________________

---

### Error 3
```
Unable to find image 'ngnix:latest' locally
docker: Error response from daemon: pull access denied for ngnix, repository does not exist
```

**Causa probable**: _______________________________________________

**Solución**: _______________________________________________

---

## Sección 9: Comparación Contenedores vs VMs

**Completa la tabla:**

| Característica | Máquina Virtual | Contenedor Docker |
|----------------|----------------|-------------------|
| Tamaño típico  | ______________ | ______________ |
| Tiempo de inicio | ______________ | ______________ |
| Consumo de RAM | ______________ | ______________ |
| Aislamiento | ______________ | ______________ |
| Sistema Operativo | ______________ | ______________ |

---

## Sección 10: Mini-Proyecto Práctico

**Crea tu primer entorno multi-contenedor**

### Objetivo
Ejecutar 3 contenedores diferentes simultáneamente:
1. Un servidor web (nginx)
2. Una base de datos (mongo)
3. Un contenedor interactivo (ubuntu)

### Instrucciones

**Paso 1: Nginx en puerto 8080**
```bash
docker run -d -p 8080:80 --name web-server nginx
```
- [ ] Ejecutado correctamente
- [ ] Verificado en navegador

**Paso 2: MongoDB en puerto 27017**
```bash
docker run -d -p 27017:27017 --name mi-mongo mongo
```
- [ ] Ejecutado correctamente
- [ ] Verificado con `docker ps`

**Paso 3: Ubuntu interactivo**
```bash
docker run -it --name mi-ubuntu ubuntu bash
# (Esto abrirá una terminal interactiva)
```
- [ ] Entré al contenedor
- [ ] Ejecuté algunos comandos
- [ ] Salí con 'exit'

**Paso 4: Verificación**
```bash
docker ps -a
```

**¿Cuántos contenedores tienes?** _______________________________________________

**¿Cuántos están corriendo?** _______________________________________________

**¿Cuántos están detenidos?** _______________________________________________

**Paso 5: Limpieza**
```bash
docker stop web-server mi-mongo
docker rm web-server mi-mongo mi-ubuntu
```
- [ ] Todo limpiado correctamente

---

## Sección 11: Reflexión Personal

### Pregunta 1
**¿Qué concepto de Docker te pareció más interesante y por qué?**
_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 2
**¿En qué proyecto personal o del trabajo podrías usar Docker?**
_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 3
**¿Qué ventaja de Docker crees que es más valiosa?**
- [ ] Portabilidad
- [ ] Velocidad
- [ ] Consistencia
- [ ] Eficiencia de recursos
- [ ] Otra: _______________________________________________

**¿Por qué?**
_______________________________________________
_______________________________________________

---

### Pregunta 4
**¿Qué fue lo más difícil de entender en este módulo?**
_______________________________________________
_______________________________________________

**¿Cómo lo superaste o cómo planeas superarlo?**
_______________________________________________
_______________________________________________

---

## Sección 12: Desafío Extra (Opcional)

### Desafío 1: Explorar una Imagen
Ejecuta un contenedor de Python y explora sus capacidades:

```bash
docker run -it python:3.9 python
```

**¿Qué versión de Python se ejecutó?** _______________________________________________

**¿Pudiste ejecutar código Python?** (Sí/No) _______________________________________________

**Código que probaste:**
```python
# Escribe aquí el código que ejecutaste
```

---

### Desafío 2: Buscar Imágenes
Busca imágenes relacionadas con tu lenguaje favorito:

```bash
docker search <tu-lenguaje>
```

**Lenguaje buscado**: _______________________________________________

**3 imágenes populares que encontraste:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Desafío 3: Personalizar el Puerto
Ejecuta nginx en un puerto diferente (ej: 3000):

```bash
docker run -d -p 3000:80 --name nginx-custom nginx
```

**¿Funcionó en el nuevo puerto?** (Sí/No) _______________________________________________

**¿Qué URL usaste?** _______________________________________________

---

## Reflexión Final

**Califica tu comprensión del módulo (1-5):**

- Conceptos de Docker: ⭐ ⭐ ⭐ ⭐ ⭐
- Comandos básicos: ⭐ ⭐ ⭐ ⭐ ⭐
- Diferencia imagen/contenedor: ⭐ ⭐ ⭐ ⭐ ⭐
- Práctica con comandos: ⭐ ⭐ ⭐ ⭐ ⭐

**Lo que mejor aprendí:**
_______________________________________________
_______________________________________________

**Lo que necesito reforzar:**
_______________________________________________
_______________________________________________

**Mi siguiente paso será:**
_______________________________________________
_______________________________________________

---

¡Revisa tus respuestas en `retroalimentacion.md`! 🐳
