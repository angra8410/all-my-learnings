# Retroalimentación y Soluciones - Módulo 3: Dockerfile y Builds

## Respuestas a Preguntas

### Pregunta 1: ¿Qué instrucción define la imagen base?
**Respuesta correcta: B) FROM**

**Explicación**: FROM es siempre la primera instrucción y define la imagen base sobre la cual construir.

### Pregunta 2: ¿Qué hace WORKDIR?
**Respuesta correcta: B) Establece el directorio de trabajo**

**Explicación**: WORKDIR es equivalente a cd. Todos los comandos siguientes se ejecutan en ese directorio.

### Pregunta 3: ¿Cuál es mejor para copiar archivos?
**Respuesta correcta: B) COPY generalmente, ADD para casos especiales**

**Explicación**: COPY es más transparente. ADD solo para descomprimir o URLs.

### Pregunta 4: ¿Por qué usar multi-stage builds?
**Respuesta correcta: B) Para imágenes más pequeñas**

**Explicación**: Multi-stage permite separar build y runtime, resultando en imágenes finales mucho más pequeñas.

### Pregunta 5: ¿Dónde se lista archivos a ignorar?
**Respuesta correcta: B) .dockerignore**

**Explicación**: .dockerignore excluye archivos del contexto de build, similar a .gitignore.

---

## Evaluación de Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Dominas la creación de Dockerfiles. Listo para el Módulo 4.

### Si acertaste 70-89%: 💪 ¡Muy bien!
Buen entendimiento. Practica más con multi-stage builds.

### Si acertaste menos de 70%: 📚 Sigue adelante
Repasa las instrucciones principales y optimizaciones.

---

## Preparación para el Siguiente Módulo

Asegúrate de:

✅ Poder crear Dockerfiles básicos  
✅ Entender instrucciones principales (FROM, RUN, COPY, CMD)  
✅ Aplicar optimizaciones básicas  
✅ Usar .dockerignore  
✅ Conocer multi-stage builds  

¡Excelente trabajo! Sigue así. 🚀
