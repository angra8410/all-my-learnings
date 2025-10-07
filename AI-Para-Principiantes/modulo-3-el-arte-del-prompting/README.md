# Módulo 3: El Arte del Prompting

## Introducción

El prompting es la habilidad de comunicarte efectivamente con IA. En este módulo aprenderás:

- Qué es un prompt y por qué importa
- Anatomía de un buen prompt
- Técnicas de prompting avanzadas
- Patrones y frameworks efectivos
- Errores comunes y cómo evitarlos
- Práctica con ejemplos reales

## ¿Por qué es importante?

La misma IA puede dar resultados completamente diferentes según cómo le preguntes:

**Prompt básico**: "Escribe sobre marketing"  
**Resultado**: Respuesta genérica y amplia

**Prompt avanzado**: "Explica 3 estrategias de marketing digital para pequeños negocios locales, con ejemplos prácticos y presupuesto limitado"  
**Resultado**: Respuesta específica, accionable y relevante

**El prompting efectivo multiplica el valor que obtienes de la IA.**

## Conceptos Principales

### 1. Anatomía de un Buen Prompt

**Componentes clave:**

```
CONTEXTO + TAREA + FORMATO + TONO + RESTRICCIONES = PROMPT EFECTIVO
```

**Ejemplo desglosado:**

```
CONTEXTO: "Soy profesor de secundaria de historia"
TAREA: "Crea un cuestionario sobre la Revolución Francesa"
FORMATO: "10 preguntas de opción múltiple"
TONO: "Lenguaje apropiado para estudiantes de 15 años"
RESTRICCIONES: "Enfócate en causas y consecuencias, no en fechas"

PROMPT COMPLETO:
"Soy profesor de secundaria de historia. Crea un cuestionario de 10 
preguntas de opción múltiple sobre la Revolución Francesa, con lenguaje 
apropiado para estudiantes de 15 años. Enfócate en causas y consecuencias, 
no en memorización de fechas."
```

### 2. Principio de Especificidad

**Regla de Oro**: Más específico = Mejor resultado

❌ **Mal prompt**: "Dame ideas"  
✅ **Buen prompt**: "Dame 5 ideas de contenido para Instagram sobre recetas saludables veganas, dirigidas a adultos jóvenes interesados en fitness"

**Comparación:**

| Vago | Específico |
|------|-----------|
| "Ayúdame con mi CV" | "Revisa mi CV de ingeniero de software con 3 años de experiencia y sugiere mejoras para aplicar a posiciones senior en startups tech" |
| "Escribe un email" | "Escribe un email profesional pero amigable solicitando una reunión de 30 minutos con un cliente potencial que mostró interés en nuestro producto de CRM" |
| "Explica Python" | "Explica el concepto de listas en Python a alguien que nunca ha programado, usando analogías de la vida cotidiana y 3 ejemplos simples" |

### 3. Técnicas de Prompting Avanzadas

#### A. Role Playing (Adoptar un Rol)
Le pides a la IA que actúe como un experto específico.

```
"Actúa como un nutricionista certificado con 10 años de experiencia. 
Crea un plan de comidas de 7 días para alguien con intolerancia 
a la lactosa que quiere ganar masa muscular."
```

#### B. Few-Shot Learning (Ejemplos)
Le muestras ejemplos de lo que quieres.

```
"Convierte estas oraciones a tono profesional:

Ejemplo 1:
Informal: 'Oye, ¿cuándo nos vemos?'
Profesional: '¿Podríamos coordinar una reunión?'

Ejemplo 2:
Informal: 'Me gusta tu idea'
Profesional: 'Considero que su propuesta tiene mérito'

Ahora convierte:
Informal: 'No me parece bien esto'
Profesional: [tu respuesta]"
```

#### C. Chain of Thought (Cadena de Pensamiento)
Pides que explique el razonamiento paso a paso.

```
"Resuelve este problema mostrando tu razonamiento paso a paso:
Si un producto cuesta $80 con 20% de descuento, ¿cuál era el precio original?"
```

#### D. Iteración y Refinamiento
Mejoras el resultado en múltiples pasos.

```
1º prompt: "Escribe un eslogan para cafetería"
Resultado: "Café que despierta tus sentidos"

2º prompt: "Hazlo más corto y memorable"
Resultado: "Despierta con sabor"

3º prompt: "Agrega un juego de palabras con 'café'"
Resultado: "Café-lidad que despierta"
```

### 4. Frameworks de Prompting

#### Framework RACE

- **R**ol: Define quién es la IA
- **A**cción: Qué debe hacer
- **C**ontexto: Información relevante
- **E**xpectativa: Formato/tono deseado

**Ejemplo:**
```
Rol: Actúa como consultor de pequeños negocios
Acción: Crea un plan de marketing
Contexto: Para una pastelería local que acaba de abrir
Expectativa: Formato de lista con acciones concretas y bajo presupuesto
```

#### Framework CREATE

- **C**ontexto: Situación actual
- **R**equisitos: Qué necesitas específicamente
- **E**jemplos: Muestra lo que quieres
- **A**djustments: Restricciones o preferencias
- **T**ype: Formato de salida
- **E**xtra: Detalles adicionales

### 5. Tipos de Prompts Según el Objetivo

#### Informativo/Educativo
```
"Explícame [tema] como si tuviera [nivel de conocimiento]"
"¿Cuáles son las diferencias clave entre [A] y [B]?"
"Resume [concepto] en 3 puntos principales"
```

#### Creativo/Generativo
```
"Genera [cantidad] ideas de [tema] que sean [características]"
"Escribe [tipo de contenido] sobre [tema] en estilo [autor/tono]"
"Crea una historia de [género] que incluya [elementos]"
```

#### Analítico/Evaluativo
```
"Analiza [texto/situación] y identifica [qué buscar]"
"Compara [opción A] vs [opción B] considerando [criterios]"
"Evalúa [propuesta] en términos de [métricas]"
```

#### Práctico/Accionable
```
"Crea un plan paso a paso para [objetivo]"
"Dame una lista de verificación para [tarea]"
"Sugiere [cantidad] acciones concretas para [problema]"
```

### 6. Errores Comunes en Prompting

❌ **Ser demasiado vago**
- Malo: "Háblame de negocios"
- Bueno: "Explica 3 modelos de negocio digitales exitosos en 2024"

❌ **Asumir que la IA sabe tu contexto**
- Malo: "Mejora esto" (¿qué es 'esto'?)
- Bueno: "Mejora este párrafo haciéndolo más conciso: [texto]"

❌ **No especificar formato**
- Malo: "Dame información sobre SEO"
- Bueno: "Crea una tabla comparativa de 5 técnicas de SEO: nombre, dificultad, impacto, tiempo de implementación"

❌ **Prompts excesivamente largos**
- Malo: 5 párrafos de contexto antes de la pregunta
- Bueno: Contexto conciso + pregunta clara

❌ **No iterar**
- Malo: Aceptar la primera respuesta si no es perfecta
- Bueno: "Acorta esto a 50 palabras" → "Ahora hazlo más formal"

### 7. Optimización de Prompts

**Antes de Optimizar:**
```
"Escribe sobre inteligencia artificial"
```

**Después de Optimizar:**
```
"Escribe un artículo de 500 palabras sobre aplicaciones prácticas de IA en 
educación, dirigido a profesores de primaria sin conocimientos técnicos. 
Incluye 3 ejemplos concretos de herramientas que pueden usar mañana mismo, 
con enlaces y pasos de implementación. Usa lenguaje sencillo y tono 
motivacional."
```

**Mejoras aplicadas:**
- ✅ Longitud específica (500 palabras)
- ✅ Tema delimitado (IA en educación)
- ✅ Audiencia clara (profesores primaria)
- ✅ Nivel técnico (sin jerga)
- ✅ Formato (3 ejemplos + pasos)
- ✅ Tono (motivacional)
- ✅ Accionable (pueden usar mañana)

## Implementación Práctica

### Ejercicio 1: Mejora estos Prompts

**Prompt vago**: "Ayúdame con mi negocio"

**Tu versión mejorada**:
_______________________________________________
_______________________________________________

---

**Prompt vago**: "Escribe código"

**Tu versión mejorada**:
_______________________________________________
_______________________________________________

---

**Prompt vago**: "Dame ideas de contenido"

**Tu versión mejorada**:
_______________________________________________
_______________________________________________

### Ejercicio 2: Usa el Framework RACE

**Escenario**: Necesitas un plan de estudio para aprender diseño gráfico

**R**ol: _______________________________________________  
**A**cción: _______________________________________________  
**C**ontexto: _______________________________________________  
**E**xpectativa: _______________________________________________

**Prompt completo**:
_______________________________________________
_______________________________________________

### Ejercicio 3: Role Playing

Crea 3 prompts usando diferentes roles:

**1. Como chef profesional**:
_______________________________________________

**2. Como coach personal**:
_______________________________________________

**3. Como analista financiero**:
_______________________________________________

## Mejores Prácticas

### 1. Sé Claro y Específico
- ✅ Define exactamente qué quieres
- ✅ Incluye detalles relevantes
- ✅ Especifica formato y tono

### 2. Proporciona Contexto
- ✅ Quién eres/tu situación
- ✅ Para qué lo necesitas
- ✅ Quién es la audiencia

### 3. Usa Ejemplos
- ✅ Muestra lo que quieres
- ✅ Formato deseado
- ✅ Estilo preferido

### 4. Itera y Refina
- ✅ Primera respuesta = punto de partida
- ✅ Pide ajustes específicos
- ✅ Conversa con la IA

### 5. Experimenta
- ✅ Prueba diferentes enfoques
- ✅ Guarda prompts que funcionan
- ✅ Aprende de cada interacción

## Conceptos Clave para Recordar

- 🎯 **Especificidad**: Más detalles = Mejores resultados
- 👤 **Role Playing**: Pide a la IA adoptar un rol experto
- 📝 **Few-Shot**: Muestra ejemplos de lo que quieres
- 🔗 **Chain of Thought**: Pide razonamiento paso a paso
- 🔄 **Iteración**: Refina la respuesta en múltiples pasos
- 📋 **Framework RACE**: Rol + Acción + Contexto + Expectativa
- ⚠️ **Evita vaguedad**: "Ayúdame" → "Ayúdame a [tarea específica]"
- 🎨 **Formato importa**: Especifica tabla, lista, párrafo, etc.

## Próximos Pasos

En el Módulo 4 explorarás:
- Herramientas populares de IA (ChatGPT, Claude, Midjourney, etc.)
- Casos de uso específicos de cada herramienta
- Cuándo usar qué herramienta
- Comparativa de capacidades
- Trucos y tips específicos por plataforma

**¿Estás listo para continuar?**
✅ Entiendes los componentes de un buen prompt  
✅ Conoces técnicas avanzadas de prompting  
✅ Puedes optimizar prompts vagos  
✅ Has practicado con frameworks  

## Motivación Final

> "La calidad de tus preguntas determina la calidad de tus respuestas." - Anónimo

**Recuerda:**
- 💬 El prompting es una habilidad que se desarrolla con práctica
- 🎓 Cada interacción con IA es una oportunidad de aprender
- 📚 Guarda tus mejores prompts como biblioteca personal
- 🚀 Buenos prompts = 10x mejor productividad con IA

**¡Ahora puedes comunicarte efectivamente con cualquier IA! 💪**

---

**Recursos Adicionales:**
- 📚 "Prompt Engineering Guide" (GitHub)
- 🎓 "ChatGPT Prompt Engineering" (Coursera)
- 🔗 PromptBase.com (biblioteca de prompts)
- 📖 Awesome ChatGPT Prompts

**Tiempo estimado**: 2-3 horas  
**Dificultad**: Intermedio ⭐⭐☆☆☆
