# Retroalimentación y Soluciones - Módulo 5b: DevOps y AWS

## Introducción

Este documento proporciona soluciones detalladas, explicaciones y mejores prácticas para los ejercicios del módulo de DevOps y AWS. Úsalo para verificar tu comprensión y aprender de las soluciones propuestas.

---

## Sección 2: Terraform - Respuestas a Preguntas de Comprensión

### Ejercicio 2.1: Explorar el Código Terraform

**1. ¿Cuántas subnets se crean en el VPC?**

**Respuesta**: 4 subnets en total:
- 2 subnets públicas (CIDR: 10.0.1.0/24, 10.0.2.0/24)
- 2 subnets privadas (CIDR: 10.0.10.0/24, 10.0.11.0/24)

**Explicación**: Se crean subnets en diferentes Availability Zones para alta disponibilidad. Las públicas tienen acceso a internet vía Internet Gateway, mientras que las privadas (para RDS) no tienen acceso directo a internet, mejorando la seguridad.

**2. ¿Qué tipo de launch type usa el servicio ECS?**

**Respuesta**: FARGATE

**Explicación**: Fargate es serverless - AWS gestiona la infraestructura subyacente. No necesitas administrar instancias EC2. Pagas solo por los recursos que consumes (CPU/memoria). Es ideal para:
- Workloads variables
- Equipos pequeños sin expertos en infraestructura
- Prototipado rápido

**3. ¿Qué motor de base de datos usa RDS?**

**Respuesta**: PostgreSQL (versión 15.4)

**Explicación**: PostgreSQL es elegido por:
- Open source y ampliamente soportado
- Excelente para aplicaciones de datos
- ACID compliance
- Rich features (JSON, full-text search)
- Compatible con muchos ORMs y herramientas

**4. ¿Cuántos security groups se definen?**

**Respuesta**: 2 security groups:
1. `ecs_tasks` - Para contenedores ECS
2. `rds` - Para instancia RDS

**Explicación**: Separar security groups por capa es una best practice de seguridad (principio de segregación). Cada capa solo tiene los permisos mínimos necesarios.

---

### Ejercicio 2.3: Comprender Dependencias de Recursos

**¿Qué pasa si intentas crear un ECS Service antes que el VPC?**

**Respuesta**: Terraform detecta las dependencias automáticamente a través de las referencias entre recursos. Si hay una referencia circular o faltante, `terraform plan` fallará con un error de dependencia.

**Explicación técnica**:
- Terraform construye un **dependency graph** basado en las referencias entre recursos
- Los recursos se crean en el orden correcto automáticamente
- Puedes forzar dependencias explícitas con `depends_on` si es necesario

**¿Por qué RDS necesita un subnet group?**

**Respuesta**: Un subnet group especifica en qué subnets (y por tanto, en qué AZs) puede desplegarse la instancia RDS. Es requerido para:
1. **Alta disponibilidad**: RDS puede hacer failover a otra AZ
2. **Seguridad**: Controlar en qué redes privadas vive la DB
3. **Cumplimiento**: Algunas regulaciones requieren datos en ubicaciones específicas

---

## Sección 3: Docker - Mejores Prácticas

### Optimización del Dockerfile

**Mejoras aplicadas en el Dockerfile del módulo**:

1. **Imagen base slim**: `python:3.11-slim` es ~70% más pequeña que `python:3.11`

2. **Multi-stage builds** (para proyectos más complejos):
```dockerfile
# Stage 1: Build dependencies
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["python", "app.py"]
```

3. **Usuario no-root**:
```dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
```
Esto previene que el contenedor corra como root, reduciendo riesgos de seguridad.

4. **Health checks**:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1
```
Permite a ECS detectar cuando el contenedor está listo y responder a problemas.

5. **Gunicorn en producción**:
Flask's built-in server NO es para producción. Gunicorn provee:
- Workers concurrentes
- Timeouts configurables
- Mejor manejo de signals
- Production-grade reliability

---

## Sección 4: ECS y Fargate - Conceptos Avanzados

### Configuración de Network Mode

**¿Por qué `network_mode = "awsvpc"`?**

Con `awsvpc`, cada tarea ECS obtiene:
- Su propia ENI (Elastic Network Interface)
- Su propia IP privada
- Sus propios security groups

**Ventajas**:
- Mayor seguridad (aislamiento por tarea)
- Integración directa con VPC features
- Soporte para Fargate (que requiere awsvpc)

### ¿Por qué `assign_public_ip = true`?

Para Fargate, necesitas IP pública si:
1. Tus contenedores necesitan pull de imágenes de ECR (público o en otra cuenta)
2. Necesitas acceso saliente a internet
3. No tienes NAT Gateway configurado en subnets privadas

**Alternativa para producción**:
- Usa subnets privadas + NAT Gateway
- Más costoso pero más seguro
- Containers no son directamente accesibles desde internet

---

## Sección 5: RDS - Explicaciones de Configuración

### `skip_final_snapshot = true`

**¿Por qué está en true?**

Solo para entornos de desarrollo/test donde los datos no son críticos.

**En producción, SIEMPRE usa**:
```hcl
skip_final_snapshot = false
final_snapshot_identifier = "${var.project_name}-final-snapshot-${timestamp()}"
```

Esto crea un snapshot antes de destruir la DB, permitiéndote recuperar datos si es necesario.

### `publicly_accessible = false`

**Nunca cambies esto a true en producción.**

Razones:
- Expone tu DB directamente a internet
- Aumenta superficie de ataque
- Violación de compliance en muchas industrias

**Cómo conectarte a RDS privada**:
1. Desde ECS tasks en la misma VPC
2. Vía bastion host en subnet pública
3. Vía VPN o AWS Direct Connect
4. Vía AWS Systems Manager Session Manager

### Backup Configuration

```hcl
backup_retention_period = 7
backup_window          = "03:00-04:00"
```

- **backup_retention_period**: 7-35 días recomendado
- **backup_window**: Elegir horario de menor carga
- **maintenance_window**: No debe solaparse con backup_window

---

## Sección 6: CI/CD - Secretos y Seguridad

### Secretos Requeridos

| Secret | Descripción | Cómo obtenerlo |
|--------|-------------|----------------|
| `AWS_ACCESS_KEY_ID` | Credencial AWS | IAM User con permisos programáticos |
| `AWS_SECRET_ACCESS_KEY` | Secret de AWS | Mismo IAM User |
| `ECR_REPOSITORY` | Nombre repo ECR | `aws ecr describe-repositories` |
| `ECS_CLUSTER` | Nombre cluster | Output de Terraform `ecs_cluster_name` |
| `ECS_SERVICE` | Nombre servicio | Output de Terraform `ecs_service_name` |
| `ECS_TASK_DEFINITION_FAMILY` | Familia task | En `main.tf`, parámetro `family` |
| `ECS_CONTAINER_NAME` | Nombre container | En task definition JSON |
| `DB_USERNAME` | Usuario DB | Variable de Terraform |
| `DB_PASSWORD` | Password DB | ¡Nunca en código! Usa Secrets Manager |

### Mejores Prácticas de Seguridad

1. **Rotación de credenciales**:
```bash
# Rotar cada 90 días
aws iam update-access-key --access-key-id AKIA... --status Inactive
aws iam create-access-key --user-name github-actions-user
```

2. **Principio de mínimo privilegio**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:UpdateService",
        "ecs:DescribeServices",
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "*"
    }
  ]
}
```

3. **Usar OIDC en lugar de credentials** (avanzado):
GitHub Actions puede asumir IAM roles sin credenciales estáticas.

---

## Sección 7: Monitoreo y Troubleshooting

### CloudWatch Logs

**¿Dónde se almacenan los logs?**

En CloudWatch Logs, en el log group especificado en la task definition:
```hcl
resource "aws_cloudwatch_log_group" "ecs" {
  name              = "/ecs/${var.project_name}"
  retention_in_days = 7
}
```

**Cómo acceder**:
```bash
# Via CLI
aws logs tail /ecs/devops-learning --follow

# Via Console
AWS Console > CloudWatch > Logs > Log groups > /ecs/devops-learning
```

**Búsqueda de errores**:
```bash
# Filtrar por ERROR
aws logs filter-log-events \
  --log-group-name /ecs/devops-learning \
  --filter-pattern "ERROR"

# Logs de última hora
aws logs tail /ecs/devops-learning --since 1h
```

### Troubleshooting Común

#### Problema: ECS task no inicia

**Causas comunes**:
1. **Imagen ECR no existe o no es accesible**
   ```bash
   aws ecr describe-images --repository-name my-app
   ```

2. **IAM role sin permisos para pull de ECR**
   - Verificar `AmazonECSTaskExecutionRolePolicy` está attachada

3. **Health check falla inmediatamente**
   - Aumentar `startPeriod` en health check
   - Verificar que endpoint /health responde

4. **Falta de recursos**
   - Verificar CPU/memoria son suficientes para la app

**Cómo debuggear**:
```bash
# Ver eventos del servicio
aws ecs describe-services \
  --cluster my-cluster \
  --services my-service \
  --query 'services[0].events'

# Ver stopped tasks
aws ecs list-tasks --cluster my-cluster --desired-status STOPPED

# Describir una stopped task
aws ecs describe-tasks \
  --cluster my-cluster \
  --tasks arn:aws:ecs:... \
  --query 'tasks[0].stopCode'
```

#### Problema: No puedo conectar a RDS desde ECS

**Checklist**:
1. ✅ Security group de RDS permite tráfico del security group de ECS
2. ✅ RDS está en subnet privada de la misma VPC
3. ✅ Credenciales son correctas
4. ✅ DNS resolution está habilitado en VPC

**Test de conectividad desde ECS**:
```bash
# Ejecutar comando en task corriendo
aws ecs execute-command \
  --cluster my-cluster \
  --task <task-id> \
  --interactive \
  --command "sh"

# Dentro del container
nc -zv <db-endpoint> 5432
psql -h <db-endpoint> -U <username> -d <dbname>
```

---

## Sección 10: Respuestas a Evaluación Final

### 1. ¿Qué es Infrastructure as Code y cuáles son sus beneficios?

**Respuesta completa**:

Infrastructure as Code (IaC) es la práctica de gestionar y provisionar infraestructura a través de código legible por máquinas, en lugar de configuración manual.

**Beneficios principales**:

1. **Reproducibilidad**: Mismo código = misma infraestructura siempre
2. **Versionamiento**: Historial de cambios con git
3. **Revisión**: Code reviews antes de aplicar cambios
4. **Documentación**: El código ES la documentación
5. **Automatización**: Integración con CI/CD
6. **Recuperación ante desastres**: Recrear infraestructura rápidamente
7. **Testing**: Probar infraestructura antes de producción
8. **Consistencia**: Elimina "snowflake servers"

**Herramientas**:
- Terraform (multi-cloud, declarativo)
- AWS CloudFormation (AWS-specific)
- Pulumi (programático)
- Ansible (configuración)

### 2. ¿Cuál es la diferencia entre ECS EC2 launch type y Fargate?

**Respuesta**:

| Aspecto | EC2 Launch Type | Fargate |
|---------|----------------|---------|
| **Gestión de hosts** | Tú gestionas EC2 instances | AWS gestiona todo |
| **Costo** | Pagas por EC2 instances (on/reserved/spot) | Pagas por recursos usados (CPU/mem) |
| **Escalabilidad** | Manual o auto-scaling group | Automático por tarea |
| **Flexibilidad** | Mayor control (SSH, custom AMIs) | Menos control, más simple |
| **Overhead operacional** | Alto (patches, monitoring) | Bajo (solo tu app) |
| **Networking** | Bridge o awsvpc | Solo awsvpc |
| **Use case** | Apps con reqs específicos, costos optimizados | Mayoría de apps, serverless |

**Cuándo usar cada uno**:
- **Fargate**: Default para mayoría de casos, especialmente startups y equipos pequeños
- **EC2**: Workloads con requerimientos especiales (GPUs, instance storage, costos optimizados a escala)

### 3. ¿Por qué es importante usar AWS Secrets Manager en lugar de hardcodear credenciales?

**Respuesta**:

**Riesgos de hardcodear**:
1. 🚨 Credenciales en git history (nunca se borran completamente)
2. 🚨 Exposición accidental al hacer fork/public
3. 🚨 Difícil rotación (cambiar en múltiples lugares)
4. 🚨 No hay audit trail de quién accedió
5. 🚨 Violación de compliance (SOC2, HIPAA, PCI)

**Ventajas de Secrets Manager**:
1. ✅ Encriptación en reposo y en tránsito
2. ✅ Rotación automática de secretos
3. ✅ Control de acceso granular con IAM
4. ✅ Audit logging (quién, cuándo, qué)
5. ✅ Integración nativa con RDS, ECS, Lambda
6. ✅ Versionamiento de secretos
7. ✅ Replicación multi-región

**Ejemplo de uso en ECS**:
```hcl
secrets = [
  {
    name      = "DB_PASSWORD"
    valueFrom = "arn:aws:secretsmanager:us-east-1:123456789012:secret:db-password-abc123"
  }
]
```

**Alternativas**:
- AWS Systems Manager Parameter Store (más simple, menos features)
- HashiCorp Vault (self-hosted, multi-cloud)

### 4. ¿Qué ventajas tiene automatizar el despliegue con CI/CD?

**Respuesta**:

**Ventajas técnicas**:
1. **Rapidez**: Deploy en minutos vs horas/días
2. **Consistencia**: Mismo proceso cada vez
3. **Reducción de errores**: Elimina pasos manuales propensos a errores
4. **Testing automático**: Tests corren antes de deploy
5. **Rollback rápido**: Versión anterior disponible inmediatamente
6. **Trazabilidad**: Historial de qué se desplegó, cuándo y por quién

**Ventajas de negocio**:
1. **Time to market**: Features llegan a producción más rápido
2. **Feedback rápido**: Detectar problemas temprano
3. **Moral del equipo**: Menos trabajo tedioso y manual
4. **Disponibilidad**: Menos downtime por errores de deploy
5. **Innovación**: Experimentar con confianza

**Estadísticas (State of DevOps Report)**:
- Elite performers despliegan 208x más frecuentemente
- Lead time de < 1 hora (vs 1-6 meses)
- Change failure rate < 15%

### 5. ¿Cuándo elegirías RDS sobre una base de datos self-hosted en EC2?

**Respuesta**:

**Elige RDS cuando**:
1. ✅ Quieres reducir overhead operacional
2. ✅ Necesitas backups automáticos y point-in-time recovery
3. ✅ Necesitas alta disponibilidad (Multi-AZ)
4. ✅ Quieres patches automáticos de seguridad
5. ✅ Tu equipo es pequeño o no tiene DBA
6. ✅ Necesitas escalabilidad sin downtime
7. ✅ Compliance requiere backups y encriptación
8. ✅ Presupuesto permite managed service

**Elige self-hosted en EC2 cuando**:
1. ❌ Necesitas control total sobre configuración
2. ❌ Usas engine o versión no soportada por RDS
3. ❌ Necesitas acceso al OS o features específicos
4. ❌ Tienes expertise interno en administración de DBs
5. ❌ Optimización de costos a muy gran escala
6. ❌ Requisitos de latencia extremadamente bajos

**Alternativas intermedias**:
- **Amazon Aurora**: Compatible con PostgreSQL/MySQL, mejor performance
- **Aurora Serverless**: RDS serverless, auto-scaling
- **DynamoDB**: NoSQL managed, para casos de uso específicos

**Costo-beneficio**:
```
RDS db.t3.micro = ~$15/mes + storage
EC2 t3.micro + PostgreSQL = ~$8/mes + tu tiempo de gestión

Si tu tiempo vale > $7/mes, RDS gana 😊
```

---

## Conceptos Avanzados (Bonus)

### Blue/Green Deployments en ECS

```hcl
resource "aws_ecs_service" "main" {
  # ... otras configs ...
  
  deployment_controller {
    type = "CODE_DEPLOY"  # Habilita blue/green
  }
}
```

Con CodeDeploy, puedes:
- Desplegar nueva versión sin downtime
- Probar tráfico en nueva versión gradualmente
- Rollback automático si hay errores

### Terraform Workspaces

```bash
# Crear workspace para diferentes ambientes
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

# Usar workspace en código
resource "aws_instance" "example" {
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"
}
```

### Service Discovery con AWS Cloud Map

Para que servicios ECS se descubran entre sí:

```hcl
resource "aws_service_discovery_service" "app" {
  name = "my-app"
  
  dns_config {
    namespace_id = aws_service_discovery_private_dns_namespace.main.id
    
    dns_records {
      ttl  = 10
      type = "A"
    }
  }
}
```

---

## Recursos Adicionales para Profundizar

### Documentación Oficial
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS ECS Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)

### Cursos y Tutoriales
- [HashiCorp Learn - Terraform](https://learn.hashicorp.com/terraform)
- [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/)
- [ECS Workshop](https://ecsworkshop.com/)

### Libros
- "Terraform: Up & Running" - Yevgeniy Brikman
- "Amazon Web Services in Action" - Andreas Wittig
- "The DevOps Handbook" - Gene Kim

### Comunidades
- r/terraform
- r/aws
- AWS Community Builders program
- DevOps Discord/Slack channels

---

**¡Felicitaciones por completar el módulo de DevOps y AWS!** 🎉

Has aprendido habilidades fundamentales que son directamente aplicables en la industria. Continúa practicando, experimenta con diferentes configuraciones, y no tengas miedo de romper cosas en entornos de desarrollo - ¡es la mejor forma de aprender!

**Próximo paso**: Aplica estos conceptos en tu proyecto integrador y construye tu portfolio en GitHub.
