#!/bin/bash
# MCP Agent - Execution Script
# This script runs the MCP Agent example locally

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  MCP Agent - Model Context Protocol   ${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python 3 no está instalado.${NC}"
    echo "Por favor, instala Python 3.9 o superior para continuar."
    exit 1
fi

# Display Python version
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✓${NC} $PYTHON_VERSION detectado"
echo ""

# Navigate to examples directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/examples"

echo -e "${BLUE}Ejecutando el agente MCP...${NC}"
echo ""

# Run the agent
python3 agent.py

echo ""
echo -e "${GREEN}✓${NC} Ejecución completada exitosamente!"
echo ""
echo -e "${BLUE}Próximos pasos:${NC}"
echo "  1. Revisa el código en examples/agent.py"
echo "  2. Ejecuta los tests: python -m pytest tests/test_agent_basic.py -v"
echo "  3. Construye la imagen Docker: cd examples && docker build -t mcp-agent ."
echo "  4. Ejecuta con Docker Compose: cd examples && docker-compose up"
echo ""
echo -e "${BLUE}========================================${NC}"
