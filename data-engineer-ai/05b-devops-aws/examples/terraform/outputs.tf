# Outputs de la infraestructura Terraform
# Estos valores son útiles para conectar componentes y debugging

# ========================================
# VPC and Networking Outputs
# ========================================

output "vpc_id" {
  description = "ID del VPC creado"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "CIDR block del VPC"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "IDs de las subnets públicas"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs de las subnets privadas"
  value       = aws_subnet.private[*].id
}

output "internet_gateway_id" {
  description = "ID del Internet Gateway"
  value       = aws_internet_gateway.main.id
}

# ========================================
# Security Groups Outputs
# ========================================

output "ecs_security_group_id" {
  description = "ID del Security Group de ECS"
  value       = aws_security_group.ecs_tasks.id
}

output "rds_security_group_id" {
  description = "ID del Security Group de RDS"
  value       = aws_security_group.rds.id
}

# ========================================
# IAM Outputs
# ========================================

output "ecs_task_execution_role_arn" {
  description = "ARN del IAM Role para Task Execution"
  value       = aws_iam_role.ecs_task_execution_role.arn
}

output "ecs_task_role_arn" {
  description = "ARN del IAM Role para Tasks"
  value       = aws_iam_role.ecs_task_role.arn
}

# ========================================
# ECS Outputs
# ========================================

output "ecs_cluster_id" {
  description = "ID del ECS Cluster"
  value       = aws_ecs_cluster.main.id
}

output "ecs_cluster_name" {
  description = "Nombre del ECS Cluster"
  value       = aws_ecs_cluster.main.name
}

output "ecs_cluster_arn" {
  description = "ARN del ECS Cluster"
  value       = aws_ecs_cluster.main.arn
}

output "ecs_service_id" {
  description = "ID del ECS Service"
  value       = aws_ecs_service.main.id
}

output "ecs_service_name" {
  description = "Nombre del ECS Service"
  value       = aws_ecs_service.main.name
}

output "ecs_task_definition_arn" {
  description = "ARN de la Task Definition"
  value       = aws_ecs_task_definition.app.arn
}

output "ecs_task_definition_family" {
  description = "Familia de la Task Definition"
  value       = aws_ecs_task_definition.app.family
}

output "ecs_task_definition_revision" {
  description = "Revisión de la Task Definition"
  value       = aws_ecs_task_definition.app.revision
}

# ========================================
# CloudWatch Outputs
# ========================================

output "cloudwatch_log_group" {
  description = "Nombre del CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.ecs.name
}

output "cloudwatch_log_group_arn" {
  description = "ARN del CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.ecs.arn
}

# ========================================
# RDS Outputs
# ========================================

output "db_instance_id" {
  description = "ID de la instancia RDS"
  value       = aws_db_instance.main.id
}

output "db_instance_arn" {
  description = "ARN de la instancia RDS"
  value       = aws_db_instance.main.arn
}

output "db_endpoint" {
  description = "Endpoint de conexión a RDS (host:port)"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}

output "db_address" {
  description = "Hostname de la instancia RDS"
  value       = aws_db_instance.main.address
  sensitive   = true
}

output "db_port" {
  description = "Puerto de conexión a RDS"
  value       = aws_db_instance.main.port
}

output "db_name" {
  description = "Nombre de la base de datos"
  value       = aws_db_instance.main.db_name
}

output "db_username" {
  description = "Usuario master de la base de datos"
  value       = aws_db_instance.main.username
  sensitive   = true
}

# ========================================
# Connection Information (para debugging)
# ========================================

output "connection_info" {
  description = "Información de conexión para debugging"
  value = {
    region              = var.aws_region
    environment         = var.environment
    ecs_cluster         = aws_ecs_cluster.main.name
    ecs_service         = aws_ecs_service.main.name
    db_host             = aws_db_instance.main.address
    db_port             = aws_db_instance.main.port
    db_name             = aws_db_instance.main.db_name
    cloudwatch_logs     = aws_cloudwatch_log_group.ecs.name
  }
  sensitive = true
}

# ========================================
# Comandos útiles (como output)
# ========================================

output "useful_commands" {
  description = "Comandos útiles para interactuar con la infraestructura"
  value = <<-EOT
    # Ver tareas corriendo en ECS:
    aws ecs list-tasks --cluster ${aws_ecs_cluster.main.name} --region ${var.aws_region}
    
    # Ver logs en CloudWatch:
    aws logs tail ${aws_cloudwatch_log_group.ecs.name} --follow --region ${var.aws_region}
    
    # Describir el servicio ECS:
    aws ecs describe-services --cluster ${aws_ecs_cluster.main.name} --services ${aws_ecs_service.main.name} --region ${var.aws_region}
    
    # Conectar a RDS (desde una tarea ECS o EC2 en la misma VPC):
    psql -h ${aws_db_instance.main.address} -p ${aws_db_instance.main.port} -U ${aws_db_instance.main.username} -d ${aws_db_instance.main.db_name}
    
    # Ver métricas de RDS:
    aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name CPUUtilization --dimensions Name=DBInstanceIdentifier,Value=${aws_db_instance.main.id} --statistics Average --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) --end-time $(date -u +%Y-%m-%dT%H:%M:%S) --period 300 --region ${var.aws_region}
  EOT
}
