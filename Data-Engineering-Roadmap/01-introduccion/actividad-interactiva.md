# 🎯 Actividad Interactiva — Módulo 01: Introducción a Data Engineering

## Objetivo General
Configurar un entorno de desarrollo profesional para Data Engineering y familiarizarte con las herramientas fundamentales: Git, Docker y PostgreSQL.

---

## 📋 Ejercicio 1: Instalación y Verificación de Herramientas (Duración: 20 minutos)

### Objetivo
Instalar y verificar que todas las herramientas necesarias están correctamente configuradas.

### Pasos

1. **Verificar instalación de Git**
```bash
git --version
```

**Tu salida:**
```
_______________________________________________
```

2. **Verificar instalación de Docker**
```bash
docker --version
docker ps
```

**Tu salida:**
```
_______________________________________________
_______________________________________________
```

3. **Verificar instalación de Python**
```bash
python --version
# o en algunos sistemas:
python3 --version
```

**Tu salida:**
```
_______________________________________________
```

### Verificación
- ✅ Git versión 2.x o superior
- ✅ Docker versión 20.x o superior
- ✅ Python versión 3.9 o superior
- ✅ `docker ps` ejecuta sin errores (puede mostrar tabla vacía)

**Duración:** 20 minutos

---

## 📋 Ejercicio 2: Configuración de Git Global (Duración: 10 minutos)

### Objetivo
Configurar tu identidad en Git para que tus commits estén correctamente identificados.

### Pasos

1. **Configurar nombre de usuario**
```bash
git config --global user.name "Tu Nombre Completo"
```

2. **Configurar email**
```bash
git config --global user.email "tu-email@ejemplo.com"
```

3. **Configurar editor por defecto (opcional)**
```bash
# VSCode como editor
git config --global core.editor "code --wait"

# Vim (por defecto en muchos sistemas)
# git config --global core.editor "vim"
```

4. **Verificar configuración**
```bash
git config --list | grep user
```

**Tu configuración:**
```
user.name=_______________________________________________
user.email=_______________________________________________
```

### Verificación
- ✅ `user.name` y `user.email` configurados
- ✅ Los valores coinciden con tu identidad real

**Duración:** 10 minutos

---

## 📋 Ejercicio 3: Clonar Repositorio y Crear Rama Personal (Duración: 15 minutos)

### Objetivo
Clonar el repositorio del curso y crear una rama de trabajo personal siguiendo las mejores prácticas de Git.

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Roadmap
```

2. **Verificar que estás en la rama correcta**
```bash
git branch
git status
```

**Rama actual:**
```
_______________________________________________
```

3. **Crear y cambiar a una rama personal**
```bash
git checkout -b feature/mi-progreso-data-eng
```

4. **Verificar la nueva rama**
```bash
git branch
```

**Todas tus ramas locales:**
```
_______________________________________________
_______________________________________________
```

5. **Ver estructura del directorio**
```bash
ls -la
```

**Contenido de Data-Engineering-Roadmap:**
```
_______________________________________________
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Repositorio clonado exitosamente
- ✅ Estás en la rama `feature/mi-progreso-data-eng`
- ✅ Puedes ver las carpetas de los módulos 01-12

**Duración:** 15 minutos

---

## 📋 Ejercicio 4: Ejecutar PostgreSQL en Docker (Duración: 25 minutos)

### Objetivo
Levantar un contenedor Docker con PostgreSQL y verificar que funciona correctamente.

### Pasos

1. **Descargar la imagen de PostgreSQL**
```bash
docker pull postgres:13
```

**Progreso de descarga:**
```
_______________________________________________
_______________________________________________
```

2. **Ejecutar contenedor con PostgreSQL**
```bash
docker run --name postgres-local \
  -e POSTGRES_PASSWORD=dataeng2024 \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_DB=learning_db \
  -p 5432:5432 \
  -d postgres:13
```

**ID del contenedor creado:**
```
_______________________________________________
```

3. **Verificar que el contenedor está corriendo**
```bash
docker ps
```

**Estado del contenedor:**
```
CONTAINER ID   IMAGE         STATUS        PORTS                    NAMES
_______________   postgres:13   Up X seconds  0.0.0.0:5432->5432/tcp  postgres-local
```

4. **Ver logs del contenedor**
```bash
docker logs postgres-local
```

**Últimas líneas de los logs (busca "ready to accept connections"):**
```
_______________________________________________
_______________________________________________
_______________________________________________
```

5. **Verificar conectividad con PostgreSQL**
```bash
docker exec -it postgres-local psql -U dataeng -d learning_db -c "SELECT version();"
```

**Versión de PostgreSQL:**
```
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Contenedor `postgres-local` en estado "Up"
- ✅ Puerto 5432 mapeado correctamente
- ✅ Consulta SQL ejecutada exitosamente
- ✅ Logs muestran "database system is ready to accept connections"

**Duración:** 25 minutos

---

## 📋 Ejercicio 5: Conectarse a PostgreSQL y Crear Primera Tabla (Duración: 20 minutos)

### Objetivo
Conectarse interactivamente a PostgreSQL y ejecutar comandos SQL básicos.

### Pasos

1. **Conectarse a PostgreSQL con psql**
```bash
docker exec -it postgres-local psql -U dataeng -d learning_db
```

2. **Listar bases de datos disponibles**
```sql
\l
```

**Bases de datos existentes:**
```
_______________________________________________
_______________________________________________
```

3. **Crear una tabla de prueba**
```sql
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    modulo_actual INT,
    fecha_inicio DATE DEFAULT CURRENT_DATE
);
```

4. **Insertar datos de prueba**
```sql
INSERT INTO estudiantes (nombre, modulo_actual) 
VALUES ('Tu Nombre', 1);
```

5. **Consultar los datos**
```sql
SELECT * FROM estudiantes;
```

**Resultado de la consulta:**
```
 id | nombre  | modulo_actual | fecha_inicio 
----|---------|---------------|-------------
_______________________________________________
```

6. **Describir la estructura de la tabla**
```sql
\d estudiantes
```

**Estructura de la tabla:**
```
_______________________________________________
_______________________________________________
_______________________________________________
```

7. **Salir de psql**
```sql
\q
```

### Verificación
- ✅ Conexión exitosa a PostgreSQL
- ✅ Tabla `estudiantes` creada
- ✅ Registro insertado correctamente
- ✅ Consulta devuelve tu nombre y módulo 1

**Duración:** 20 minutos

---

## 📋 Ejercicio 6: Gestión de Contenedores Docker (Duración: 15 minutos)

### Objetivo
Aprender a administrar contenedores Docker: detener, iniciar, eliminar.

### Pasos

1. **Ver contenedores en ejecución**
```bash
docker ps
```

2. **Ver TODOS los contenedores (incluso detenidos)**
```bash
docker ps -a
```

**Número total de contenedores:**
```
_______________________________________________
```

3. **Detener el contenedor PostgreSQL**
```bash
docker stop postgres-local
```

4. **Verificar que está detenido**
```bash
docker ps
docker ps -a
```

**Estado actual de postgres-local:**
```
_______________________________________________
```

5. **Reiniciar el contenedor**
```bash
docker start postgres-local
```

6. **Verificar que los datos persisten**
```bash
docker exec -it postgres-local psql -U dataeng -d learning_db -c "SELECT * FROM estudiantes;"
```

**¿Tus datos siguen ahí? (Sí/No):**
```
_______________________________________________
```

7. **Ver información detallada del contenedor**
```bash
docker inspect postgres-local | grep -i ipaddress
```

**IP del contenedor:**
```
_______________________________________________
```

### Verificación
- ✅ Puedes detener y reiniciar contenedores
- ✅ Los datos persisten después de reiniciar
- ✅ Comprendes la diferencia entre `docker ps` y `docker ps -a`

**Duración:** 15 minutos

---

## 📋 Ejercicio 7: Crear Tu Plan Personal de Estudio (Duración: 15 minutos)

### Objetivo
Personalizar el archivo `progreso.md` con tu plan de estudio realista.

### Pasos

1. **Calcular tu disponibilidad semanal**

**Horas disponibles por semana:** _____ horas

**Distribución:**
- Lunes: _____ horas
- Martes: _____ horas
- Miércoles: _____ horas
- Jueves: _____ horas
- Viernes: _____ horas
- Sábado: _____ horas
- Domingo: _____ horas

2. **Determinar tu ritmo**

Si tienes:
- **15-20 horas/semana**: Ritmo intensivo → 1.5 módulos/semana → 8 semanas
- **10-15 horas/semana**: Ritmo moderado → 1 módulo/semana → 12 semanas
- **5-10 horas/semana**: Ritmo relajado → 1 módulo cada 2 semanas → 24 semanas

**Tu ritmo elegido:** _______________________

3. **Fecha objetivo de finalización**

Fecha de inicio: ___________________  
Fecha objetivo de fin: ___________________

4. **Editar progreso.md con tu plan**
```bash
cd 01-introduccion
nano progreso.md  # o usa VSCode: code progreso.md
```

5. **Hacer commit de tu progreso**
```bash
git add progreso.md
git commit -m "feat: personalizar plan de estudio - Módulo 01"
```

### Verificación
- ✅ Plan realista basado en tu disponibilidad real
- ✅ Fechas objetivo definidas
- ✅ Commit realizado en tu rama personal

**Duración:** 15 minutos

---

## 📋 Ejercicio 8: Exploración de Docker Compose (Opcional - Duración: 20 minutos)

### Objetivo
Introducción a Docker Compose para gestionar múltiples contenedores (útil para módulos futuros).

### Pasos

1. **Crear archivo docker-compose.yml**
```bash
cd /tmp
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:13
    container_name: postgres-compose
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: dataeng2024
      POSTGRES_DB: learning_db
    ports:
      - "5433:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
EOF
```

2. **Levantar servicios con docker-compose**
```bash
docker-compose up -d
```

**Servicios levantados:**
```
_______________________________________________
```

3. **Verificar servicios**
```bash
docker-compose ps
```

4. **Ver logs**
```bash
docker-compose logs postgres
```

5. **Detener servicios**
```bash
docker-compose down
```

6. **Eliminar incluyendo volúmenes (datos)**
```bash
docker-compose down -v
```

### Verificación
- ✅ Entiendes la diferencia entre `docker run` y `docker-compose`
- ✅ Puedes levantar/detener servicios con compose
- ✅ Comprendes el concepto de volúmenes para persistencia

**Duración:** 20 minutos

---

## 📊 Resumen de Tiempo Total

| Ejercicio | Duración |
|-----------|----------|
| 1. Instalación y verificación | 20 min |
| 2. Configuración de Git | 10 min |
| 3. Clonar repo y crear rama | 15 min |
| 4. PostgreSQL en Docker | 25 min |
| 5. Conectar y crear tabla | 20 min |
| 6. Gestión de contenedores | 15 min |
| 7. Plan personal de estudio | 15 min |
| 8. Docker Compose (opcional) | 20 min |
| **TOTAL** | **120-140 min (2-2.5 horas)** |

---

## ✅ Checklist Final

Antes de pasar al Módulo 02, verifica que completaste:

- [ ] Todas las herramientas instaladas y verificadas
- [ ] Git configurado con tu nombre y email
- [ ] Repositorio clonado y rama personal creada
- [ ] PostgreSQL corriendo en Docker
- [ ] Tabla de prueba creada y datos insertados
- [ ] Comprendes comandos básicos de Docker (start, stop, ps)
- [ ] Plan personal documentado en `progreso.md`
- [ ] Al menos un commit realizado en tu rama

---

## 🎯 Próximos Pasos

1. **Actualiza tu `progreso.md`** marcando las tareas completadas
2. **Revisa `retroalimentacion.md`** para autoevaluarte
3. **Consulta `recursos.md`** para profundizar en temas específicos
4. **Prepárate para el Módulo 02**: SQL para Data Engineering

---

**🎉 ¡Felicitaciones!** Has completado la configuración de tu entorno de Data Engineering. Ahora tienes las bases para construir pipelines de datos profesionales.

**💡 Tip**: Mantén tu contenedor PostgreSQL corriendo, lo usaremos intensivamente en el Módulo 02.