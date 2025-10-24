# Módulo 01: Actividad Interactiva

## 🎯 Objetivo

Familiarizarte con los conceptos básicos y prepararte mentalmente para el curso mediante ejercicios cortos y prácticos.

---

## 📝 Ejercicio 1: Explora tu Sistema (5 minutos)

**Objetivo**: Verificar que tienes acceso a la terminal y familiarizarte con comandos básicos.

### Pasos:

1. Abre tu terminal (CMD, PowerShell, Terminal, bash)
2. Ejecuta los siguientes comandos y anota los resultados:

```bash
# Minuto fluido 1: ¿Dónde estoy?
pwd
```

**Resultado esperado**: Tu directorio actual
**Tu resultado**: _______________

```bash
# Minuto fluido 2: ¿Qué hay aquí?
ls
# En Windows: dir
```

**Resultado esperado**: Lista de archivos y carpetas
**Tu resultado**: _______________

```bash
# Minuto fluido 3: ¿Qué sistema operativo?
uname -a
# En Windows: systeminfo | findstr /B /C:"OS"
```

**Resultado esperado**: Información del sistema
**Tu resultado**: _______________

**Duración**: 1 minuto x 3 repeticiones = 3 minutos

---

## 🐍 Ejercicio 2: Verifica Python (4 minutos)

**Objetivo**: Asegurar que Python está instalado y funcionando.

### Pasos:

```bash
# Minuto fluido 1: Versión de Python
python --version
# o en algunos sistemas:
python3 --version
```

**Tu resultado**: _______________

```bash
# Minuto fluido 2: Versión de pip
pip --version
# o:
pip3 --version
```

**Tu resultado**: _______________

```bash
# Minuto fluido 3: Ejecuta Python interactivo
python
# Dentro de Python:
>>> print("Hello, Agentic World!")
>>> 2 + 2
>>> exit()
```

**Tu resultado**: _______________

**Duración**: 1 minuto x 3 comandos = 3 minutos

---

## 🐳 Ejercicio 3: Verifica Docker (si está instalado) (3 minutos)

**Objetivo**: Comprobar si Docker ya está instalado.

### Pasos:

```bash
# Minuto fluido 1: ¿Está Docker instalado?
docker --version
```

**Tu resultado**: 
- [ ] Docker está instalado - Versión: _______________
- [ ] Docker NO está instalado (lo instalarás en el Módulo 02)

```bash
# Minuto fluido 2: ¿Está corriendo Docker?
docker ps
```

**Tu resultado**:
- [ ] Docker está corriendo (lista vacía o con contenedores)
- [ ] Error (Docker no está corriendo o no instalado)

```bash
# Minuto fluido 3: Imágenes disponibles
docker images
```

**Tu resultado**: _______________

**Duración**: 1 minuto x 3 comandos = 3 minutos

**Nota**: Si Docker no está instalado, no te preocupes. Lo instalarás en el próximo módulo.

---

## 💭 Ejercicio 4: Reflexión y Objetivos (10 minutos)

**Objetivo**: Establecer tus motivaciones y objetivos personales.

### Pregunta 1: ¿Por qué agentes con IA?

Escribe 3 razones por las que te interesa este tema:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Pregunta 2: ¿Qué quieres construir?

Describe brevemente un agente que te gustaría crear después del curso:

**Mi idea de agente**:
_______________________________________________
_______________________________________________
_______________________________________________

**Ejemplo**: "Un agente que lea mis correos, identifique los urgentes y prepare borradores de respuesta"

### Pregunta 3: Compromiso de tiempo

¿Cuánto tiempo puedes dedicar al curso?

- [ ] 2-3 horas por semana (ritmo relajado - 8 semanas)
- [ ] 4-6 horas por semana (ritmo moderado - 4 semanas)
- [ ] 8-10 horas por semana (ritmo intensivo - 2 semanas)

**Mi compromiso**: _____ horas por semana

---

## 🔍 Ejercicio 5: Investiga un Agente Real (8 minutos)

**Objetivo**: Entender cómo funcionan los agentes existentes.

### Tarea:

Elige uno de estos agentes y explora su documentación por 5 minutos:

- [ ] ChatGPT (chat.openai.com)
- [ ] GitHub Copilot (github.com/features/copilot)
- [ ] Claude (claude.ai)
- [ ] Otro: _______________

### Preguntas a responder:

1. **¿Qué hace este agente?**
   _______________________________________________

2. **¿Qué "herramientas" o capacidades tiene?**
   _______________________________________________

3. **¿Cómo interactúas con él?** (chat, API, extensión, etc.)
   _______________________________________________

4. **¿Qué te gustaría que hiciera de forma diferente?**
   _______________________________________________

**Duración**: 5 minutos exploración + 3 minutos respuestas = 8 minutos

---

## 📊 Ejercicio 6: Diagrama tu Agente Ideal (7 minutos)

**Objetivo**: Visualizar cómo quieres que funcione tu agente.

### Tarea:

Dibuja (en papel o digitalmente) un diagrama simple de tu agente ideal:

```
Ejemplo:

Usuario
   ↓
[Interfaz: Chat/API]
   ↓
[Agent Core: Razonamiento]
   ↓
[Tools: Weather, News, Email]
   ↓
Acciones / Respuestas
```

**Tu diagrama**:

```
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

**Componentes a incluir**:
- [ ] Forma de entrada (cómo el usuario interactúa)
- [ ] Agent core (el cerebro)
- [ ] Tools/Herramientas (qué puede hacer)
- [ ] Salida (qué devuelve al usuario)

**Duración**: 7 minutos

---

## 🎯 Ejercicio 7: Define tu Proyecto del Curso (5 minutos)

**Objetivo**: Decidir qué construirás como proyecto final.

### Preguntas guía:

1. **¿Qué problema quiero resolver?**
   _______________________________________________

2. **¿Quién usará mi agente?**
   - [ ] Yo mismo
   - [ ] Mi equipo
   - [ ] Usuarios finales
   - [ ] Portfolio personal

3. **¿Qué herramientas necesitará?** (máximo 3 para empezar)
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

4. **¿Cómo sabré que funciona?** (define éxito)
   _______________________________________________

**Duración**: 5 minutos

---

## 📝 Ejercicio 8: Primera Práctica de Documentación (3 minutos)

**Objetivo**: Empezar el hábito de documentar tu aprendizaje.

### Tarea:

Crea un archivo en tu computadora:

```bash
# Crear carpeta para el curso
mkdir -p ~/fromzero-agentic-docker/modulo-01
cd ~/fromzero-agentic-docker/modulo-01

# Crear archivo de notas
touch mis-notas.md
# En Windows: echo. > mis-notas.md
```

Escribe en ese archivo:

```markdown
# Módulo 01: Mis Aprendizajes

**Fecha**: [HOY]

## Lo que aprendí:
- 

## Dudas que tengo:
- 

## Próximos pasos:
- 
```

**Duración**: 3 minutos

---

## 🔄 Ejercicio 9: Practica el Flujo "Minuto Fluido" (6 minutos)

**Objetivo**: Familiarizarte con la metodología del curso.

### Actividad:

Ejecuta este comando 5 veces, cronometrando cada ejecución:

```bash
# Comando simple: Crear y eliminar archivo
touch test-file.txt && ls -l test-file.txt && rm test-file.txt
```

**Repetición 1**: _____ segundos
**Repetición 2**: _____ segundos
**Repetición 3**: _____ segundos
**Repetición 4**: _____ segundos
**Repetición 5**: _____ segundos

**Observación**: ¿Fue más rápido con cada repetición?
_______________________________________________

**Duración**: 1 minuto x 5 repeticiones + 1 min reflexión = 6 minutos

---

## ✅ Ejercicio 10: Checklist de Preparación (3 minutos)

**Objetivo**: Confirmar que estás listo para el Módulo 02.

### Verifica:

- [ ] Tengo acceso a una terminal
- [ ] Python está instalado (o sé que necesito instalarlo)
- [ ] He explorado qué es un agente con IA
- [ ] Tengo una idea de qué quiero construir
- [ ] He establecido mi compromiso de tiempo
- [ ] He creado mi carpeta de trabajo
- [ ] Estoy motivado para continuar

**Si marcaste todos**, ¡estás listo para el Módulo 02! 🚀

**Si faltan algunos**, anota qué necesitas hacer:
_______________________________________________
_______________________________________________

**Duración**: 3 minutos

---

## 📊 Resumen del Tiempo

| Ejercicio | Duración | Completado |
|-----------|----------|------------|
| 1. Explora tu sistema | 5 min | [ ] |
| 2. Verifica Python | 4 min | [ ] |
| 3. Verifica Docker | 3 min | [ ] |
| 4. Reflexión y objetivos | 10 min | [ ] |
| 5. Investiga agente real | 8 min | [ ] |
| 6. Diagrama tu agente | 7 min | [ ] |
| 7. Define tu proyecto | 5 min | [ ] |
| 8. Documentación | 3 min | [ ] |
| 9. Minuto fluido | 6 min | [ ] |
| 10. Checklist | 3 min | [ ] |
| **TOTAL** | **54 min** | |

---

## 🎯 Próximos Pasos

1. Completa todos los ejercicios marcándolos como completados
2. Registra tus resultados en `retroalimentacion.md`
3. Actualiza tu progreso en `progreso.md`
4. Continúa al **Módulo 02: Prerrequisitos y Entorno**

---

**¡Excelente trabajo! Has completado tu primera actividad interactiva. 🎉**

Cada módulo tendrá ejercicios similares, siempre enfocados en la práctica inmediata.
