# Retroalimentación y Soluciones - Módulo 2: Fundamentos de IA

## Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: Diferencia entre programación tradicional y Machine Learning
**Respuesta correcta: B) En ML el sistema aprende patrones de datos, en programación tradicional el humano escribe reglas**

**Explicación**: Esta es la diferencia fundamental. En programación tradicional, el programador define explícitamente cada regla. En Machine Learning, el sistema encuentra patrones automáticamente a partir de datos de ejemplo.

---

### Pregunta 2: Tipo de aprendizaje del filtro de spam
**Respuesta correcta: C) Aprendizaje Supervisado**

**Explicación**: El filtro de spam usa aprendizaje supervisado porque aprende de emails que ya están etiquetados como "spam" o "no spam". Estas etiquetas son la "supervisión" que guía el aprendizaje.

---

### Pregunta 3: ¿Qué significa "overfitting"?
**Respuesta correcta: B) El modelo memoriza datos de entrenamiento pero falla con datos nuevos**

**Explicación**: Overfitting ocurre cuando el modelo se ajusta demasiado a los datos de entrenamiento, memorizando en lugar de aprender patrones generales. Es como estudiar solo las preguntas del examen del año pasado sin entender los conceptos.

---

### Pregunta 4: ¿Qué es una red neuronal?
**Respuesta correcta: C) Un sistema de nodos conectados inspirado en el cerebro humano**

**Explicación**: Las redes neuronales artificiales están inspiradas en cómo funcionan las neuronas en el cerebro, con nodos (neuronas artificiales) conectados que procesan y transmiten información.

---

### Pregunta 5: Afirmación correcta sobre datos en IA
**Respuesta correcta: B) La calidad de los datos es más importante que la cantidad**

**Explicación**: "Basura entra, basura sale". Tener millones de datos de mala calidad produce peores resultados que tener menos datos pero de alta calidad, bien etiquetados y representativos.

---

## Respuestas a Verdadero o Falso

1. **El aprendizaje supervisado requiere datos etiquetados.**  
   **VERDADERO** - La característica definitoria del aprendizaje supervisado es que necesita datos con etiquetas/respuestas correctas para aprender.

2. **Una red neuronal profunda (Deep Learning) siempre es mejor que una simple.**  
   **FALSO** - No siempre. Las redes profundas requieren más datos, son más costosas computacionalmente y pueden ser innecesarias para problemas simples. A veces un modelo más simple es mejor.

3. **El entrenamiento de un modelo es más costoso computacionalmente que la inferencia.**  
   **VERDADERO** - El entrenamiento puede tomar días o semanas en servidores potentes. La inferencia (uso) es mucho más rápida, a menudo en milisegundos.

4. **La IA actual puede razonar exactamente como los humanos.**  
   **FALSO** - La IA actual no razona como humanos. Encuentra patrones estadísticos en datos pero no tiene comprensión real, sentido común o razonamiento causal como nosotros.

5. **El aprendizaje por refuerzo aprende mediante recompensas y penalizaciones.**  
   **VERDADERO** - El aprendizaje por refuerzo se basa en el principio de recompensas (acciones buenas) y penalizaciones (acciones malas), similar a cómo aprenden los animales.

6. **Un modelo con 99% en entrenamiento pero 60% en datos nuevos probablemente tiene overfitting.**  
   **VERDADERO** - Esta gran diferencia es un síntoma clásico de overfitting. El modelo memorizó los datos de entrenamiento pero no generalizó bien.

7. **Los sesgos en datos de entrenamiento pueden resultar en IA sesgada.**  
   **VERDADERO** - Los sesgos en los datos se transfieren directamente al modelo. Si entrenas con datos sesgados, obtendrás predicciones sesgadas.

8. **La inferencia es la fase donde el modelo aprende.**  
   **FALSO** - La inferencia es la fase de USO del modelo, no de aprendizaje. El aprendizaje ocurre durante el entrenamiento.

---

## Respuestas a Clasificación de Tipos de Aprendizaje

### Aplicación 1: Sistema de Recomendación de Amazon
**Tipo**: Aprendizaje No Supervisado  
**Justificación**: Agrupa productos similares sin categorías predefinidas. El sistema encuentra patrones naturales de similitud.

### Aplicación 2: Reconocimiento de Imágenes Médicas
**Tipo**: Aprendizaje Supervisado  
**Justificación**: Usa imágenes etiquetadas por expertos médicos. El modelo aprende de estos ejemplos etiquetados.

### Aplicación 3: Robot que Aprende a Caminar
**Tipo**: Aprendizaje por Refuerzo  
**Justificación**: Aprende por prueba y error. Recompensa (mantener equilibrio) vs penalización (caerse).

### Aplicación 4: Segmentación de Clientes
**Tipo**: Aprendizaje No Supervisado  
**Justificación**: Encuentra grupos naturales sin categorías predefinidas. Clustering basado en comportamiento.

---

## Respuestas al Ciclo del Machine Learning

**Orden correcto:**

1. Recolección de datos
2. Preparación y limpieza de datos
3. Entrenamiento del modelo
4. Evaluación del modelo
5. Predicción/Uso del modelo

**Explicación**: Primero necesitas datos, luego los preparas, entrenas el modelo, lo evalúas para asegurarte que funciona bien, y finalmente lo usas para hacer predicciones.

---

## Retroalimentación de Diseño de Dataset

### Dataset para Predicción de Aprobación de Examen

**Datos de entrada sugeridos:**
1. Horas de estudio
2. Asistencia a clases (%)
3. Calificaciones previas
4. Tareas completadas
5. Participación en clase
6. Horas de sueño
7. Tiempo desde último examen

**Etiqueta**: "Aprobado" / "Reprobado" (Clasificación binaria)

**Cantidad mínima**: Al menos 500-1000 estudiantes para tener datos representativos

**Sesgos a evitar:**
- Solo estudiantes de un programa
- Solo un tipo de examen
- Datos de un solo semestre
- Desbalance (90% aprobados, 10% reprobados)

**Características más importantes**: Probablemente horas de estudio, calificaciones previas y asistencia tienen mayor peso predictivo.

---

## Soluciones a Detección de Problemas

### Caso 1: Reconocimiento Facial

1. **Problema**: Sesgo etario - el modelo no funciona bien con personas mayores
   
2. **Causa**: Los datos de entrenamiento solo incluyen personas jóvenes (20-30 años). El modelo nunca aprendió cómo se ven las personas mayores.

3. **Solución**:
   - Incluir datos balanceados de todos los rangos de edad
   - Recolectar al menos 2,000-3,000 fotos de personas mayores de 60
   - Re-entrenar el modelo con el dataset expandido

### Caso 2: Predictor de Precios de Casas

1. **Problema**: Overfitting clásico

2. **Causa**: Muy pocas muestras (1,000) para tantas variables (50). El modelo memorizó los datos en lugar de aprender patrones.

3. **Soluciones**:
   - Reducir número de características (usar solo las más relevantes)
   - Conseguir más datos (al menos 5,000-10,000 casas)
   - Usar técnicas de regularización
   - Simplificar el modelo
   - Usar validación cruzada

---

## Entrenamiento vs Inferencia - Tabla Completa

| Aspecto | Entrenamiento | Inferencia |
|---------|--------------|-----------|
| **Cuándo ocurre** | Una vez o periódicamente | Continuamente en uso |
| **Velocidad** | Lento (horas/días/semanas) | Rápido (milisegundos) |
| **Requiere datos** | Miles/millones de ejemplos | Solo el input actual |
| **Costo computacional** | Muy alto (GPUs potentes) | Bajo (puede correr en móvil) |
| **Frecuencia** | Ocasional | Constante |

---

## Redes Neuronales - Reconocimiento de Dígitos

### Estructura:

**Capa de Entrada**: Píxeles de la imagen (ej: 28x28 = 784 píxeles)

**Capas Ocultas**:
- Capa 1: Detecta bordes y líneas básicas
- Capa 2: Combina líneas para formar curvas y formas
- Capa 3: Reconoce patrones específicos de cada número

**Capa de Salida**: 10 neuronas (una por cada dígito 0-9), cada una con probabilidad

### Ejemplo de reconocer un "8":
La red detecta dos círculos apilados (capa 1 detecta curvas, capa 2 detecta círculos, capa 3 reconoce que dos círculos verticales = "8").

---

## Evaluación de Calidad de Datos

### Dataset 1: Predictor de Clima
**Evaluación**: ❌ Problemático  
**Razón**: Muy pocos datos (100), solo un mes, una ciudad, una hora del día. No representativo ni generalizable. Necesita años de datos, múltiples ciudades, diferentes horas.

### Dataset 2: Clasificador de Sentimientos
**Evaluación**: ✅ Adecuado  
**Razón**: Gran cantidad (50,000), balanceado, diverso (diferentes regiones), etiquetado por humanos. Cumple los requisitos de calidad.

### Dataset 3: Detector de Enfermedades
**Evaluación**: ❌ Problemático  
**Razón**: Muy desbalanceado (95% vs 5%), solo un hospital. Necesita más casos positivos y datos de múltiples hospitales para generalizar.

---

## Caso de Estudio: Recomendación de Películas

### Respuestas sugeridas:

1. **Tipo de aprendizaje**: Combinación de Supervisado (predicción de calificaciones) y No Supervisado (encontrar películas similares)

2. **Características relevantes**:
   - Historial de visualización
   - Calificaciones previas
   - Género de películas vistas
   - Similitud con otros usuarios
   - Tendencias temporales

3. **Desafíos**:
   - "Cold start": Nuevos usuarios sin historial
   - Nuevas películas sin calificaciones
   - Sesgos de popularidad
   - Diversidad vs precisión (no recomendar solo lo mismo)

4. **Métricas de éxito**:
   - Precisión de predicción de calificaciones
   - Click-through rate (% de recomendaciones vistas)
   - Tiempo de visualización
   - Satisfacción del usuario (encuestas)

5. **Sesgos posibles**:
   - Favorecer contenido popular sobre nicho
   - Sesgo demográfico (edad, ubicación)
   - "Filter bubble" (solo mostrar lo similar)

---

## Limitaciones Reales de la IA

**Limitaciones correctas:**
- ✅ No tiene sentido común como humanos
- ✅ Necesita muchos datos para aprender
- ✅ No puede explicar todas sus decisiones (caja negra)
- ✅ No puede razonar fuera de sus datos de entrenamiento

**NO son limitaciones:**
- ❌ Puede procesar grandes cantidades de datos (es una fortaleza)
- ❌ Puede aprender de ejemplos (es su función principal)
- ❌ Puede crear contenido original (IA generativa lo hace)
- ❌ Puede superar a humanos en tareas específicas (ajedrez, Go, etc.)

### Ejemplos de limitaciones:

**Falta de sentido común**: ChatGPT puede escribir perfectamente pero no sabe que no puedes meter un elefante en un refrigerador.

**Necesidad de datos**: Un niño aprende qué es un gato viendo 1-2 ejemplos. Una IA necesita miles.

**Caja negra**: Un modelo de deep learning puede detectar cáncer pero no siempre puede explicar exactamente por qué marcó una imagen como sospechosa.

---

## Evaluación de Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Tienes comprensión sólida de los fundamentos técnicos de IA. Estás listo para técnicas avanzadas de prompting.

**Próximos pasos:**
- Continúa con Módulo 3
- Experimenta diseñando datasets simples
- Explora herramientas de ML sin código (AutoML)

---

### Si acertaste 70-89%: 💪 ¡Muy bien!
Comprendes los conceptos principales. Algunas áreas técnicas pueden beneficiarse de repaso.

**Recomendaciones:**
- Repasa tipos de aprendizaje
- Practica identificar overfitting/underfitting
- Revisa la importancia de datos de calidad

---

### Si acertaste menos de 70%: 📚 Continúa aprendiendo
Los conceptos técnicos pueden ser desafiantes. ¡Es normal!

**Recomendaciones:**
- Enfócate en un tipo de aprendizaje a la vez
- Usa analogías del mundo real
- Experimenta con herramientas visuales (ML Playground)
- Re-lee secciones específicas donde tengas dudas

---

## Recursos Adicionales

**Videos:**
- "Machine Learning for Everybody" - Kylie Ying
- "Neural Networks Explained" - 3Blue1Brown
- "Overfitting y Underfitting" - StatQuest

**Herramientas Interactivas:**
- TensorFlow Playground
- Google's Teachable Machine
- ML Crash Course de Google

**Artículos:**
- "A Visual Introduction to Machine Learning"
- "Supervised vs Unsupervised Learning"

---

**¡Felicidades por completar el Módulo 2! Ahora entiendes la ciencia detrás de la IA. 🧠**

**Siguiente paso**: Módulo 3 - El Arte del Prompting (donde aprenderás a comunicarte efectivamente con IA)
