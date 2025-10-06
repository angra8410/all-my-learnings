# Retroalimentación y Soluciones - Módulo 2: Imágenes y Contenedores

## Respuestas a Preguntas

### Pregunta 1: ¿Cómo se construyen las imágenes Docker?
**Respuesta correcta: B) Por capas inmutables**

**Explicación**: Las imágenes Docker se construyen por capas apiladas. Cada capa es inmutable y se reutiliza entre imágenes, lo que hace el sistema muy eficiente.

### Pregunta 2: ¿Qué beneficio tiene la arquitectura de capas?
**Respuesta correcta: B) Reutilización y caché eficiente**

**Explicación**: Las capas permiten compartir componentes comunes entre imágenes y acelerar builds mediante caché.

### Pregunta 3: ¿Qué tag debes usar en producción?
**Respuesta correcta: B) Versión específica (ej: 1.24)**

**Explicación**: Usar versiones específicas asegura comportamiento predecible. `latest` puede cambiar sin aviso.

### Pregunta 4: ¿Qué hace docker run --rm?
**Respuesta correcta: B) Elimina el contenedor al salir**

**Explicación**: La flag `--rm` elimina automáticamente el contenedor cuando termina su ejecución.

### Pregunta 5: ¿Cómo se comunican dos contenedores en la misma red?
**Respuesta correcta: B) Por nombre del contenedor**

**Explicación**: Docker proporciona resolución DNS automática, permitiendo que contenedores se comuniquen usando nombres.

---

## Evaluación de Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Dominas los conceptos de imágenes y contenedores. Continúa al Módulo 3.

### Si acertaste 70-89%: 💪 ¡Muy bien!
Buen entendimiento. Repasa conceptos de capas y networking.

### Si acertaste menos de 70%: 📚 Sigue adelante
Vuelve a practicar los ejercicios del README y los comandos básicos.

---

## Preparación para el Siguiente Módulo

Asegúrate de:

✅ Entender la arquitectura de capas  
✅ Saber crear redes personalizadas  
✅ Poder usar variables de entorno  
✅ Entender tags y versionado  

¡Excelente trabajo! Sigue así. 🚀
