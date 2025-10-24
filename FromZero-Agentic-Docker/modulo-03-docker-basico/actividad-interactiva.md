# Módulo 03: Actividad Interactiva - Docker Básico

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Comandos Docker Básicos (10 min)

Practica estos comandos 3 veces cada uno (Minuto fluido x3):

```bash
# Round 1
docker --version
docker images
docker ps
docker ps -a

# Round 2  
docker images
docker ps
docker ps -a

# Round 3
docker images
docker ps -a
```

**Resultados registrados**: [ ] Sí

---

### Ejercicio 2: Construir Primera Imagen (15 min)

```bash
cd modulo-03-docker-basico/ejemplos
docker build -t my-app:v1 .
docker images
```

**Imagen creada**: [ ] Sí
**Tamaño**: _____ MB

---

### Ejercicio 3: Ejecutar Contenedor (10 min)

```bash
docker run -d -p 8000:8000 --name test-container my-app:v1
docker ps
curl http://localhost:8000
curl http://localhost:8000/health
docker logs test-container
```

**Contenedor funcionando**: [ ] Sí

---

### Ejercicio 4: Gestión de Contenedores (15 min)

```bash
docker stop test-container
docker ps
docker ps -a
docker start test-container
docker restart test-container
docker logs -f test-container
docker rm -f test-container
```

**Ciclo completo practicado**: [ ] Sí

---

## 📊 Total: 50 minutos

**Todos los ejercicios completados**: [ ] Sí
