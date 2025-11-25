# Actividades Interactivas - Módulo 1: Introducción a CI/CD

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué significa CI en CI/CD?**

A) Code Integration  
B) Continuous Integration  
C) Computer Intelligence  
D) Complete Installation

B
---

### Pregunta 2
**¿Cuál es el principal beneficio de CI/CD?**

A) Hacer el código más largo  
B) Detectar errores temprano y entregar más rápido  
C) Eliminar la necesidad de pruebas  
D) Reducir el número de desarrolladores

B
---

### Pregunta 3
**¿Qué es un pipeline en CI/CD?**

A) Una tubería física para transportar datos  
B) Serie de pasos automatizados desde código hasta producción  
C) Un tipo de base de datos  
D) Un lenguaje de programación

B
---

### Pregunta 4
**¿Cuál de estas NO es una etapa típica del pipeline CI/CD?**

A) Build (Construcción)  
B) Test (Pruebas)  
C) Sleep (Dormir)  
D) Deploy (Despliegue)

C
---

### Pregunta 5
**¿Con qué frecuencia deberían hacerse commits en CI/CD?**

A) Una vez al mes  
B) Una vez terminado todo el proyecto  
C) Frecuentemente, con pequeños cambios  
D) Solo cuando hay errores

C
---

## Sección 2: Completa la Analogía

### Analogía 1
**CI/CD es a desarrollo de software como _______________ es a construcción de edificios.**

Pista: Piensa en construir piso por piso vs construir todo de una vez.

Tu respuesta: Maquinaria_______________________________________________

---

### Analogía 2
**Un pipeline CI/CD es como _______________**

Opciones: 
- Una línea de ensamblaje en una fábrica
- Un restaurante sin cocina
- Una biblioteca sin libros

Tu elección y por qué: Una Linea de ensamblaje en una fábrica, porque todo se tiene que hacer paso a paso, primero crea, revisa, haz pruebas y si sale todo bien, sale a producción.

---

### Analogía 3
**Desarrollo sin CI/CD es como _______________**

Opciones:
- Conducir con los ojos vendados
- Cocinar con todas las herramientas necesarias
- Estudiar con un buen plan

Tu elección y por qué: Conducir con los ojos vendados, todo tiene que ser encomendado a la suerte y un cruce de dedos que de.

---

## Sección 3: Verdadero o Falso

1. **CI/CD elimina completamente la necesidad de hacer pruebas manuales.** 
   - [x] Verdadero
   - [] Falso

2. **Un pipeline CI/CD puede ejecutarse automáticamente al hacer push al repositorio.**
   - [x] Verdadero
   - [ ] Falso

3. **CI/CD solo funciona con aplicaciones web.**
   - [ ] Verdadero
   - [x] Falso

4. **Los artefactos son los resultados compilados listos para desplegar.**
   - [x] Verdadero
   - [ ] Falso

5. **Es mejor hacer un gran commit al final del proyecto que muchos pequeños.**
   - [ ] Verdadero
   - [x] Falso

---

## Sección 4: Ordena el Pipeline

**Ordena estos pasos del pipeline CI/CD en el orden correcto (1-5):**

___ Deploy (Desplegar a producción)  
___ Test (Ejecutar pruebas)  
___ Source (Escribir código)  
___ Build (Compilar)  
___ Notify (Notificar resultados)

1)Source
2)Build
3)Test
4)Notify
5)Deploy
---

## Sección 5: Escenario Práctico

**Escenario**: Eres parte de un equipo que desarrolla una app móvil. Actualmente:
- Cada desarrollador trabaja 2 semanas en su feature
- Se integra todo el código cada mes
- Las pruebas se hacen manualmente antes de cada release
- Los despliegues toman un día completo
- Hay muchos conflictos al integrar código

**Preguntas:**

1. **¿Qué problemas identificas en este proceso?**
   Mucho tiempo, 1 mes para hacer integraciones
   Realización de pruebas manuales
   Hay muchos bugs ya que se hacen integraciones a muy largo plazo.

2. **¿Cómo podría CI/CD ayudar en esta situación?**
   Se harían pruebas de manera aumatica
   Las integraciones serian casi que instantáneas
   Los despliegues se harían en casi horas y no dias

3. **¿Qué beneficios específicos esperarías al implementar CI/CD?**
   Entregas mucho mas rapidas
   Integraciones y actualizacionces casi que inmediatas
   Reducción de bugs por entregas constantes

---

## Sección 6: Diagrama de Flujo

**Dibuja o describe el flujo de un pipeline CI/CD para tu propio proyecto:**

**Mi proyecto es**: Realizar Verdemetria o NDVI

**Paso 1 (Source)**: Google Earth API

**Paso 2 (Build)**: Scripts 

**Paso 3 (Test)**: Bajar la data y hacer las pruebas con los datos obtenidos

**Paso 4 (Deploy)**: Ver el Cloropleth map y mostrar los resultados graficamente

**Notificaciones**: Cuando no se están generando los mapas ni se están obteniendo los csv files.

---

## Sección 7: Términos Clave

**Relaciona cada término con su definición correcta:**

**Términos:**
1. Build: Es el proceso de compilar codigo.
2. Artifact: son los resultados compilados listos para desplegar
3. Pipeline: Series de pasos secuenciales desde desarrollo hasta producción
4. Deployment: Despliegue o implementación.
5. Continuous Integration: Integración continua o cambios realizados durante la ejecución del proyecto.

**Definiciones:**
A. Serie automatizada de pasos desde código hasta producción
B. Resultado compilado listo para usar
C. Proceso de compilar el código 
D. Integrar código frecuentemente con validación automática
E. Llevar el código a un ambiente específico

**Tus respuestas:**
1 → Pipeline  
2 → Deployment_  
3 → Build  
4 → CI  
5 → CD

---

## Sección 8: Caso de Estudio

**Lee este escenario:**

La empresa "TechStart" solía desplegar su aplicación una vez al trimestre. Cada despliegue era un evento estresante de 2 días que requería que todo el equipo trabajara horas extra. Después de implementar CI/CD:
- Ahora despliegan 3-4 veces por semana
- Los despliegues toman 15 minutos
- Los bugs se detectan en minutos, no en semanas
- El equipo está menos estresado

**Preguntas:**

1. **¿Cuál fue el cambio más significativo?**
   _______________________________________________

2. **¿Por qué los bugs se detectan más rápido ahora?**
   _______________________________________________

3. **¿Qué rol juegan las pruebas automáticas en este éxito?**
   _______________________________________________

---

## Sección 9: Reflexión Personal

**¿En tu trabajo o proyectos personales:**

1. **¿Qué tareas repetitivas haces que podrían automatizarse?**
   _______________________________________________
   _______________________________________________

2. **¿Cuánto tiempo pasa entre que escribes código y lo despliegas?**
   _______________________________________________

3. **¿Qué te gustaría automatizar primero?**
   _______________________________________________
   _______________________________________________

---

## Sección 10: Mini-Proyecto Conceptual

**Diseña un pipeline CI/CD básico para uno de estos proyectos:**

- [ ] Blog personal
- [ ] API REST
- [ ] App móvil
- [ ] Sitio web de portafolio

**Mi proyecto elegido**: _______________________________________________

**Pipeline propuesto:**

**1. Trigger (¿Qué inicia el pipeline?)**
_______________________________________________

**2. Build (¿Qué se necesita construir/compilar?)**
_______________________________________________

**3. Test (¿Qué pruebas se ejecutarían?)**
_______________________________________________

**4. Deploy (¿A dónde se desplegaría?)**
_______________________________________________

**5. Rollback (¿Qué pasa si algo falla?)**
_______________________________________________

---

## Reflexión Final

**¿Qué concepto te pareció más útil?**
_______________________________________________

**¿Qué te gustaría aprender más en profundidad?**
_______________________________________________

**¿Cómo aplicarías CI/CD en tu próximo proyecto?**
_______________________________________________

¡Revisa tus respuestas en `retroalimentacion.md`! 🎉
