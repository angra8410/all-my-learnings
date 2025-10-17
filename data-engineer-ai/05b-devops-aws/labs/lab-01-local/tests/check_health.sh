#!/bin/bash

# Script para verificar la salud de todos los servicios del laboratorio
# Este script valida que los servicios estén funcionando correctamente

set -e

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
    else
        echo -e "${RED}✗${NC} $2"
    fi
}

# Función para verificar que un servicio responde
check_http() {
    local url=$1
    local name=$2
    local max_retries=5
    local retry=0
    
    while [ $retry -lt $max_retries ]; do
        if curl -sf "$url" > /dev/null 2>&1; then
            print_status 0 "$name está respondiendo correctamente"
            return 0
        fi
        retry=$((retry + 1))
        if [ $retry -lt $max_retries ]; then
            echo -e "${YELLOW}Reintentando $name ($retry/$max_retries)...${NC}"
            sleep 2
        fi
    done
    
    print_status 1 "$name no está respondiendo"
    return 1
}

# Función para verificar PostgreSQL
check_postgres() {
    local max_retries=5
    local retry=0
    
    while [ $retry -lt $max_retries ]; do
        if docker compose exec -T lab_postgres pg_isready -U devuser -d appdb > /dev/null 2>&1; then
            print_status 0 "PostgreSQL está listo y aceptando conexiones"
            
            # Verificar que las tablas existen
            if docker compose exec -T lab_postgres psql -U devuser -d appdb -c "SELECT COUNT(*) FROM users;" > /dev/null 2>&1; then
                print_status 0 "Tablas de base de datos inicializadas correctamente"
            else
                print_status 1 "Las tablas de base de datos no están inicializadas"
                return 1
            fi
            return 0
        fi
        retry=$((retry + 1))
        if [ $retry -lt $max_retries ]; then
            echo -e "${YELLOW}Reintentando PostgreSQL ($retry/$max_retries)...${NC}"
            sleep 2
        fi
    done
    
    print_status 1 "PostgreSQL no está disponible"
    return 1
}

# Banner
echo -e "${GREEN}======================================${NC}"
echo -e "${GREEN}  Verificación de Salud del Lab${NC}"
echo -e "${GREEN}======================================${NC}"
echo ""

# Verificar que docker compose está ejecutándose
if ! docker compose ps | grep -q "Up"; then
    echo -e "${RED}Error: Los servicios no están ejecutándose${NC}"
    echo -e "${YELLOW}Ejecuta 'make up' para iniciar los servicios${NC}"
    exit 1
fi

# Contador de fallos
FAILED=0

# Verificar aplicación Flask
echo -e "${YELLOW}Verificando Aplicación Flask...${NC}"
if check_http "http://localhost:8080/health" "Flask App (health endpoint)"; then
    # Verificar endpoint principal
    check_http "http://localhost:8080/" "Flask App (home endpoint)" || FAILED=$((FAILED + 1))
    
    # Verificar endpoint info
    check_http "http://localhost:8080/info" "Flask App (info endpoint)" || FAILED=$((FAILED + 1))
else
    FAILED=$((FAILED + 1))
fi
echo ""

# Verificar PostgreSQL
echo -e "${YELLOW}Verificando PostgreSQL...${NC}"
check_postgres || FAILED=$((FAILED + 1))
echo ""

# Verificar LocalStack
echo -e "${YELLOW}Verificando LocalStack...${NC}"
check_http "http://localhost:4566/_localstack/health" "LocalStack" || FAILED=$((FAILED + 1))
echo ""

# Verificar MinIO
echo -e "${YELLOW}Verificando MinIO...${NC}"
check_http "http://localhost:9000/minio/health/live" "MinIO (API)" || FAILED=$((FAILED + 1))
check_http "http://localhost:9001" "MinIO (Console)" || FAILED=$((FAILED + 1))
echo ""

# Resumen final
echo -e "${GREEN}======================================${NC}"
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ Todos los servicios están funcionando correctamente${NC}"
    echo ""
    echo -e "${YELLOW}URLs disponibles:${NC}"
    echo "  • Aplicación:     http://localhost:8080"
    echo "  • PostgreSQL:     localhost:5432"
    echo "  • LocalStack:     http://localhost:4566"
    echo "  • MinIO Console:  http://localhost:9001"
    echo ""
    echo -e "${YELLOW}Siguiente paso:${NC} Consulta README.md para ejemplos de uso"
    exit 0
else
    echo -e "${RED}✗ $FAILED servicio(s) con problemas${NC}"
    echo ""
    echo -e "${YELLOW}Sugerencias:${NC}"
    echo "  1. Verifica los logs: make logs"
    echo "  2. Reinicia los servicios: make restart"
    echo "  3. Reconstruye si es necesario: make rebuild"
    exit 1
fi
