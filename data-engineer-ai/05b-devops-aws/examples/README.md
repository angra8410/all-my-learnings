# Ejemplos de DevOps y AWS

Este directorio contiene ejemplos prácticos de:
- Infrastructure as Code con Terraform
- Containerización con Docker
- CI/CD con GitHub Actions

## Estructura

```
examples/
├── terraform/              # Infraestructura como código
│   ├── main.tf            # Recursos principales (VPC, ECS, RDS)
│   ├── variables.tf       # Variables configurables
│   ├── outputs.tf         # Outputs útiles
│   └── terraform.tfvars.example  # Plantilla de variables
├── docker/                # Aplicación containerizada
│   ├── Dockerfile         # Imagen Docker
│   └── app.py            # Aplicación Python simple
└── .github/workflows/     # CI/CD
    └── ci-cd-infra.yml   # Pipeline automatizado
```

## Inicio Rápido

### 1. Terraform

```bash
cd terraform/

# Copiar plantilla de variables
cp terraform.tfvars.example terraform.tfvars

# Editar terraform.tfvars con tus valores
nano terraform.tfvars

# Inicializar Terraform
terraform init

# Ver qué se va a crear
terraform plan

# Aplicar cambios (⚠️ crea recursos reales en AWS)
# terraform apply

# Destruir recursos cuando termines
# terraform destroy
```

### 2. Docker

```bash
cd docker/

# Construir imagen
docker build -t devops-app:latest .

# Ejecutar localmente
docker run -p 8080:8080 devops-app:latest

# Probar health endpoint
curl http://localhost:8080/health
```

### 3. GitHub Actions

El workflow en `.github/workflows/ci-cd-infra.yml` se ejecuta automáticamente en:
- Push a `main` o `develop`
- Pull requests
- Manualmente (workflow_dispatch)

**Secretos requeridos** (configurar en GitHub Settings > Secrets):
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `ECR_REPOSITORY`
- `ECS_CLUSTER`
- `ECS_SERVICE`
- `ECS_TASK_DEFINITION_FAMILY`
- `ECS_CONTAINER_NAME`
- `DB_USERNAME`
- `DB_PASSWORD`

## Notas Importantes

⚠️ **Costos**: Ejecutar `terraform apply` crea recursos reales en AWS que pueden generar costos. Usa `terraform destroy` cuando termines.

⚠️ **Seguridad**: Nunca subas `terraform.tfvars` o archivos con credenciales a git. Ya están en `.gitignore`.

⚠️ **Free Tier**: Los ejemplos usan recursos elegibles para AWS Free Tier cuando es posible (db.t3.micro, ECS Fargate con recursos mínimos).

## Validación Sin Crear Recursos

Para aprender sin crear recursos reales:

```bash
# Solo validar sintaxis
terraform validate

# Ver plan de ejecución sin aplicar
terraform plan

# Construir imagen Docker localmente
docker build -t test .
```

## Recursos Adicionales

- [Documentación de Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Guía de ECS](https://docs.aws.amazon.com/ecs/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Troubleshooting

### Error: "No credentials found"
```bash
aws configure
# Ingresa tu Access Key ID y Secret Access Key
```

### Error: "Image not found in ECR"
Primero crea el repositorio ECR y sube una imagen:
```bash
aws ecr create-repository --repository-name my-app
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

### ECS task no inicia
- Verifica logs en CloudWatch: `/ecs/<project-name>`
- Verifica que la imagen ECR exista y sea accesible
- Verifica IAM roles tienen permisos correctos

---

Para más información, consulta el [README principal del módulo](../README.md) y la [actividad interactiva](../actividad-interactiva.md).
