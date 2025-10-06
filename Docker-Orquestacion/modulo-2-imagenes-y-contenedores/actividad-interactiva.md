# Actividades Interactivas - Módulo 2: Imágenes y Contenedores

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cómo se construyen las imágenes Docker?**

A) Como un solo archivo  
B) Por capas inmutables  
C) Como código Python  
D) En la nube

### Pregunta 2
**¿Qué beneficio tiene la arquitectura de capas?**

A) Las imágenes son más grandes  
B) Reutilización y caché eficiente  
C) Más seguridad automática  
D) Ninguno

### Pregunta 3
**¿Qué tag debes usar en producción?**

A) latest  
B) Versión específica (ej: 1.24)  
C) test  
D) development

### Pregunta 4
**¿Qué hace docker run --rm?**

A) Reinicia el contenedor  
B) Elimina el contenedor al salir  
C) Elimina la imagen  
D) Reinicia el sistema

### Pregunta 5
**¿Cómo se comunican dos contenedores en la misma red?**

A) Por IP pública  
B) Por nombre del contenedor  
C) No pueden comunicarse  
D) Solo por localhost

---

## Sección 2: Ejercicios Prácticos

### Ejercicio 1: Comparar Tamaños
```bash
docker pull ubuntu:22.04
docker pull alpine:3.18
docker images
```

**¿Cuánto pesa Ubuntu?** _______________  
**¿Cuánto pesa Alpine?** _______________  
**¿Diferencia?** _______________

### Ejercicio 2: Networking
```bash
docker network create mi-red
docker run -d --name db --network mi-red postgres
docker run -d --name app --network mi-red nginx
```

**¿Funcionó?** [ ] Sí [ ] No  
**¿Los contenedores se ven?** _______________

### Ejercicio 3: Variables de Entorno
```bash
docker run -e MI_VAR=hola alpine env | grep MI_VAR
```

**Resultado:** _______________

---

## Reflexión Final

**¿Qué te pareció más útil?**
_______________________________________________

¡Revisa tus respuestas en `retroalimentacion.md`! 🎉
