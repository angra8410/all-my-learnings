# Módulo 10 — Plataforma & Pipelines en la Nube (AWS/Azure/GCP)

Objetivos:
- Desplegar un pipeline end-to-end en una de las nubes (ejemplos: AWS/GCP/Azure).

Contenido:
1. Opciones de infra: managed services vs self-managed
2. Componentes: storage (S3/GCS), compute (EC2/GKE), managed warehouses
3. Despliegue de infra con IaC (Terraform / ARM / Deployment Manager)
4. CI/CD: GitHub Actions / Azure Pipelines / Cloud Build
5. Seguridad: gestión de secretos, roles y permisos

Actividades prácticas:
- Desplegar una tubería simple: data ingest → landing storage → dbt → warehouse (ej. S3 + Snowflake).