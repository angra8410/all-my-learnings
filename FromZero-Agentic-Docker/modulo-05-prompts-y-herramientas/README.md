# Módulo 05: Prompts y Herramientas

## 🎯 Objetivos

- ✅ Diseñar prompts efectivos para agentes
- ✅ Implementar herramientas (tools) avanzadas
- ✅ Integrar tools con el agent core
- ✅ Probar weather tool y otras herramientas

## 📖 Prompts Efectivos

Un buen prompt para agentes debe:

1. **Ser claro y específico**
2. **Incluir contexto**
3. **Definir el rol del agente**
4. **Especificar el formato de salida**

### Ejemplo de System Prompt

```
You are a helpful weather assistant.
Your role is to provide accurate weather information.
Always respond in JSON format.
Be concise and friendly.
```

## 🔧 Herramientas Disponibles

Revisa `ejemplos/weather_tool.py` que incluye:

- **WeatherTool** - Información meteorológica
- **TimeTool** - Fecha y hora
- **CalculatorTool** - Cálculos matemáticos

## 🧪 Prueba las Herramientas

```bash
cd modulo-05-prompts-y-herramientas/ejemplos
python weather_tool.py
```

## ✅ Checklist

- [ ] Entiendo diseño de prompts
- [ ] He probado weather_tool.py
- [ ] Comprendo estructura de tools
- [ ] Puedo crear nuevas tools
- [ ] He integrado tools con agent

## 🎯 Próximos Pasos

Continúa al **Módulo 06: Contenedoriza la App**
