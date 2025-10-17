.PHONY: help install up down build rebuild logs check clean status ps

# Variables
COMPOSE_FILE := docker-compose.yml
COMPOSE := docker compose -f $(COMPOSE_FILE)

# Colores para output
GREEN  := \033[0;32m
YELLOW := \033[0;33m
RED    := \033[0;31m
NC     := \033[0m # No Color

help: ## Muestra esta ayuda
	@echo "$(GREEN)Comandos disponibles:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-15s$(NC) %s\n", $$1, $$2}'

install: ## Instala dependencias necesarias (no requerido en devcontainer)
	@echo "$(GREEN)Verificando dependencias...$(NC)"
	@command -v docker >/dev/null 2>&1 || { echo "$(RED)Error: Docker no está instalado$(NC)"; exit 1; }
	@command -v docker compose >/dev/null 2>&1 || { echo "$(RED)Error: Docker Compose no está instalado$(NC)"; exit 1; }
	@echo "$(GREEN)✓ Todas las dependencias están instaladas$(NC)"

up: ## Levanta todos los servicios del lab
	@echo "$(GREEN)Iniciando servicios del laboratorio...$(NC)"
	$(COMPOSE) up -d
	@echo "$(GREEN)✓ Servicios iniciados$(NC)"
	@echo "$(YELLOW)Esperando a que los servicios estén listos...$(NC)"
	@sleep 10
	@$(MAKE) status

down: ## Detiene todos los servicios del lab
	@echo "$(YELLOW)Deteniendo servicios del laboratorio...$(NC)"
	$(COMPOSE) down
	@echo "$(GREEN)✓ Servicios detenidos$(NC)"

build: ## Construye las imágenes Docker
	@echo "$(GREEN)Construyendo imágenes...$(NC)"
	$(COMPOSE) build --no-cache
	@echo "$(GREEN)✓ Imágenes construidas$(NC)"

rebuild: down build up ## Reconstruye y reinicia todos los servicios

logs: ## Muestra logs de todos los servicios
	$(COMPOSE) logs -f

logs-app: ## Muestra logs de la aplicación
	$(COMPOSE) logs -f app

logs-postgres: ## Muestra logs de PostgreSQL
	$(COMPOSE) logs -f lab_postgres

logs-localstack: ## Muestra logs de LocalStack
	$(COMPOSE) logs -f localstack

logs-minio: ## Muestra logs de MinIO
	$(COMPOSE) logs -f minio

check: ## Verifica que todos los servicios estén funcionando
	@echo "$(GREEN)Verificando servicios...$(NC)"
	@bash tests/check_health.sh

status: ## Muestra el estado de los servicios
	@echo "$(GREEN)Estado de los servicios:$(NC)"
	@$(COMPOSE) ps

ps: status ## Alias para status

clean: down ## Detiene servicios y elimina volúmenes
	@echo "$(YELLOW)Limpiando volúmenes...$(NC)"
	$(COMPOSE) down -v
	@echo "$(GREEN)✓ Volúmenes eliminados$(NC)"

restart: ## Reinicia todos los servicios
	@echo "$(YELLOW)Reiniciando servicios...$(NC)"
	$(COMPOSE) restart
	@echo "$(GREEN)✓ Servicios reiniciados$(NC)"

restart-app: ## Reinicia solo la aplicación
	$(COMPOSE) restart app

shell-app: ## Abre shell en el contenedor de la aplicación
	$(COMPOSE) exec app /bin/bash

shell-postgres: ## Abre psql en PostgreSQL
	$(COMPOSE) exec lab_postgres psql -U devuser -d appdb

test-app: ## Prueba el endpoint de la aplicación
	@echo "$(GREEN)Probando aplicación...$(NC)"
	@curl -s http://localhost:8080/ | jq . || echo "$(RED)Error al conectar con la aplicación$(NC)"

test-health: ## Prueba el endpoint de health
	@echo "$(GREEN)Probando health check...$(NC)"
	@curl -s http://localhost:8080/health | jq . || echo "$(RED)Error en health check$(NC)"

test-info: ## Prueba el endpoint de info
	@echo "$(GREEN)Probando info endpoint...$(NC)"
	@curl -s http://localhost:8080/info | jq . || echo "$(RED)Error al obtener info$(NC)"

test-db: ## Verifica conexión a la base de datos
	@echo "$(GREEN)Verificando base de datos...$(NC)"
	@$(COMPOSE) exec -T lab_postgres psql -U devuser -d appdb -c "SELECT COUNT(*) as total_users FROM users;" || echo "$(RED)Error al conectar con la base de datos$(NC)"

test-localstack: ## Verifica LocalStack
	@echo "$(GREEN)Verificando LocalStack...$(NC)"
	@curl -s http://localhost:4566/_localstack/health | jq . || echo "$(RED)Error al conectar con LocalStack$(NC)"

test-minio: ## Verifica MinIO
	@echo "$(GREEN)Verificando MinIO...$(NC)"
	@curl -s http://localhost:9000/minio/health/live || echo "$(RED)Error al conectar con MinIO$(NC)"
	@echo ""
	@echo "$(YELLOW)Consola MinIO: http://localhost:9001$(NC)"
	@echo "$(YELLOW)Usuario: minioadmin / Contraseña: minioadmin123$(NC)"

test-all: test-health test-db test-localstack test-minio ## Ejecuta todas las pruebas

info: ## Muestra información del laboratorio
	@echo "$(GREEN)====================================$(NC)"
	@echo "$(GREEN) Lab 01: Entorno DevOps Local$(NC)"
	@echo "$(GREEN)====================================$(NC)"
	@echo ""
	@echo "$(YELLOW)URLs de los servicios:$(NC)"
	@echo "  • Aplicación:     http://localhost:8080"
	@echo "  • PostgreSQL:     localhost:5432"
	@echo "  • LocalStack:     http://localhost:4566"
	@echo "  • MinIO Console:  http://localhost:9001"
	@echo ""
	@echo "$(YELLOW)Credenciales PostgreSQL:$(NC)"
	@echo "  • Usuario:   devuser"
	@echo "  • Password:  devpass123"
	@echo "  • Database:  appdb"
	@echo ""
	@echo "$(YELLOW)Credenciales MinIO:$(NC)"
	@echo "  • Usuario:   minioadmin"
	@echo "  • Password:  minioadmin123"
	@echo ""
	@echo "$(YELLOW)Comandos útiles:$(NC)"
	@echo "  • make up         - Iniciar servicios"
	@echo "  • make down       - Detener servicios"
	@echo "  • make check      - Verificar servicios"
	@echo "  • make logs       - Ver logs"
	@echo "  • make test-all   - Ejecutar todas las pruebas"
	@echo ""
