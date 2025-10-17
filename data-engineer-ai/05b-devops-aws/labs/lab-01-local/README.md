# Lab 01: Entorno DevOps Local (Sin Coste AWS)

## 🎯 Objetivos del Laboratorio

Este laboratorio te permite practicar conceptos de DevOps y AWS **sin incurrir en costos de AWS**, utilizando herramientas locales que simulan servicios en la nube:

- Ejecutar una aplicación Flask containerizada (simula ECS Fargate)
- Gestionar una base de datos PostgreSQL (simula Amazon RDS)
- Usar LocalStack para simular servicios AWS (S3, Secrets Manager, CloudWatch, etc.)
- Usar MinIO como alternativa visual a S3
- Practicar orquestación con Docker Compose
- Automatizar tareas con Make
- Validar infraestructura con scripts de health check

## 🏗️ Arquitectura del Lab

```
┌─────────────────────────────────────────────────────────┐
│                     Tu Máquina Local                     │
│                                                          │
│  ┌────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │   Flask    │  │  PostgreSQL  │  │   LocalStack    │  │
│  │    App     │─▶│   (RDS)      │  │  (AWS Services) │  │
│  │  :8080     │  │    :5432     │  │     :4566       │  │
│  └────────────┘  └─────────────┘  └─────────────────┘  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │              MinIO (S3 alternativo)             │    │
│  │      API :9000      Console :9001               │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## 📋 Prerrequisitos

### Opción 1: Usar DevContainer (Recomendado)

Si usas VS Code con Remote - Containers, todas las herramientas ya están instaladas. Solo necesitas:

- Visual Studio Code
- Docker Desktop
- Extensión Remote - Containers

Ver `.devcontainer/README-codespaces.md` para más detalles.

### Opción 2: Instalación Local

Si prefieres trabajar sin DevContainer, necesitas:

- **Docker** >= 20.10 y **Docker Compose** >= 2.0
- **Make** (instalado en Linux/Mac por defecto)
- **curl** y **jq** para pruebas
- **psql** (cliente PostgreSQL) - opcional pero recomendado

Verificar instalación:
```bash
docker --version
docker compose version
make --version
```

## 🚀 Inicio Rápido

### 1. Navegar al Directorio del Lab

```bash
cd data-engineer-ai/05b-devops-aws/labs/lab-01-local
```

### 2. Ver Comandos Disponibles

```bash
make help
```

Deberías ver una lista de todos los comandos disponibles con descripciones.

### 3. Iniciar el Laboratorio

```bash
# Verificar dependencias (opcional)
make install

# Levantar todos los servicios
make up
```

Este comando:
- Construye la imagen de la aplicación Flask
- Inicia PostgreSQL, LocalStack, MinIO y la aplicación
- Ejecuta el script de inicialización de base de datos
- Espera a que todos los servicios estén listos

### 4. Verificar que Todo Funciona

```bash
make check
```

Este comando ejecuta el script `tests/check_health.sh` que verifica:
- Endpoint `/health` de la aplicación Flask
- Conexión y tablas de PostgreSQL
- Disponibilidad de LocalStack
- Disponibilidad de MinIO

### 5. Explorar los Servicios

#### Aplicación Flask

```bash
# Endpoint principal
curl http://localhost:8080/

# Health check
curl http://localhost:8080/health

# Información de la aplicación
curl http://localhost:8080/info

# Con formato JSON bonito
curl http://localhost:8080/info | jq .
```

#### PostgreSQL

```bash
# Abrir shell de PostgreSQL
make shell-postgres

# Dentro de psql, ejecuta:
\dt                           # Listar tablas
SELECT * FROM users;          # Ver usuarios
SELECT * FROM app_events;     # Ver eventos
\q                            # Salir
```

O directamente desde la terminal:
```bash
make test-db
```

#### LocalStack (AWS local)

```bash
# Verificar servicios disponibles
curl http://localhost:4566/_localstack/health | jq .

# Ejemplo: Listar buckets S3 (vacío inicialmente)
aws --endpoint-url=http://localhost:4566 s3 ls

# Crear un bucket S3 local
aws --endpoint-url=http://localhost:4566 s3 mb s3://mi-bucket-local

# Listar buckets
aws --endpoint-url=http://localhost:4566 s3 ls

# Subir un archivo
echo "Hola desde LocalStack" > test.txt
aws --endpoint-url=http://localhost:4566 s3 cp test.txt s3://mi-bucket-local/

# Listar objetos del bucket
aws --endpoint-url=http://localhost:4566 s3 ls s3://mi-bucket-local/
```

#### MinIO (S3 visual)

Abre tu navegador en: http://localhost:9001

Credenciales:
- **Usuario**: `minioadmin`
- **Contraseña**: `minioadmin123`

Desde la consola web puedes:
- Crear buckets
- Subir/descargar archivos
- Gestionar políticas de acceso
- Ver métricas y logs

### 6. Ver Logs

```bash
# Logs de todos los servicios
make logs

# Logs solo de la aplicación
make logs-app

# Logs solo de PostgreSQL
make logs-postgres

# Logs de LocalStack
make logs-localstack
```

Para salir de los logs, presiona `Ctrl+C`.

### 7. Detener el Laboratorio

```bash
# Detener servicios (preserva los datos)
make down

# Detener y eliminar volúmenes (borra todos los datos)
make clean
```

## 🧪 Ejercicios Prácticos

### Ejercicio 1: Explorar la Base de Datos

1. Conecta a PostgreSQL:
   ```bash
   make shell-postgres
   ```

2. Explora las tablas y datos:
   ```sql
   -- Ver estructura de la tabla users
   \d users

   -- Contar usuarios
   SELECT COUNT(*) FROM users;

   -- Ver todos los usuarios
   SELECT * FROM users;

   -- Ver eventos recientes
   SELECT event_type, event_data, created_at 
   FROM app_events 
   ORDER BY created_at DESC 
   LIMIT 5;
   ```

3. Inserta nuevos datos:
   ```sql
   INSERT INTO users (username, email) 
   VALUES ('newuser', 'newuser@example.com');

   INSERT INTO app_events (event_type, event_data) 
   VALUES ('user_login', '{"username": "newuser", "ip": "127.0.0.1"}'::jsonb);
   ```

4. Sal de psql: `\q`

### Ejercicio 2: Interactuar con la API Flask

1. Obtener información general:
   ```bash
   curl http://localhost:8080/info | jq .
   ```

2. Enviar datos al endpoint:
   ```bash
   curl -X POST http://localhost:8080/api/data \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Test", "valor": 123}' | jq .
   ```

3. Verificar health check:
   ```bash
   watch -n 2 'curl -s http://localhost:8080/health | jq .'
   ```
   (Presiona `Ctrl+C` para salir)

### Ejercicio 3: Simular AWS con LocalStack

1. Crear recursos en S3:
   ```bash
   # Crear bucket
   aws --endpoint-url=http://localhost:4566 s3 mb s3://data-lab

   # Subir un archivo JSON
   echo '{"curso": "DevOps", "modulo": "05b"}' > datos.json
   aws --endpoint-url=http://localhost:4566 s3 cp datos.json s3://data-lab/

   # Leer el archivo
   aws --endpoint-url=http://localhost:4566 s3 cp s3://data-lab/datos.json -
   ```

2. Crear un secreto:
   ```bash
   aws --endpoint-url=http://localhost:4566 secretsmanager create-secret \
     --name mi-secreto \
     --secret-string '{"usuario":"admin","password":"secret123"}'

   # Leer el secreto
   aws --endpoint-url=http://localhost:4566 secretsmanager get-secret-value \
     --secret-id mi-secreto | jq -r '.SecretString'
   ```

3. Listar recursos IAM:
   ```bash
   aws --endpoint-url=http://localhost:4566 iam list-users
   ```

### Ejercicio 4: Trabajar con MinIO

1. Abre la consola: http://localhost:9001
2. Login con `minioadmin` / `minioadmin123`
3. Crea un bucket llamado `imagenes`
4. Sube algunos archivos (imágenes, documentos, etc.)
5. Configura el bucket como público
6. Intenta acceder a los archivos desde el navegador

### Ejercicio 5: Modificar y Reconstruir la Aplicación

1. Edita el archivo `../../examples/docker/app.py`
2. Añade un nuevo endpoint:
   ```python
   @app.route('/custom')
   def custom():
       return jsonify({
           'message': '¡Endpoint personalizado!',
           'timestamp': datetime.utcnow().isoformat()
       })
   ```

3. Reconstruye y reinicia:
   ```bash
   make rebuild
   ```

4. Prueba tu nuevo endpoint:
   ```bash
   curl http://localhost:8080/custom | jq .
   ```

## 📊 Comandos Útiles del Makefile

| Comando | Descripción |
|---------|-------------|
| `make help` | Muestra todos los comandos disponibles |
| `make up` | Inicia todos los servicios |
| `make down` | Detiene todos los servicios |
| `make restart` | Reinicia todos los servicios |
| `make logs` | Muestra logs en tiempo real |
| `make check` | Verifica salud de todos los servicios |
| `make test-all` | Ejecuta todas las pruebas |
| `make clean` | Detiene servicios y elimina volúmenes |
| `make status` | Muestra estado de los servicios |
| `make info` | Muestra información del laboratorio |

## 🔍 Solución de Problemas

### Los servicios no inician

```bash
# Ver logs para identificar el problema
make logs

# Verificar que los puertos no están en uso
netstat -an | grep 8080
netstat -an | grep 5432

# Reconstruir desde cero
make clean
make build
make up
```

### Error de conexión a PostgreSQL

```bash
# Verificar que el contenedor está corriendo
docker ps | grep postgres

# Ver logs de PostgreSQL
make logs-postgres

# Reiniciar solo PostgreSQL
docker compose restart lab_postgres
```

### La aplicación no responde

```bash
# Verificar logs de la app
make logs-app

# Verificar que la imagen se construyó correctamente
docker images | grep devops

# Reconstruir la aplicación
docker compose build app
docker compose up -d app
```

### LocalStack no funciona

```bash
# Ver logs de LocalStack
make logs-localstack

# Verificar health
curl http://localhost:4566/_localstack/health

# Reiniciar LocalStack
docker compose restart localstack
```

### Los datos de LocalStack se pierden al reiniciar

Por defecto, LocalStack no persiste datos entre reinicios. Esto es intencional para mantener el lab simple. Si necesitas persistencia:

1. Edita `docker-compose.yml`
2. Cambia `PERSISTENCE=0` a `PERSISTENCE=1`
3. Añade un volumen en la sección de LocalStack:
   ```yaml
   volumes:
     - localstack_data:/var/lib/localstack
     - /var/run/docker.sock:/var/run/docker.sock
   ```
4. Añade el volumen en la sección `volumes` al final del archivo:
   ```yaml
   localstack_data:
     name: lab_localstack_data
   ```
5. Reconstruye: `make rebuild`

## 📚 Recursos de Referencia

### Documentación de Servicios

- **Docker Compose**: https://docs.docker.com/compose/
- **PostgreSQL**: https://www.postgresql.org/docs/
- **LocalStack**: https://docs.localstack.cloud/
- **MinIO**: https://min.io/docs/
- **Flask**: https://flask.palletsprojects.com/

### Comandos Docker Compose

```bash
# Ver servicios corriendo
docker compose ps

# Ver logs de un servicio específico
docker compose logs -f <servicio>

# Ejecutar comando en un contenedor
docker compose exec <servicio> <comando>

# Ver recursos utilizados
docker compose stats

# Pausar servicios
docker compose pause

# Reanudar servicios
docker compose unpause
```

### Comandos PostgreSQL

```bash
# Conectar desde línea de comandos
psql -h localhost -U devuser -d appdb

# Dentro de psql:
\l              # Listar bases de datos
\dt             # Listar tablas
\d <tabla>      # Describir tabla
\du             # Listar usuarios
\q              # Salir
```

## 🎓 Conceptos Aprendidos

Al completar este laboratorio, habrás practicado:

✅ **Containerización**: Ejecutar aplicaciones en contenedores Docker
✅ **Orquestación**: Gestionar múltiples servicios con Docker Compose
✅ **Bases de Datos**: Conectar y gestionar PostgreSQL
✅ **Servicios AWS (local)**: Simular S3, Secrets Manager, CloudWatch
✅ **APIs REST**: Interactuar con endpoints HTTP
✅ **Health Checks**: Validar disponibilidad de servicios
✅ **Automatización**: Usar Makefiles para tareas comunes
✅ **Debugging**: Leer logs y diagnosticar problemas

## 🚀 Siguientes Pasos

1. **Modifica la aplicación**: Añade nuevos endpoints o funcionalidades
2. **Integra Terraform**: Usa LocalStack con código Terraform (ver `../../examples/terraform/`)
3. **Configura CI/CD local**: Simula pipelines de deployment
4. **Implementa monitoreo**: Añade logs estructurados y métricas
5. **Prueba con datos reales**: Carga datasets en PostgreSQL y procésalos

## ⚠️ Limitaciones y Diferencias con AWS Real

| Aspecto | Lab Local | AWS Real |
|---------|-----------|----------|
| **Costo** | Gratis | Pay-as-you-go |
| **Escalado** | Manual, limitado por recursos locales | Auto-scaling, casi ilimitado |
| **Alta disponibilidad** | Single point of failure | Multi-AZ, redundancia |
| **Seguridad** | Simulada | IAM, VPC, Security Groups reales |
| **Servicios** | Subset de servicios AWS | Todos los servicios AWS |
| **Performance** | Depende de tu máquina | SLAs empresariales |
| **Networking** | Todo en localhost | VPC, subnets, internet gateway |

**Este lab es perfecto para aprender y experimentar, pero no reemplaza la experiencia con AWS real en producción.**

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias de mejora, abre un issue o PR en el repositorio.

---

**¡Disfruta experimentando con DevOps sin preocuparte por costos!** 🚀💸

Para más información, consulta el README principal del módulo: `../../README.md`
