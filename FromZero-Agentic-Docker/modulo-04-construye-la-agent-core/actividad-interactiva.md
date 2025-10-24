# Módulo 04: Actividad Interactiva

## Ejercicio 1: Ejecuta el Agent Core (10 min)

```bash
cd modulo-04-construye-la-agent-core/ejemplos
python agent.py
```

**Output observado**: _______________
**Herramientas disponibles**: _______________

## Ejercicio 2: Añade una Nueva Tool (15 min)

Modifica `agent.py` para añadir una calculadora:

```python
def calculator_tool(analysis):
    # Implementar calculadora simple
    return {"result": 42}

agent.add_tool(Tool(
    name="calculator",
    description="Perform calculations",
    function=calculator_tool
))
```

**Tool añadida**: [ ] Sí
**Funciona correctamente**: [ ] Sí

## Ejercicio 3: Prueba Diferentes Queries (10 min)

Prueba estas queries:
- "What's the weather?"
- "What time is it?"
- "Calculate 5 + 5"

**Resultados**: _______________

## Total: 35 minutos
