#!/bin/bash

################################################################################
# run.sh - Script para ejecutar el MCP Agent localmente
#
# Este script facilita la ejecución del agente MCP en modo local.
# Instrucciones:
#   1. Dar permisos de ejecución: chmod +x run.sh
#   2. Ejecutar: ./run.sh
#
# Requisitos:
#   - Python 3.9 o superior instalado
#   - Estar en el directorio MCP-Agent/ del repositorio
#
# Autor: MCP Agent Team
# Versión: 0.1
################################################################################

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}  MCP Agent - Execution Script${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Check if Python is installed
echo -e "${YELLOW}Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    echo "Please install Python 3.9 or higher and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓ Python found: ${PYTHON_VERSION}${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "examples/agent.py" ]; then
    echo -e "${RED}Error: Cannot find examples/agent.py${NC}"
    echo "Please run this script from the MCP-Agent/ directory"
    exit 1
fi

# Run the agent
echo -e "${YELLOW}Running MCP Agent...${NC}"
echo ""
python3 examples/agent.py

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}============================================================${NC}"
    echo -e "${GREEN}  ✓ Agent execution completed successfully!${NC}"
    echo -e "${GREEN}============================================================${NC}"
else
    echo ""
    echo -e "${RED}============================================================${NC}"
    echo -e "${RED}  ✗ Agent execution failed${NC}"
    echo -e "${RED}============================================================${NC}"
    exit 1
fi
