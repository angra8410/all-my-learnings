#!/bin/bash

# run.sh - Script para ejecutar el MCP Agent localmente
#
# Este script automatiza:
# 1. Creación de un entorno virtual Python (si no existe)
# 2. Activación del entorno virtual
# 3. Instalación de dependencias (pytest para testing, si es necesario)
# 4. Ejecución del agente
#
# Uso:
#   ./run.sh              # Ejecuta el agente en puerto 8000
#   ./run.sh 8080         # Ejecuta el agente en puerto 8080
#   ./run.sh test         # Ejecuta los tests unitarios
#   ./run.sh docker       # Construye y ejecuta con Docker
#

set -e  # Salir si algún comando falla

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Directorio del script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🚀 MCP Agent - Ejecutor Local${NC}"
echo -e "${BLUE}========================================${NC}"

# Función: Crear y activar entorno virtual
setup_venv() {
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}📦 Creando entorno virtual...${NC}"
        python3 -m venv venv
        echo -e "${GREEN}✅ Entorno virtual creado${NC}"
    else
        echo -e "${GREEN}✅ Entorno virtual ya existe${NC}"
    fi
    
    # Activar entorno virtual
    echo -e "${YELLOW}🔄 Activando entorno virtual...${NC}"
    source venv/bin/activate
    
    # Actualizar pip
    echo -e "${YELLOW}📦 Actualizando pip...${NC}"
    pip install --quiet --upgrade pip
    
    echo -e "${GREEN}✅ Entorno virtual activado${NC}"
}

# Función: Instalar dependencias de testing
install_test_deps() {
    echo -e "${YELLOW}📦 Instalando dependencias de testing...${NC}"
    pip install --quiet pytest pytest-cov
    echo -e "${GREEN}✅ Dependencias instaladas${NC}"
}

# Función: Ejecutar el agente
run_agent() {
    PORT=${1:-8000}
    
    echo -e "${BLUE}========================================${NC}"
    echo -e "${GREEN}🚀 Iniciando MCP Agent en puerto ${PORT}...${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
    
    python3 examples/agent.py "$PORT"
}

# Función: Ejecutar tests
run_tests() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${GREEN}🧪 Ejecutando tests unitarios...${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
    
    install_test_deps
    
    # Ejecutar pytest con verbose y coverage
    pytest tests/ -v --cov=examples --cov-report=term-missing
    
    echo ""
    echo -e "${GREEN}✅ Tests completados${NC}"
}

# Función: Ejecutar con Docker
run_docker() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${GREEN}🐳 Construyendo y ejecutando con Docker...${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
    
    cd examples
    
    # Construir la imagen
    echo -e "${YELLOW}🔨 Construyendo imagen Docker...${NC}"
    docker build -t mcp-agent:latest .
    echo -e "${GREEN}✅ Imagen construida${NC}"
    echo ""
    
    # Ejecutar el contenedor
    echo -e "${YELLOW}🚀 Ejecutando contenedor...${NC}"
    echo -e "${YELLOW}Usa Ctrl+C para detener el contenedor${NC}"
    echo ""
    docker run --rm -p 8000:8000 mcp-agent:latest
}

# Función: Mostrar ayuda
show_help() {
    echo ""
    echo -e "${GREEN}Uso:${NC}"
    echo "  ./run.sh              Ejecuta el agente en puerto 8000"
    echo "  ./run.sh 8080         Ejecuta el agente en puerto 8080"
    echo "  ./run.sh test         Ejecuta los tests unitarios"
    echo "  ./run.sh docker       Construye y ejecuta con Docker"
    echo "  ./run.sh help         Muestra esta ayuda"
    echo ""
    echo -e "${GREEN}Ejemplos:${NC}"
    echo "  ./run.sh              # Inicia el agente"
    echo "  ./run.sh 9000         # Inicia en puerto 9000"
    echo "  ./run.sh test         # Ejecuta tests"
    echo "  ./run.sh docker       # Ejecuta con Docker"
    echo ""
}

# Main: Parsear argumentos
case "${1}" in
    test)
        setup_venv
        run_tests
        ;;
    docker)
        run_docker
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        setup_venv
        run_agent "$1"
        ;;
esac
