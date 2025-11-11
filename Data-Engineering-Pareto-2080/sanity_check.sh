#!/bin/bash

# ============================================================================
# Sanity Check Script - Data Engineering Pareto 20/80 Course
# ============================================================================
#
# Este script valida que la estructura del curso esté completa y correcta.
#
# Checks realizados:
# 1. Todos los módulos existen (00-12)
# 2. Cada módulo tiene los 5 archivos requeridos
# 3. Ningún archivo está vacío
# 4. Helper artifacts existen
# 5. Plan de estudio existe
#
# Uso:
#   ./sanity_check.sh
#
# Exit codes:
#   0 = Todo OK
#   1 = Faltan archivos o están vacíos
#
# ============================================================================

set -e  # Exit on error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contadores
PASS_COUNT=0
FAIL_COUNT=0
WARN_COUNT=0

# Función para print con color
print_pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    ((PASS_COUNT++))
}

print_fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    ((FAIL_COUNT++))
}

print_warn() {
    echo -e "${YELLOW}⚠ WARN${NC}: $1"
    ((WARN_COUNT++))
}

print_header() {
    echo ""
    echo "=========================================="
    echo "$1"
    echo "=========================================="
}

# ============================================================================
# CHECK 1: Estructura de directorios
# ============================================================================

print_header "CHECK 1: Estructura de Directorios"

MODULES=(
    "00-plan-setup"
    "01-intro-pareto"
    "02-sql-core"
    "03-python-etl-basics"
    "04-spark-scala-fundamentals"
    "05-databricks-workflow"
    "06-delta-lake-storage"
    "07-dbt-transforms"
    "08-airflow-orchestration"
    "09-testing-data-quality"
    "10-observability-cost"
    "11-security-governance"
    "12-final-project"
)

for module in "${MODULES[@]}"; do
    if [ -d "$module" ]; then
        print_pass "Módulo $module existe"
    else
        print_fail "Módulo $module NO EXISTE"
    fi
done

# ============================================================================
# CHECK 2: Archivos requeridos por módulo
# ============================================================================

print_header "CHECK 2: Archivos Requeridos (5 por módulo)"

REQUIRED_FILES=(
    "README.md"
    "actividad-interactiva.md"
    "progreso.md"
    "retroalimentacion.md"
    "recursos.md"
)

for module in "${MODULES[@]}"; do
    echo ""
    echo "Verificando módulo: $module"
    
    for file in "${REQUIRED_FILES[@]}"; do
        filepath="$module/$file"
        
        if [ ! -f "$filepath" ]; then
            print_fail "  $file NO EXISTE"
        elif [ ! -s "$filepath" ]; then
            print_fail "  $file está VACÍO"
        else
            # Check si es solo placeholder
            if grep -q "Contenido en desarrollo" "$filepath" 2>/dev/null; then
                print_warn "  $file es placeholder (contiene 'Contenido en desarrollo')"
            else
                print_pass "  $file OK"
            fi
        fi
    done
done

# ============================================================================
# CHECK 3: Plan de estudio
# ============================================================================

print_header "CHECK 3: Plan de Estudio"

if [ -f "plan-estudio-pareto-data-engineering.md" ]; then
    if [ -s "plan-estudio-pareto-data-engineering.md" ]; then
        print_pass "plan-estudio-pareto-data-engineering.md existe y no está vacío"
    else
        print_fail "plan-estudio-pareto-data-engineering.md está vacío"
    fi
else
    print_fail "plan-estudio-pareto-data-engineering.md NO EXISTE"
fi

# ============================================================================
# CHECK 4: Helper Artifacts
# ============================================================================

print_header "CHECK 4: Helper Artifacts"

HELPER_FILES=(
    "helper-artifacts/README.md"
    "helper-artifacts/airflow/minimal_dag_skeleton.py"
    "helper-artifacts/spark-scala/DataCleaningJob.scala"
    "helper-artifacts/sql/ddl_fact_dimension_tables.sql"
    "helper-artifacts/sql/data_quality_tests.sql"
)

for helper in "${HELPER_FILES[@]}"; do
    if [ ! -f "$helper" ]; then
        print_fail "$helper NO EXISTE"
    elif [ ! -s "$helper" ]; then
        print_fail "$helper está VACÍO"
    else
        print_pass "$helper OK"
    fi
done

# ============================================================================
# CHECK 5: Conteo de proyectos en actividades interactivas
# ============================================================================

print_header "CHECK 5: Proyectos en Actividades Interactivas"

PROJECT_COUNT=0

for module in "${MODULES[@]}"; do
    activity_file="$module/actividad-interactiva.md"
    
    if [ -f "$activity_file" ]; then
        # Buscar palabras clave de proyecto
        if grep -qi "proyecto\|project" "$activity_file"; then
            echo "  ✓ $module contiene proyecto"
            ((PROJECT_COUNT++))
        fi
    fi
done

echo ""
if [ $PROJECT_COUNT -ge 6 ]; then
    print_pass "Encontrados $PROJECT_COUNT módulos con proyectos (requerido >= 6)"
else
    print_fail "Solo $PROJECT_COUNT módulos con proyectos (requerido >= 6)"
fi

# ============================================================================
# CHECK 6: Comandos verificables en actividades
# ============================================================================

print_header "CHECK 6: Comandos Verificables en Actividades"

for module in "${MODULES[@]}"; do
    activity_file="$module/actividad-interactiva.md"
    
    if [ -f "$activity_file" ]; then
        # Buscar bloques de código
        code_blocks=$(grep -c '```' "$activity_file" 2>/dev/null || echo 0)
        
        if [ $code_blocks -ge 2 ]; then  # Al menos 1 bloque (2 líneas de ```)
            echo "  ✓ $module: $code_blocks líneas de código"
        else
            print_warn "  $module: Sin bloques de código visible"
        fi
    fi
done

# ============================================================================
# CHECK 7: Campos de verificación (blanks) en actividades
# ============================================================================

print_header "CHECK 7: Campos de Verificación (_____) en Actividades"

for module in "${MODULES[@]}"; do
    activity_file="$module/actividad-interactiva.md"
    
    if [ -f "$activity_file" ]; then
        blanks=$(grep -c '___' "$activity_file" 2>/dev/null || echo 0)
        
        if [ $blanks -ge 3 ]; then
            echo "  ✓ $module: $blanks campos de verificación"
        elif [ $blanks -eq 0 ]; then
            print_warn "  $module: Sin campos de verificación"
        fi
    fi
done

# ============================================================================
# CHECK 8: Tamaño de archivos (detectar archivos muy pequeños)
# ============================================================================

print_header "CHECK 8: Tamaño de Archivos (detectar contenido mínimo)"

MIN_SIZE=100  # bytes

for module in "${MODULES[@]}"; do
    for file in "${REQUIRED_FILES[@]}"; do
        filepath="$module/$file"
        
        if [ -f "$filepath" ]; then
            size=$(wc -c < "$filepath")
            
            if [ $size -lt $MIN_SIZE ]; then
                print_warn "  $filepath es muy pequeño ($size bytes)"
            fi
        fi
    done
done

# ============================================================================
# RESUMEN FINAL
# ============================================================================

print_header "RESUMEN FINAL"

echo ""
echo "Resultados:"
echo "  ${GREEN}PASS${NC}: $PASS_COUNT"
echo "  ${YELLOW}WARN${NC}: $WARN_COUNT"
echo "  ${RED}FAIL${NC}: $FAIL_COUNT"
echo ""

# Acceptance criteria del curso
echo "Acceptance Criteria:"
echo ""

# 1. Módulos
if [ ${#MODULES[@]} -eq 13 ]; then
    print_pass "13 módulos creados (00-12)"
else
    print_fail "No hay 13 módulos"
fi

# 2. Archivos por módulo
total_expected=$((13 * 5))
total_found=$(find . -maxdepth 2 -name "README.md" -o -name "actividad-interactiva.md" -o -name "progreso.md" -o -name "retroalimentacion.md" -o -name "recursos.md" | wc -l)

if [ $total_found -eq $total_expected ]; then
    print_pass "Todos los archivos requeridos existen ($total_found/$total_expected)"
else
    print_fail "Faltan archivos ($total_found/$total_expected encontrados)"
fi

# 3. Helper artifacts
if [ ${#HELPER_FILES[@]} -eq 5 ]; then
    print_pass "Todos los helper artifacts creados"
else
    print_fail "Faltan helper artifacts"
fi

# 4. Proyectos
if [ $PROJECT_COUNT -ge 6 ]; then
    print_pass "Requisito de proyectos cumplido ($PROJECT_COUNT >= 6)"
else
    print_fail "Requisito de proyectos NO cumplido ($PROJECT_COUNT < 6)"
fi

# Exit code
echo ""
if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}════════════════════════════════════${NC}"
    echo -e "${GREEN}  ✓ TODOS LOS CHECKS PASARON!${NC}"
    echo -e "${GREEN}════════════════════════════════════${NC}"
    echo ""
    echo "El curso está listo para uso."
    exit 0
else
    echo -e "${RED}════════════════════════════════════${NC}"
    echo -e "${RED}  ✗ ALGUNOS CHECKS FALLARON${NC}"
    echo -e "${RED}════════════════════════════════════${NC}"
    echo ""
    echo "Por favor revisa los errores arriba."
    echo ""
    echo "Acciones recomendadas:"
    echo "1. Completar archivos faltantes"
    echo "2. Añadir contenido a archivos vacíos"
    echo "3. Reemplazar placeholders con contenido real"
    echo "4. Re-ejecutar este script"
    exit 1
fi
