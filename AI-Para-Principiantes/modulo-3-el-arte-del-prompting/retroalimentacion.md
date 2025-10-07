# Retroalimentación y Soluciones - Módulo 3: El Arte del Prompting

## Ejemplos de Prompts Mejorados

### Prompt 1: Marketing
**Vago**: "Escríbeme algo sobre marketing"

**Mejorado**: "Actúa como consultor de marketing digital. Crea una guía de 5 estrategias de marketing en redes sociales para pequeños negocios locales con presupuesto limitado (<$500/mes). Incluye para cada estrategia: descripción, pasos de implementación, costo estimado y métricas de éxito. Usa lenguaje simple y ejemplos concretos."

**Elementos agregados**:
- Rol (consultor de marketing digital)
- Especificidad (5 estrategias, redes sociales, pequeños negocios)
- Restricción (presupuesto <$500)
- Formato (estructura definida para cada estrategia)
- Audiencia (pequeños negocios)
- Tono (lenguaje simple)

---

### Prompt 2: CV
**Vago**: "Ayúdame con mi CV"

**Mejorado**: "Soy diseñador gráfico con 3 años de experiencia aplicando a posiciones senior en agencias creativas. Revisa mi CV y sugiere mejoras específicas en: (1) resumen profesional, (2) descripción de proyectos destacados, (3) habilidades técnicas relevantes. Enfócate en resultados medibles y lenguaje orientado a logros."

**Elementos agregados**:
- Contexto personal (diseñador, 3 años)
- Objetivo (posición senior, agencias)
- Áreas específicas de mejora
- Criterio (resultados medibles)

---

### Prompt 3: Ideas
**Vago**: "Dame ideas"

**Mejorado**: "Genera 10 ideas de contenido para canal de YouTube sobre cocina vegana saludable, dirigido a adultos jóvenes (25-35 años) principiantes en cocina. Cada idea debe incluir: título atractivo, concepto en 1 frase, y por qué sería popular. Enfócate en recetas rápidas (<30 min) y accesibles."

**Elementos agregados**:
- Cantidad (10 ideas)
- Plataforma (YouTube)
- Tema específico (cocina vegana saludable)
- Audiencia (adultos jóvenes principiantes)
- Formato (título + concepto + razón)
- Restricción (recetas <30 min)

---

## Framework RACE - Soluciones

### Escenario 1: Plan de Ejercicio

**R**ol: Entrenador personal certificado con especialización en fitness para principiantes  
**A**cción: Crea un plan de ejercicio de 4 semanas  
**C**ontexto: Para persona sedentaria de 30 años que quiere empezar a hacer ejercicio, sin equipo, 30 min por día  
**E**xpectativa: Formato de tabla semanal con ejercicios, series, repeticiones y videos de referencia

**Prompt completo**:
"Actúa como entrenador personal certificado con especialización en principiantes. Crea un plan de ejercicio de 4 semanas para una persona sedentaria de 30 años que quiere empezar a hacer ejercicio en casa, sin equipo, 30 minutos por día. Presenta en formato de tabla semanal con: ejercicio, series, repeticiones, y enlaces a videos demostrativos. Progresión gradual de intensidad."

---

### Escenario 2: Estrategia de Redes Sociales

**R**ol: Especialista en redes sociales con experiencia en crecimiento orgánico  
**A**cción: Diseña estrategia de contenido para Instagram  
**C**ontexto: Marca personal de coach de productividad, audiencia objetivo: profesionales 25-40 años  
**E**xpectativa: Plan de 30 días con tipos de contenido, frecuencia, hashtags y horarios

**Prompt completo**:
"Actúa como especialista en redes sociales con expertise en crecimiento orgánico de Instagram. Diseña una estrategia de contenido de 30 días para una marca personal de coach de productividad, dirigida a profesionales de 25-40 años. Incluye: tipos de contenido (Reels, carruseles, historias), frecuencia de publicación, hashtags relevantes, mejores horarios y ideas específicas de posts."

---

## Role Playing - Ejemplos

1. **Como nutricionista**: "Actúa como nutricionista certificada. Crea un plan de comidas de 7 días para vegetariano que entrena 4 veces por semana, busca ganar masa muscular. Incluye macros aproximados y opciones de snacks."

2. **Como desarrollador senior**: "Actúa como desarrollador senior de Python con 10 años de experiencia. Revisa este código [código] y sugiere mejoras en términos de eficiencia, legibilidad y mejores prácticas. Explica cada sugerencia."

3. **Como diseñador UX**: "Actúa como diseñador UX senior. Analiza el flujo de registro de esta app [descripción] e identifica 3 puntos de fricción potenciales con soluciones concretas para mejorar la experiencia."

4. **Como coach de negocios**: "Actúa como coach de negocios especializado en emprendimientos digitales. Ayúdame a validar esta idea de negocio [idea] mediante 5 preguntas críticas que debo responder antes de invertir tiempo y dinero."

5. **Como profesor de matemáticas**: "Actúa como profesor de matemáticas de secundaria. Explica el teorema de Pitágoras usando 3 analogías de la vida real y crea 3 problemas prácticos con diferentes niveles de dificultad."

---

## Few-Shot Learning - Solución

**Clickbait**: "TODOS están usando esto y TÚ NO"  
**Profesional**: "Herramienta emergente en adopción empresarial"

O también válido:
- "Tendencia actual en el sector profesional"
- "Nueva práctica estándar en la industria"
- "Tecnología de rápida adopción en el mercado"

---

## Chain of Thought - Ejemplos

**Problema 1: Presupuesto**
"Quiero crear un presupuesto mensual con ingresos de $2,500. Guíame paso a paso:
1. Primero, identifica categorías esenciales vs opcionales
2. Luego, sugiere porcentajes para cada categoría
3. Después, muestra un ejemplo numérico concreto
4. Finalmente, dame tips para mantenerme dentro del presupuesto
Explica tu razonamiento en cada paso."

**Problema 2: Decisión de Carrera**
"Estoy decidiendo entre dos ofertas de trabajo [detalles]. Ayúdame a analizar mostrando tu proceso de pensamiento:
1. ¿Qué factores debería considerar y por qué?
2. ¿Cómo ponderarías cada factor en importancia?
3. ¿Qué preguntas debería hacerme sobre cada opción?
4. ¿Cuál recomendarías basándote en el análisis y por qué?
Muestra tu razonamiento completo."

---

## Calificación de Especificidad

1. "Escribe un artículo" - **Calificación: 1/5** (extremadamente vago)
2. "Escribe un artículo de 800 palabras sobre IA en medicina" - **Calificación: 3/5** (mejor pero falta audiencia, formato, tono)
3. "Escribe" - **Calificación: 0/5** (completamente vago)
4. "Escribe un artículo de 800 palabras sobre IA en diagnóstico médico, dirigido a doctores, con 3 casos de estudio y referencias" - **Calificación: 5/5** (excelente: longitud, tema, audiencia, estructura, evidencia)

---

## Evaluación de Desempeño

### Si completaste 90% o más: 🌟 ¡Excelente!
Dominas el arte del prompting. Puedes obtener resultados de alta calidad de cualquier IA.

**Próximos pasos:**
- Crea tu biblioteca personal de prompts
- Experimenta con técnicas avanzadas
- Comparte tus mejores prompts con otros

---

### Si completaste 70-89%: 💪 ¡Muy bien!
Comprendes los principios fundamentales del prompting efectivo.

**Recomendaciones:**
- Practica más con role playing
- Experimenta con iteración
- Usa frameworks consistentemente

---

### Si completaste menos de 70%: 📚 Sigue practicando
El prompting es una habilidad que mejora con práctica.

**Recomendaciones:**
- Empieza con el framework RACE
- Compara prompts vagos vs específicos
- Practica diariamente con casos reales

---

## Checklist de Maestría en Prompting

Antes de avanzar, confirma que puedes:

- [ ] Identificar elementos de un prompt efectivo
- [ ] Transformar prompts vagos en específicos
- [ ] Aplicar framework RACE
- [ ] Usar role playing apropiadamente
- [ ] Implementar few-shot learning
- [ ] Pedir razonamiento con chain of thought
- [ ] Iterar y refinar respuestas
- [ ] Especificar formato y tono
- [ ] Crear prompts para diferentes objetivos

---

**¡Felicidades! Ahora puedes obtener el máximo valor de cualquier IA. 🎯**

Módulo siguiente: Herramientas Populares de IA
