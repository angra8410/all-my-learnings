.PHONY: help up down check logs clean status

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

up: ## Levanta todos los servicios del lab
	@echo "$(GREEN)Iniciando servicios del laboratorio...$(NC)"
	$(COMPOSE) up -d
	@echo "$(GREEN)✓ Servicios iniciados$(NC)"
	@echo "$(YELLOW)Instalando pytest...$(NC)"
	@sleep 2
	$(COMPOSE) exec -T app pip install pytest > /dev/null 2>&1 || true
	@$(MAKE) status

down: ## Detiene todos los servicios del lab
	@echo "$(YELLOW)Deteniendo servicios del laboratorio...$(NC)"
	$(COMPOSE) down
	@echo "$(GREEN)✓ Servicios detenidos$(NC)"

logs: ## Muestra logs de todos los servicios
	$(COMPOSE) logs -f

check: ## Ejecuta los tests y genera revision.md
	@echo "$(GREEN)Ejecutando tests y generando calificación...$(NC)"
	@$(COMPOSE) exec -T app python tests/check_ejercicios.sh

status: ## Muestra el estado de los servicios
	@echo "$(GREEN)Estado de los servicios:$(NC)"
	@$(COMPOSE) ps

clean: down ## Detiene servicios y elimina volúmenes
	@echo "$(YELLOW)Limpiando...$(NC)"
	$(COMPOSE) down -v
	@echo "$(GREEN)✓ Limpieza completada$(NC)"

restart: ## Reinicia todos los servicios
	@echo "$(YELLOW)Reiniciando servicios...$(NC)"
	$(COMPOSE) restart
	@echo "$(GREEN)✓ Servicios reiniciados$(NC)"

shell: ## Abre shell en el contenedor de la aplicación
	$(COMPOSE) exec app /bin/bash

info: ## Muestra información del laboratorio
	@echo "$(GREEN)====================================$(NC)"
	@echo "$(GREEN) Lab 01: Lógica y Programación$(NC)"
	@echo "$(GREEN)====================================$(NC)"
	@echo ""
	@echo "$(YELLOW)Comandos útiles:$(NC)"
	@echo "  • make up         - Iniciar servicios"
	@echo "  • make down       - Detener servicios"
	@echo "  • make check      - Ejecutar tests y generar calificación"
	@echo "  • make logs       - Ver logs"
	@echo ""
	@echo "$(YELLOW)Archivos importantes:$(NC)"
	@echo "  • revision.md     - Calificación y resultados"
	@echo "  • ejercicios/     - Soluciones de los ejercicios"
	@echo "  • tests/          - Scripts de prueba"
	@echo ""
