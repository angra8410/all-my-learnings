# Actividades Interactivas - Módulo 5b: DevOps y AWS para Data Engineering

## Introducción

Este documento contiene ejercicios prácticos para aplicar los conceptos de DevOps, IaC, containerización, y servicios de AWS. Los ejercicios están diseñados para ser realizados de manera incremental, construyendo sobre lo aprendido en cada sección.

---

## Sección 1: Preparación del Entorno

### Ejercicio 1.1: Verificar Herramientas

**Objetivo**: Asegurar que tienes todas las herramientas necesarias instaladas.

**Pasos**:

1. Verifica la instalación de Terraform:
```bash
terraform version
```
Resultado esperado: `Terraform v1.0+`

2. Verifica Docker:
```bash
docker --version
docker run hello-world
```

3. Verifica AWS CLI:
```bash
aws --version
aws sts get-caller-identity
```

4. Si no tienes las herramientas instaladas, instálalas según tu sistema operativo:
   - **Terraform**: https://www.terraform.io/downloads
   - **Docker**: https://docs.docker.com/get-docker/
   - **AWS CLI**: https://aws.amazon.com/cli/

**Checklist**:
- [ ] Terraform instalado y funcional
- [ ] Docker instalado y puede ejecutar contenedores
- [ ] AWS CLI configurado con credenciales válidas
- [ ] Git configurado

---

### Ejercicio 1.2: Configurar Credenciales AWS

**Objetivo**: Configurar acceso seguro a AWS.

**Pasos**:

1. Crea un usuario IAM en AWS Console con permisos de desarrollo (o usa credenciales existentes)

2. Configura AWS CLI:
```bash
aws configure
# AWS Access Key ID: [tu-access-key]
# AWS Secret Access Key: [tu-secret-key]
# Default region: us-east-1
# Default output format: json
```

3. Valida el acceso:
```bash
aws iam get-user
aws ec2 describe-regions
```

**Checklist**:
- [ ] Credenciales configuradas
- [ ] Conexión a AWS validada
- [ ] Región por defecto configurada

---

## Sección 2: Infrastructure as Code con Terraform

### Ejercicio 2.1: Explorar el Código Terraform

**Objetivo**: Familiarizarte con la estructura de los archivos Terraform del módulo.

**Pasos**:

1. Navega al directorio de ejemplos:
```bash
cd data-engineer-ai/05b-devops-aws/examples/terraform/
```

2. Lee los archivos en este orden:
   - `variables.tf` - Variables de configuración
   - `main.tf` - Recursos principales
   - `outputs.tf` - Valores de salida

3. Para cada archivo, identifica:
   - ¿Qué recursos se están creando?
   - ¿Qué variables son requeridas?
   - ¿Qué outputs se exponen?

**Preguntas de comprensión**:
1. ¿Cuántas subnets se crean en el VPC?
   - **Tu respuesta**: ___

2. ¿Qué tipo de launch type usa el servicio ECS?
   - **Tu respuesta**: ___

3. ¿Qué motor de base de datos usa RDS?
   - **Tu respuesta**: ___

4. ¿Cuántos security groups se definen?
   - **Tu respuesta**: ___

**Checklist**:
- [ ] He leído y entendido variables.tf
- [ ] He leído y entendido main.tf
- [ ] He leído y entendido outputs.tf
- [ ] He respondido las preguntas de comprensión

---

### Ejercicio 2.2: Validar Configuración Terraform

**Objetivo**: Ejecutar comandos básicos de Terraform sin crear recursos reales.

**Pasos**:

1. Inicializa Terraform:
```bash
terraform init
```
Esto descarga el provider de AWS y prepara el directorio.

2. Formatea el código (best practice):
```bash
terraform fmt
```

3. Valida la sintaxis:
```bash
terraform validate
```

4. Crea un archivo `terraform.tfvars` con valores de prueba:
```hcl
aws_region   = "us-east-1"
project_name = "devops-learning"
environment  = "dev"
db_username  = "dbadmin"
db_password  = "TempPassword123!"  # Cambiar en producción
ecr_image    = "public.ecr.aws/nginx/nginx:latest"  # Placeholder
```

5. Genera un plan de ejecución (NO apliques todavía):
```bash
terraform plan
```

6. Revisa el plan:
   - ¿Cuántos recursos se crearán?
   - ¿Hay algún error o advertencia?

**Resultados esperados**:
- `terraform init`: Success
- `terraform validate`: Configuration is valid
- `terraform plan`: Plan shows N resources to add

**Checklist**:
- [ ] Terraform inicializado correctamente
- [ ] Código validado sin errores
- [ ] Plan generado y revisado
- [ ] Entiendo qué recursos se crearían

---

### Ejercicio 2.3: Comprender Dependencias de Recursos

**Objetivo**: Identificar cómo Terraform gestiona dependencias entre recursos.

**Pasos**:

1. En `main.tf`, busca los recursos en este orden:
   - VPC
   - Subnets (dependen de VPC)
   - Security Groups (dependen de VPC)
   - RDS (depende de subnets y security group)
   - ECS (depende de VPC y security groups)

2. Crea un diagrama simple de dependencias:
```
VPC
 ├── Subnets
 ├── Security Groups
 │    ├── ECS Service
 │    └── RDS Instance
 └── Internet Gateway
```

**Preguntas**:
1. ¿Qué pasa si intentas crear un ECS Service antes que el VPC?
   - **Tu respuesta**: ___

2. ¿Por qué RDS necesita un subnet group?
   - **Tu respuesta**: ___

**Checklist**:
- [ ] He identificado las dependencias principales
- [ ] Entiendo el orden de creación de recursos
- [ ] He creado mi diagrama de dependencias

---

## Sección 3: Docker y Containerización

### Ejercicio 3.1: Construir Imagen Docker

**Objetivo**: Crear una imagen Docker compatible con ECS.

**Pasos**:

1. Navega al directorio de Docker:
```bash
cd ../docker/
```

2. Revisa el Dockerfile:
```bash
cat Dockerfile
```

3. Construye la imagen:
```bash
docker build -t devops-app:latest .
```

4. Lista las imágenes:
```bash
docker images | grep devops-app
```

5. Ejecuta el contenedor localmente:
```bash
docker run -p 8080:8080 devops-app:latest
```

6. En otra terminal, prueba el health endpoint:
```bash
curl http://localhost:8080/health
```

**Resultado esperado**:
```json
{"status": "healthy", "service": "devops-app"}
```

7. Detén el contenedor:
```bash
docker ps
docker stop <container_id>
```

**Checklist**:
- [ ] Imagen construida exitosamente
- [ ] Contenedor ejecutado localmente
- [ ] Health endpoint responde correctamente
- [ ] Contenedor detenido

---

### Ejercicio 3.2: Optimizar Imagen Docker (Avanzado)

**Objetivo**: Reducir el tamaño de la imagen y mejorar seguridad.

**Pasos**:

1. Verifica el tamaño actual:
```bash
docker images devops-app:latest
```

2. Modifica el Dockerfile para usar multi-stage build (opcional):
```dockerfile
# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1
CMD ["python", "app.py"]
```

3. Reconstruye:
```bash
docker build -t devops-app:optimized .
```

4. Compara tamaños:
```bash
docker images | grep devops-app
```

**Checklist**:
- [ ] He entendido multi-stage builds
- [ ] He comparado tamaños de imágenes
- [ ] He agregado health check

---

## Sección 4: Despliegue con ECS y Fargate (Conceptual)

### Ejercicio 4.1: Entender Arquitectura ECS

**Objetivo**: Comprender los componentes de ECS.

**Conceptos clave**:
- **Cluster**: Agrupación lógica de tareas y servicios
- **Task Definition**: Blueprint de tu aplicación (imagen, CPU, memoria)
- **Service**: Mantiene N tareas corriendo
- **Fargate**: Serverless compute engine (sin gestionar EC2s)

**Pasos**:

1. En `main.tf`, localiza:
   - `aws_ecs_cluster`
   - `aws_ecs_task_definition`
   - `aws_ecs_service`

2. Responde:

**¿Cuántas tareas (containers) corren por defecto?**
- **Tu respuesta**: ___

**¿Qué capacidad de CPU y memoria tiene cada tarea?**
- **Tu respuesta**: ___

**¿En qué subnets se despliegan los containers?**
- **Tu respuesta**: ___

**Checklist**:
- [ ] Entiendo qué es un ECS Cluster
- [ ] Entiendo la diferencia entre Task y Service
- [ ] Entiendo por qué usamos Fargate

---

### Ejercicio 4.2: Configuración de Networking

**Objetivo**: Comprender la configuración de red para ECS con Fargate.

**Preguntas**:

1. ¿Por qué los containers ECS necesitan subnets públicas con `assign_public_ip = true`?
   - **Tu respuesta**: ___

2. ¿Qué reglas de security group permiten tráfico al ECS service?
   - **Tu respuesta**: ___

3. ¿Cómo se comunica ECS con RDS de manera segura?
   - **Tu respuesta**: ___

**Checklist**:
- [ ] Entiendo la configuración de subnets
- [ ] Entiendo los security groups
- [ ] Entiendo la comunicación ECS-RDS

---

## Sección 5: Base de Datos con RDS

### Ejercicio 5.1: Configuración de RDS

**Objetivo**: Comprender la configuración de Amazon RDS para PostgreSQL.

**Pasos**:

1. En `main.tf`, localiza el recurso `aws_db_instance`

2. Identifica:
   - **Engine**: ¿Qué motor de base de datos?
   - **Instance class**: ¿Qué tamaño de instancia?
   - **Storage**: ¿Cuánto almacenamiento?
   - **Backup retention**: ¿Cuántos días de backup?

3. Responde:

**¿Por qué usamos `skip_final_snapshot = true`?**
- **Tu respuesta**: ___

**¿Qué pasa si cambias `publicly_accessible = true`?**
- **Tu respuesta**: ___

**¿Cómo se conecta la aplicación ECS a RDS?**
- **Tu respuesta**: ___

**Checklist**:
- [ ] Entiendo la configuración de RDS
- [ ] Entiendo subnet groups
- [ ] Entiendo consideraciones de seguridad

---

## Sección 6: CI/CD con GitHub Actions

### Ejercicio 6.1: Analizar Workflow de CI/CD

**Objetivo**: Entender el pipeline automatizado de despliegue.

**Pasos**:

1. Revisa el archivo:
```bash
cat ../.github/workflows/ci-cd-infra.yml
```

2. Identifica las etapas del pipeline:
   - **Terraform Check**: ¿Qué hace?
   - **Docker Build**: ¿Qué hace?
   - **Deploy**: ¿Qué hace?

3. ¿Qué secretos de GitHub se necesitan configurar?

Lista los secretos:
1. ___
2. ___
3. ___
4. ___

**Checklist**:
- [ ] Entiendo el flujo del workflow
- [ ] Identifico los secretos necesarios
- [ ] Entiendo cuándo se ejecuta el workflow

---

### Ejercicio 6.2: Configurar Secretos (Conceptual)

**Objetivo**: Comprender qué secretos configurar en GitHub Actions.

**Secretos necesarios**:

| Secret Name | Descripción | Ejemplo |
|-------------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | Credencial de AWS | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Secret de AWS | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION` | Región de AWS | `us-east-1` |
| `ECR_REPOSITORY` | Nombre del repo ECR | `my-app-repo` |
| `ECS_CLUSTER` | Nombre del cluster ECS | `devops-cluster` |
| `ECS_SERVICE` | Nombre del servicio ECS | `devops-service` |

**Pasos para configurar** (no ejecutar ahora):
1. Ve a tu repositorio en GitHub
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Agrega cada secret de la tabla

**Checklist**:
- [ ] Entiendo qué son los GitHub Secrets
- [ ] Sé dónde configurarlos
- [ ] Entiendo por qué nunca hardcodearlos en código

---

## Sección 7: Monitoreo y Observabilidad

### Ejercicio 7.1: CloudWatch Logs (Conceptual)

**Objetivo**: Comprender cómo se capturan logs en AWS.

**Conceptos**:
- ECS envía logs automáticamente a CloudWatch Logs
- Cada task definition especifica un log group
- Puedes filtrar y buscar logs en tiempo real

**Preguntas**:

1. ¿Dónde se almacenan los logs de los containers ECS?
   - **Tu respuesta**: ___

2. ¿Cuánto tiempo se retienen los logs por defecto?
   - **Tu respuesta**: ___

3. ¿Cómo buscarías errores en los logs?
   - **Tu respuesta**: ___

**Checklist**:
- [ ] Entiendo CloudWatch Logs
- [ ] Sé cómo acceder a logs de ECS
- [ ] Entiendo retention policies

---

## Sección 8: Integración Completa (Proyecto Guiado)

### Ejercicio 8.1: Despliegue Completo (Opcional - Genera Costos)

**⚠️ ADVERTENCIA**: Este ejercicio crea recursos reales en AWS que pueden generar costos. Solo realízalo si tienes una cuenta AWS y entiendes las implicaciones de costo.

**Objetivo**: Realizar un despliegue end-to-end de la infraestructura.

**Pasos**:

1. **Preparación**:
```bash
cd examples/terraform/
cp terraform.tfvars.example terraform.tfvars
# Edita terraform.tfvars con tus valores
```

2. **Crear ECR Repository** (una sola vez):
```bash
aws ecr create-repository --repository-name devops-app
```

3. **Build y Push imagen Docker a ECR**:
```bash
cd ../docker/
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker build -t devops-app:latest .
docker tag devops-app:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/devops-app:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/devops-app:latest
```

4. **Actualiza `ecr_image` en terraform.tfvars** con la imagen que acabas de subir

5. **Aplica Terraform**:
```bash
cd ../terraform/
terraform plan
terraform apply
```
Escribe `yes` cuando se te solicite.

6. **Espera a que se creen los recursos** (~5-10 minutos)

7. **Verifica el despliegue**:
```bash
# Obtén el ECS cluster
aws ecs list-clusters

# Verifica las tareas en ejecución
aws ecs list-tasks --cluster devops-cluster

# Obtén el endpoint de RDS
terraform output db_endpoint
```

8. **Limpieza** (MUY IMPORTANTE):
```bash
terraform destroy
```
Escribe `yes` para confirmar.

**Checklist despliegue**:
- [ ] ECR repository creado
- [ ] Imagen Docker subida a ECR
- [ ] Terraform plan revisado
- [ ] Recursos creados con terraform apply
- [ ] ECS tasks corriendo
- [ ] RDS instance disponible
- [ ] Recursos destruidos con terraform destroy

**Resultados esperados**:
- VPC creado con subnets
- ECS cluster con al menos 1 tarea corriendo
- RDS instance en estado "available"
- Outputs de Terraform mostrando IDs de recursos

---

## Sección 9: Troubleshooting Común

### Ejercicio 9.1: Resolver Problemas Típicos

**Problema 1: Terraform init falla**
```
Error: Failed to query available provider packages
```
**Solución**: Verifica tu conexión a internet y proxy settings.

**Problema 2: ECS task no inicia**
- Verifica que la imagen ECR existe y es accesible
- Revisa logs en CloudWatch Logs
- Verifica IAM roles tienen permisos correctos

**Problema 3: No puedo conectar a RDS**
- Verifica security groups permiten tráfico desde ECS
- Verifica que RDS está en subnet privada correcta
- Prueba conectividad desde ECS task

**Problema 4: Terraform apply falla con conflicto de nombres**
- Cambia `project_name` en variables
- Verifica que no hay recursos con el mismo nombre en AWS

**Checklist**:
- [ ] He leído los problemas comunes
- [ ] Sé dónde buscar logs para debugging
- [ ] Entiendo conceptos básicos de troubleshooting

---

## Sección 10: Evaluación Final

### Preguntas de Comprensión

1. **¿Qué es Infrastructure as Code y cuáles son sus beneficios?**
   - Tu respuesta: ___

2. **¿Cuál es la diferencia entre ECS EC2 launch type y Fargate?**
   - Tu respuesta: ___

3. **¿Por qué es importante usar AWS Secrets Manager en lugar de hardcodear credenciales?**
   - Tu respuesta: ___

4. **¿Qué ventajas tiene automatizar el despliegue con CI/CD?**
   - Tu respuesta: ___

5. **¿Cuándo elegirías RDS sobre una base de datos self-hosted en EC2?**
   - Tu respuesta: ___

### Checklist Global del Módulo

- [ ] He completado todos los ejercicios de preparación
- [ ] Entiendo los conceptos de Terraform
- [ ] He construido y ejecutado una imagen Docker
- [ ] Comprendo la arquitectura ECS + Fargate
- [ ] Entiendo la configuración de RDS
- [ ] He analizado el workflow de CI/CD
- [ ] Sé cómo monitorear con CloudWatch
- [ ] (Opcional) He realizado un despliegue completo
- [ ] He documentado mi aprendizaje en progreso.md

### Reflexión

**¿Qué fue lo más desafiante del módulo?**
- Tu respuesta: ___

**¿Qué concepto te resultó más útil?**
- Tu respuesta: ___

**¿Qué aplicarías en un proyecto real?**
- Tu respuesta: ___

---

## Próximos Pasos

Una vez completada esta actividad:

1. ✅ Revisa tus respuestas contra `retroalimentacion.md`
2. ✅ Documenta tu progreso en `progreso.md`
3. ✅ Experimenta modificando el código Terraform
4. ✅ Investiga servicios adicionales de AWS (EKS, Lambda, Step Functions)

**¡Excelente trabajo completando el módulo de DevOps y AWS!** 🎉

Ahora estás preparado para llevar aplicaciones de datos e IA a producción con prácticas modernas de DevOps.
