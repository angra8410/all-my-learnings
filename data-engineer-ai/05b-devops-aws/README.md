# Módulo 5b: DevOps y AWS para Data Engineering

## Introducción

Bienvenido al módulo de DevOps y AWS para Data Engineering. En este módulo aprenderás las prácticas y herramientas esenciales para llevar tus pipelines de datos y aplicaciones de IA a producción de manera confiable, automatizada y escalable en AWS.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Comprender los principios fundamentales de DevOps aplicados a Data Engineering
- 🎯 Implementar Infrastructure as Code (IaC) con Terraform
- 🎯 Desplegar aplicaciones containerizadas con Docker, ECS y Fargate
- 🎯 Configurar bases de datos gestionadas con Amazon RDS
- 🎯 Automatizar despliegues con CI/CD usando GitHub Actions y AWS CodePipeline
- 🎯 Gestionar redes, seguridad y accesos con VPC, Security Groups e IAM
- 🎯 Implementar monitoreo y observabilidad con CloudWatch
- 🎯 Aplicar prácticas de gestión de secretos con AWS Secrets Manager
- 🎯 Entender el paso de herramientas open source a soluciones enterprise

## ¿Por qué es importante?

En producción, no basta con que tu código funcione localmente. Necesitas:
- **Infraestructura reproducible**: Crear y destruir entornos de manera consistente
- **Despliegues automatizados**: Reducir errores humanos y acelerar el time-to-market
- **Escalabilidad**: Manejar cargas variables sin intervención manual
- **Observabilidad**: Detectar y resolver problemas rápidamente
- **Seguridad**: Proteger datos sensibles y cumplir regulaciones

**Dato importante**: Las empresas que adoptan DevOps despliegan 46 veces más frecuentemente y tienen una tasa de falla 5 veces menor.

## Guía Rápida

### Prerrequisitos
- Cuenta de AWS (free tier es suficiente para los ejemplos)
- Docker instalado localmente
- Terraform instalado (v1.0+)
- AWS CLI configurado
- Git y GitHub account

### Estructura del Módulo
```
05b-devops-aws/
├── README.md                          # Este archivo
├── actividad-interactiva.md           # Ejercicios prácticos
├── progreso.md                        # Tu registro de avance
├── retroalimentacion.md               # Soluciones y explicaciones
└── examples/
    ├── terraform/                     # Ejemplos de IaC
    │   ├── main.tf                    # Recursos principales (VPC, ECS, RDS)
    │   ├── variables.tf               # Variables configurables
    │   └── outputs.tf                 # Outputs útiles
    ├── docker/                        # Dockerfile ejemplo
    │   └── Dockerfile                 # Imagen Python para ECS
    └── .github/workflows/             # CI/CD
        └── ci-cd-infra.yml            # Pipeline de ejemplo
```

## Temas Cubiertos

### 1. Infrastructure as Code (IaC)

#### Terraform
- Declaración de recursos de AWS (provider, VPC, subnets, security groups)
- Gestión de estado y workspaces
- Módulos reutilizables
- Best practices para equipos

**Comparación con alternativas:**
- **AWS CDK**: Más programático, integrado con AWS
- **CloudFormation**: Nativo de AWS, más verboso
- **Pulumi**: Multi-cloud, lenguajes de programación completos

**Archivo de ejemplo**: `examples/terraform/main.tf`

#### Ansible (Conceptos)
- Automatización de configuración
- Playbooks para setup de servidores
- Cuándo usar Ansible vs Terraform

### 2. Containerización y Orquestación

#### Docker
- Creación de imágenes optimizadas para producción
- Multi-stage builds para reducir tamaño
- Health checks y señales de graceful shutdown
- **Archivo de ejemplo**: `examples/docker/Dockerfile`

#### Amazon ECS + Fargate
- Task definitions y servicios
- Fargate vs EC2 launch type
- Network configuration y service discovery
- Auto-scaling basado en métricas
- **Código**: Ver `main.tf` - recursos `aws_ecs_cluster`, `aws_ecs_task_definition`, `aws_ecs_service`

### 3. Bases de Datos Gestionadas

#### Amazon RDS (PostgreSQL)
- Configuración de subnet groups
- Security groups y acceso controlado
- Backups automáticos y recuperación
- Monitoring de performance
- **Código**: Ver `main.tf` - recursos `aws_db_subnet_group`, `aws_db_instance`

### 4. CI/CD: Integración y Despliegue Continuo

#### GitHub Actions
- Workflows automatizados
- Terraform plan/apply en PRs
- Build y push de imágenes Docker a ECR
- Deploy a ECS service
- **Archivo de ejemplo**: `examples/.github/workflows/ci-cd-infra.yml`

#### AWS CodePipeline (Conceptos)
- Pipelines nativos de AWS
- Integración con CodeBuild y CodeDeploy
- Blue/green deployments

### 5. Networking y Seguridad

#### VPC (Virtual Private Cloud)
- Subnets públicas y privadas
- Internet Gateway y NAT Gateway
- Route tables
- **Código**: Ver configuración VPC en `main.tf`

#### IAM (Identity and Access Management)
- Roles para servicios (ECS Task Role, ECS Execution Role)
- Políticas de mínimo privilegio
- Service-linked roles

#### Security Groups
- Reglas de entrada y salida
- Principio de least privilege
- Segmentación por capas (ALB, ECS, RDS)

#### AWS Secrets Manager
- Almacenamiento seguro de credenciales
- Rotación automática de secretos
- Integración con ECS y RDS

### 6. Observabilidad y Monitoreo

#### CloudWatch
- Logs centralizados
- Métricas de infraestructura y aplicación
- Alarmas y notificaciones
- Dashboards personalizados

#### Alternativas Enterprise
- **Splunk**: SIEM y análisis avanzado de logs
- **Datadog**: Monitoreo unificado multi-cloud
- **New Relic**: APM y observabilidad de aplicaciones

### 7. Servicios de Datos AWS

#### AWS Glue
- Data catalog y ETL serverless
- Crawlers para descubrimiento de datos
- Integración con S3 y RDS

#### Amazon Athena
- Queries SQL sobre S3
- Serverless, pay-per-query
- Integración con Glue catalog

## Lab Local (Sin Coste) 🆓

¿Quieres practicar sin gastar en AWS? Tenemos un **laboratorio 100% local** que simula servicios de AWS:

### 🎯 ¿Qué incluye el Lab Local?

- **Aplicación containerizada** (simula ECS Fargate)
- **PostgreSQL** (simula Amazon RDS)
- **LocalStack** (simula S3, Secrets Manager, CloudWatch, IAM)
- **MinIO** (alternativa visual a S3)
- **DevContainer** (entorno preconfigurado con todas las herramientas)

### 🚀 Inicio Rápido con DevContainer

Si usas **VS Code**, el entorno está listo para usar con Remote - Containers:

1. Instala VS Code + Docker Desktop + extensión Remote - Containers
2. Abre esta carpeta en VS Code
3. Click en "Reopen in Container" cuando aparezca la notificación
4. Una vez dentro del container:
   ```bash
   cd labs/lab-01-local
   make up      # Inicia todos los servicios
   make check   # Verifica que todo funciona
   make info    # Muestra URLs e información
   ```

Ver guía completa: [.devcontainer/README-codespaces.md](.devcontainer/README-codespaces.md)

### 🏗️ Sin DevContainer (Instalación Local)

Si prefieres trabajar sin DevContainer, solo necesitas Docker y Docker Compose:

```bash
cd labs/lab-01-local

# Ver comandos disponibles
make help

# Iniciar servicios
make up

# Verificar que todo funciona
make check

# Ver logs
make logs

# Detener servicios
make down
```

**Documentación completa del lab**: [labs/lab-01-local/README.md](labs/lab-01-local/README.md)

### ✨ Ventajas del Lab Local

- ✅ **Costo cero**: No necesitas cuenta AWS ni tarjeta de crédito
- ✅ **Aprendizaje seguro**: Experimenta sin miedo a generar costos
- ✅ **Iteración rápida**: Desarrolla y prueba localmente antes de ir a la nube
- ✅ **Offline**: Trabaja sin conexión a internet
- ✅ **Mismos conceptos**: Lo que aprendas aplica directamente a AWS real

### 📊 Servicios Disponibles

Una vez levantes el lab con `make up`, tendrás acceso a:

| Servicio | URL | Descripción |
|----------|-----|-------------|
| Flask App | http://localhost:8080 | Aplicación de ejemplo con endpoints |
| PostgreSQL | localhost:5432 | Base de datos (user: devuser, pass: devpass123) |
| LocalStack | http://localhost:4566 | Servicios AWS simulados |
| MinIO Console | http://localhost:9001 | Interfaz web para S3 (user: minioadmin) |

### 🎓 Ejercicios del Lab

El lab incluye ejercicios prácticos para:

1. Explorar bases de datos PostgreSQL
2. Interactuar con APIs REST
3. Simular servicios AWS con LocalStack
4. Gestionar objetos en S3 (MinIO)
5. Modificar y reconstruir aplicaciones containerizadas

**¿Listo para empezar?** → [labs/lab-01-local/README.md](labs/lab-01-local/README.md)

---

## Cómo Usar los Ejemplos de AWS

### Paso 1: Revisar el Código Terraform

```bash
cd examples/terraform/
cat main.tf variables.tf outputs.tf
```

Lee los comentarios para entender cada recurso y su propósito.

### Paso 2: Configurar Variables

Crea un archivo `terraform.tfvars` (NO lo subas a git):

```hcl
aws_region      = "us-east-1"
project_name    = "mi-proyecto"
db_username     = "admin"
db_password     = "ChangeMe123!"  # Usa Secrets Manager en producción
ecr_image       = "123456789012.dkr.ecr.us-east-1.amazonaws.com/mi-app:latest"
```

### Paso 3: Inicializar y Validar

```bash
terraform init
terraform fmt
terraform validate
terraform plan
```

### Paso 4: Aplicar Cambios (Opcional)

**⚠️ ATENCIÓN**: Esto creará recursos reales en AWS que pueden generar costos.

```bash
terraform apply
```

### Paso 5: Limpiar Recursos

```bash
terraform destroy
```

## De Open Source a Enterprise

| Aspecto | Open Source | Enterprise (AWS) |
|---------|-------------|------------------|
| **IaC** | Terraform (OSS) | Terraform Enterprise, AWS CDK |
| **Containers** | Docker, Docker Compose | Amazon ECS, EKS (Kubernetes) |
| **Orchestration** | Kubernetes (self-managed) | Amazon EKS, ECS Fargate |
| **CI/CD** | GitHub Actions, GitLab CI | AWS CodePipeline, Jenkins Enterprise |
| **Monitoring** | Prometheus + Grafana | CloudWatch, Datadog, Splunk |
| **Secrets** | HashiCorp Vault (OSS) | AWS Secrets Manager, Vault Enterprise |
| **Databases** | PostgreSQL (self-hosted) | Amazon RDS, Aurora |
| **ETL** | Apache Airflow (self-hosted) | AWS Glue, Airflow en MWAA |
| **Data Lake** | MinIO, HDFS | Amazon S3 |
| **Networking** | VPN, firewalls DIY | AWS VPC, Transit Gateway, PrivateLink |

### ¿Cuándo elegir Open Source vs Enterprise?

**Open Source cuando**:
- Presupuesto limitado
- Control total sobre la infraestructura
- Flexibilidad para customizar
- Comunidad activa y soporte comunitario

**Enterprise/AWS cuando**:
- Necesitas soporte 24/7 con SLAs
- Escalabilidad sin gestión de infraestructura
- Compliance y certificaciones requeridas
- Tiempo al mercado es crítico
- Equipos pequeños sin expertos en DevOps

### Habilidades Transferibles

Lo que aprendas con herramientas open source es **directamente aplicable** en entornos enterprise:
- Conceptos de containerización
- Principios de IaC
- Networking y seguridad
- Observabilidad y debugging
- CI/CD pipelines

La diferencia está en la **implementación específica**, no en los fundamentos.

## Recursos Adicionales

### Documentación Oficial
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Amazon ECS Developer Guide](https://docs.aws.amazon.com/ecs/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### Tutoriales Recomendados
- [Getting Started with Terraform on AWS](https://learn.hashicorp.com/collections/terraform/aws-get-started)
- [ECS Workshop](https://ecsworkshop.com/)
- [AWS DevOps Blog](https://aws.amazon.com/blogs/devops/)

### Libros
- "Terraform: Up & Running" - Yevgeniy Brikman
- "The DevOps Handbook" - Gene Kim
- "Site Reliability Engineering" - Google

### Certificaciones
- AWS Certified DevOps Engineer - Professional
- AWS Certified Solutions Architect - Associate
- HashiCorp Certified: Terraform Associate

## Mejores Prácticas

### Seguridad
- ✅ Nunca hardcodees credenciales en código
- ✅ Usa AWS Secrets Manager o Parameter Store
- ✅ Habilita MFA en cuentas AWS
- ✅ Aplica principio de mínimo privilegio
- ✅ Escanea imágenes Docker por vulnerabilidades
- ✅ Rota credenciales regularmente

### Infraestructura
- ✅ Usa módulos de Terraform reutilizables
- ✅ Versiona tu código de infraestructura
- ✅ Mantén estados de Terraform en S3 con lock en DynamoDB
- ✅ Usa workspaces para separar entornos (dev/staging/prod)
- ✅ Implementa tags consistentes para recursos

### CI/CD
- ✅ Ejecuta `terraform plan` en PRs antes de merge
- ✅ Requiere aprobación manual para `terraform apply` en producción
- ✅ Automatiza tests de infraestructura
- ✅ Mantén logs de todos los despliegues
- ✅ Implementa rollback automático en fallos

### Costos
- ✅ Usa Fargate para workloads variables
- ✅ Implementa auto-scaling
- ✅ Configura alarmas de presupuesto en AWS
- ✅ Destruye recursos de dev/test cuando no se usen
- ✅ Revisa AWS Cost Explorer mensualmente

## Próximos Pasos

1. **Lee el README completo** (este archivo)
2. **Revisa los ejemplos de código** en `examples/`
3. **Completa la actividad interactiva** en `actividad-interactiva.md`
4. **Documenta tu progreso** en `progreso.md`
5. **Consulta las soluciones** en `retroalimentacion.md`

## Consejos para el Aprendizaje

- 💡 No intentes aplicar todo a producción de inmediato
- 💡 Empieza con pequeños experimentos en entornos de desarrollo
- 💡 Lee y entiende los mensajes de error de Terraform
- 💡 Usa `terraform plan` frecuentemente antes de `apply`
- 💡 Mantén copias de seguridad del state file de Terraform
- 💡 Aprende a leer la documentación oficial de AWS

---

**¿Listo para comenzar?**

Dirígete a [actividad-interactiva.md](actividad-interactiva.md) para poner en práctica estos conceptos con ejercicios guiados.

**¡DevOps es cultura, no solo herramientas!** 🚀🔧☁️
