# Variables de configuración para infraestructura de ECS + Fargate + RDS
# Este archivo define todas las variables configurables del proyecto

# ========================================
# General Configuration
# ========================================

variable "aws_region" {
  description = "Región de AWS donde se desplegarán los recursos"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nombre del proyecto - se usa como prefijo para todos los recursos"
  type        = string
  default     = "devops-learning"

  validation {
    condition     = can(regex("^[a-z0-9-]+$", var.project_name))
    error_message = "El nombre del proyecto solo puede contener letras minúsculas, números y guiones."
  }
}

variable "environment" {
  description = "Ambiente de despliegue (dev, staging, prod)"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "El ambiente debe ser dev, staging o prod."
  }
}

# ========================================
# ECS Configuration
# ========================================

variable "ecr_image" {
  description = "URI de la imagen Docker en ECR (ej: 123456789012.dkr.ecr.us-east-1.amazonaws.com/app:latest)"
  type        = string
  default     = "public.ecr.aws/nginx/nginx:latest"  # Placeholder - cambiar por tu imagen

  validation {
    condition     = can(regex("^.+:.+$", var.ecr_image))
    error_message = "La imagen debe tener el formato repository:tag"
  }
}

variable "task_cpu" {
  description = "CPU units para la task (256, 512, 1024, 2048, 4096)"
  type        = number
  default     = 256

  validation {
    condition     = contains([256, 512, 1024, 2048, 4096], var.task_cpu)
    error_message = "CPU debe ser 256, 512, 1024, 2048 o 4096."
  }
}

variable "task_memory" {
  description = "Memoria para la task en MB (debe ser compatible con CPU)"
  type        = number
  default     = 512

  validation {
    condition     = var.task_memory >= 512 && var.task_memory <= 30720
    error_message = "La memoria debe estar entre 512 MB y 30720 MB."
  }
}

variable "desired_count" {
  description = "Número de tasks que deben estar corriendo"
  type        = number
  default     = 1

  validation {
    condition     = var.desired_count >= 0 && var.desired_count <= 10
    error_message = "El número de tasks debe estar entre 0 y 10."
  }
}

# ========================================
# RDS Configuration
# ========================================

variable "db_instance_class" {
  description = "Clase de instancia RDS (ej: db.t3.micro, db.t3.small)"
  type        = string
  default     = "db.t3.micro"  # Free tier elegible
}

variable "db_name" {
  description = "Nombre de la base de datos inicial"
  type        = string
  default     = "appdb"

  validation {
    condition     = can(regex("^[a-zA-Z][a-zA-Z0-9_]*$", var.db_name))
    error_message = "El nombre de la base de datos debe empezar con letra y contener solo letras, números y guiones bajos."
  }
}

variable "db_username" {
  description = "Usuario master de la base de datos"
  type        = string
  default     = "dbadmin"

  validation {
    condition     = length(var.db_username) >= 1 && length(var.db_username) <= 16
    error_message = "El username debe tener entre 1 y 16 caracteres."
  }
}

variable "db_password" {
  description = "Contraseña del usuario master (usar Secrets Manager en producción)"
  type        = string
  sensitive   = true
  default     = "ChangeMe123!"  # CAMBIAR INMEDIATAMENTE - Solo para demos

  validation {
    condition     = length(var.db_password) >= 8
    error_message = "La contraseña debe tener al menos 8 caracteres."
  }
}

# ========================================
# Outputs de Variables (para debug)
# ========================================

# Nota: No hacer output de valores sensibles como db_password
