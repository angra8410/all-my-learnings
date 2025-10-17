#!/usr/bin/env python3
"""
Script de verificación de ejercicios de Lógica y Programación.
Ejecuta tests y genera un archivo revision.md con los resultados.
"""

import sys
import os
from datetime import datetime

# Agregar el directorio de ejercicios al path
sys.path.insert(0, '/app/ejercicios')

def test_suma():
    """Tests para la función suma"""
    from suma import suma
    tests = [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (100, 200, 300),
    ]
    passed = 0
    total = len(tests)
    errors = []
    
    for a, b, expected in tests:
        try:
            result = suma(a, b)
            if result == expected:
                passed += 1
            else:
                errors.append(f"suma({a}, {b}) = {result}, esperado {expected}")
        except Exception as e:
            errors.append(f"suma({a}, {b}) generó error: {str(e)}")
    
    return passed, total, errors

def test_factorial():
    """Tests para la función factorial"""
    from factorial import factorial
    tests = [
        (0, 1),
        (1, 1),
        (5, 120),
        (6, 720),
        (10, 3628800),
    ]
    passed = 0
    total = len(tests)
    errors = []
    
    for n, expected in tests:
        try:
            result = factorial(n)
            if result == expected:
                passed += 1
            else:
                errors.append(f"factorial({n}) = {result}, esperado {expected}")
        except Exception as e:
            errors.append(f"factorial({n}) generó error: {str(e)}")
    
    return passed, total, errors

def test_ordenamiento():
    """Tests para la función ordenamiento"""
    from ordenamiento import ordenamiento
    tests = [
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([2, 2, 2], [2, 2, 2]),
    ]
    passed = 0
    total = len(tests)
    errors = []
    
    for lista, expected in tests:
        try:
            result = ordenamiento(lista)
            if result == expected:
                passed += 1
            else:
                errors.append(f"ordenamiento({lista}) = {result}, esperado {expected}")
        except Exception as e:
            errors.append(f"ordenamiento({lista}) generó error: {str(e)}")
    
    return passed, total, errors

def test_busqueda():
    """Tests para la función busqueda"""
    from busqueda import busqueda
    tests = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([], 1, -1),
    ]
    passed = 0
    total = len(tests)
    errors = []
    
    for lista, elemento, expected in tests:
        try:
            result = busqueda(lista, elemento)
            if result == expected:
                passed += 1
            else:
                errors.append(f"busqueda({lista}, {elemento}) = {result}, esperado {expected}")
        except Exception as e:
            errors.append(f"busqueda({lista}, {elemento}) generó error: {str(e)}")
    
    return passed, total, errors

def run_all_tests():
    """Ejecuta todos los tests y retorna los resultados"""
    results = {}
    
    print("\n🧪 Ejecutando tests de ejercicios...\n")
    
    # Test suma
    print("📝 Testing suma.py...")
    try:
        passed, total, errors = test_suma()
        results['suma'] = {'passed': passed, 'total': total, 'errors': errors}
        print(f"   ✓ {passed}/{total} tests pasaron")
    except Exception as e:
        results['suma'] = {'passed': 0, 'total': 5, 'errors': [f"Error al cargar módulo: {str(e)}"]}
        print(f"   ✗ Error: {str(e)}")
    
    # Test factorial
    print("📝 Testing factorial.py...")
    try:
        passed, total, errors = test_factorial()
        results['factorial'] = {'passed': passed, 'total': total, 'errors': errors}
        print(f"   ✓ {passed}/{total} tests pasaron")
    except Exception as e:
        results['factorial'] = {'passed': 0, 'total': 5, 'errors': [f"Error al cargar módulo: {str(e)}"]}
        print(f"   ✗ Error: {str(e)}")
    
    # Test ordenamiento
    print("📝 Testing ordenamiento.py...")
    try:
        passed, total, errors = test_ordenamiento()
        results['ordenamiento'] = {'passed': passed, 'total': total, 'errors': errors}
        print(f"   ✓ {passed}/{total} tests pasaron")
    except Exception as e:
        results['ordenamiento'] = {'passed': 0, 'total': 5, 'errors': [f"Error al cargar módulo: {str(e)}"]}
        print(f"   ✗ Error: {str(e)}")
    
    # Test busqueda
    print("📝 Testing busqueda.py...")
    try:
        passed, total, errors = test_busqueda()
        results['busqueda'] = {'passed': passed, 'total': total, 'errors': errors}
        print(f"   ✓ {passed}/{total} tests pasaron")
    except Exception as e:
        results['busqueda'] = {'passed': 0, 'total': 5, 'errors': [f"Error al cargar módulo: {str(e)}"]}
        print(f"   ✗ Error: {str(e)}")
    
    return results

def calculate_score(results):
    """Calcula el puntaje total"""
    total_passed = sum(r['passed'] for r in results.values())
    total_tests = sum(r['total'] for r in results.values())
    
    if total_tests == 0:
        return 0
    
    return (total_passed / total_tests) * 100

def generate_revision_md(results, score):
    """Genera el archivo revision.md con los resultados"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    md_content = f"""# Revisión de Ejercicios - Lógica y Programación

## 📊 Resumen de Calificación

**Fecha y Hora:** {timestamp}  
**Puntuación Total:** {score:.1f}%

## 📝 Resultados Detallados

"""
    
    for ejercicio, data in results.items():
        status = "✅" if data['passed'] == data['total'] else "⚠️"
        percentage = (data['passed'] / data['total'] * 100) if data['total'] > 0 else 0
        
        md_content += f"### {status} {ejercicio}.py\n\n"
        md_content += f"- **Tests pasados:** {data['passed']}/{data['total']}\n"
        md_content += f"- **Porcentaje:** {percentage:.1f}%\n\n"
        
        if data['errors']:
            md_content += "**Errores encontrados:**\n\n"
            for error in data['errors']:
                md_content += f"- {error}\n"
            md_content += "\n"
        else:
            md_content += "✨ ¡Todos los tests pasaron correctamente!\n\n"
    
    md_content += """## 🎯 Interpretación de Resultados

- **90-100%:** Excelente - Todos los ejercicios funcionan correctamente
- **70-89%:** Bueno - La mayoría de los ejercicios están correctos
- **50-69%:** Regular - Algunos ejercicios necesitan revisión
- **< 50%:** Necesita mejorar - Revisar la lógica de los ejercicios

## 📚 Próximos Pasos

1. Revisa los errores encontrados en cada ejercicio
2. Corrige el código en los archivos correspondientes
3. Ejecuta `make check` nuevamente para verificar las correcciones
4. Consulta el README.md para ejemplos y guías adicionales

---

*Generado automáticamente por el sistema de calificación*
"""
    
    # Escribir el archivo
    with open('/app/revision.md', 'w') as f:
        f.write(md_content)
    
    print(f"\n📄 Archivo revision.md generado exitosamente")
    print(f"📊 Puntuación total: {score:.1f}%\n")

def main():
    """Función principal"""
    print("=" * 60)
    print("  Sistema de Calificación - Lógica y Programación")
    print("=" * 60)
    
    # Ejecutar tests
    results = run_all_tests()
    
    # Calcular puntuación
    score = calculate_score(results)
    
    # Generar archivo de revisión
    generate_revision_md(results, score)
    
    # Resumen final
    print("=" * 60)
    total_passed = sum(r['passed'] for r in results.values())
    total_tests = sum(r['total'] for r in results.values())
    print(f"✅ Total: {total_passed}/{total_tests} tests pasaron")
    print(f"📊 Puntuación: {score:.1f}%")
    print("=" * 60)
    
    # Salir con código de error si no todos los tests pasaron
    if score < 100:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
