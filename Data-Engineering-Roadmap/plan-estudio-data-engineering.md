# 🎓 Plan de Estudio — Data Engineering Roadmap

## Resumen Ejecutivo

Este curso integral guía a estudiantes desde los fundamentos de ingeniería de datos hasta la construcción de pipelines de producción completos. Combina teoría sólida con práctica intensiva, cubriendo SQL avanzado, Python para ETL, transformaciones con dbt, orquestación con Airflow, y modelado de datos en la nube.

**Nivel:** Principiante a Intermedio  
**Duración:** 8-12 semanas (10-15 horas/semana)  
**Modalidad:** Auto-guiado con ejercicios verificables  
**Proyecto Final:** Pipeline end-to-end desplegado en cloud

## 🎯 Objetivos de Aprendizaje

Al completar este roadmap serás capaz de:

1. Diseñar y construir pipelines de datos escalables
2. Escribir SQL optimizado para grandes volúmenes de datos
3. Desarrollar procesos ETL/ELT con Python y dbt
4. Orquestar workflows complejos con Apache Airflow
5. Modelar datos usando esquemas dimensionales y relacionales
6. Implementar testing, monitoreo y observabilidad
7. Desplegar soluciones en plataformas cloud (AWS/Azure/GCP)
8. Aplicar mejores prácticas de ingeniería de software a datos

## 📚 Estructura del Curso

### **Módulo 01: Introducción a Data Engineering**
- 🎯 Rol del Data Engineer en organizaciones modernas
- 🔧 Configuración del entorno de desarrollo
- 🐳 Docker y contenedores para desarrollo local
- ⏱️ Duración: 4-6 horas

### **Módulo 02: SQL para Data Engineering**
- 📊 Consultas avanzadas: CTEs, window functions, optimización
- 🔄 Operaciones MERGE, UPSERT y deduplicación
- 🚀 Performance tuning e índices
- ⏱️ Duración: 12-15 horas

### **Módulo 03: Python para Data Engineering**
- 🐍 Ingesta de datos desde APIs y bases de datos
- 🔄 Transformaciones con pandas y procesamiento batch
- 📦 Manejo de dependencias y entornos virtuales
- ⏱️ Duración: 10-12 horas

### **Módulo 04: Transformaciones con dbt**
- 🎨 Models, tests, y documentación
- 🔄 Flujo dev → staging → production
- 📊 Materializations (table, view, incremental)
- ⏱️ Duración: 10-12 horas

### **Módulo 05: Orquestación con Airflow**
- 🔀 DAGs, operators y sensores
- 📅 Scheduling y dependencias
- 🔍 Monitoreo y troubleshooting
- ⏱️ Duración: 12-15 horas

### **Módulo 06: Data Warehousing con Snowflake**
- ❄️ Arquitectura multi-cluster y virtual warehouses
- 🔐 Roles, permisos y governance
- 💰 Optimización de costos y performance
- ⏱️ Duración: 8-10 horas

### **Módulo 07: Modelado Dimensional**
- ⭐ Diseño de star schema y snowflake schema
- 📅 Slowly Changing Dimensions (SCD)
- 🎯 Fact tables y métricas calculadas
- ⏱️ Duración: 8-10 horas

### **Módulo 08: Modelado Relacional**
- 🔗 Normalización (1NF, 2NF, 3NF)
- 🔑 Primary keys, foreign keys e integridad referencial
- 📐 Diseño de esquemas transaccionales
- ⏱️ Duración: 6-8 horas

### **Módulo 09: Testing y Depuración**
- ✅ Tests unitarios, integración y data quality
- 🐛 Debugging de pipelines y análisis de logs
- 📊 Great Expectations y validaciones
- ⏱️ Duración: 8-10 horas

### **Módulo 10: Pipelines en Cloud**
- ☁️ AWS (S3, Glue, Redshift) / Azure (Synapse, Data Factory) / GCP (BigQuery, Dataflow)
- 🚀 CI/CD para pipelines de datos
- 🔄 IaC con Terraform
- ⏱️ Duración: 12-15 horas

### **Módulo 11: Buenas Prácticas y Observabilidad**
- 📝 Logging estructurado y monitoreo
- 🔔 Alertas y SLAs
- 🔒 Seguridad y compliance (GDPR, encriptación)
- ⏱️ Duración: 6-8 horas

### **Módulo 12: Proyecto Integrador**
- 🎯 Pipeline completo: ingestión → transformación → visualización
- 📦 Entregables: código, documentación, presentación
- 🚀 Despliegue en producción (cloud)
- ⏱️ Duración: 15-20 horas

## 📁 Formato de cada Módulo

Cada módulo incluye 5 archivos estandarizados:

1. **README.md**: Objetivos, contenido teórico, actividades prácticas, duración
2. **actividad-interactiva.md**: 6-10 ejercicios prácticos con:
   - Objetivo claro y contexto
   - Pasos detallados con comandos verificables
   - Campos para completar respuestas
   - Duración estimada por ejercicio
   - Criterios de validación
3. **progreso.md**: Checklist de avance con casillas marcables
4. **retroalimentacion.md**: Rúbrica de evaluación con porcentajes
5. **recursos.md**: Enlaces, datasets, herramientas, documentación oficial

## 🛠️ Prerequisitos

### Conocimientos Previos
- ✅ Programación básica (cualquier lenguaje)
- ✅ Línea de comandos/terminal (básico)
- ✅ Conceptos de bases de datos (deseable)
- ✅ Git básico (clone, commit, push)

### Herramientas Necesarias
- 💻 Laptop/PC con 8GB RAM mínimo
- 🐳 Docker Desktop instalado
- 🔧 Git instalado
- 📝 Editor de código (VSCode recomendado)
- ☁️ Cuenta gratuita en Snowflake/AWS/GCP (para módulos cloud)

## 🚀 Cómo Usar este Roadmap

### Paso 1: Configuración Inicial
```bash
# Clonar el repositorio
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Roadmap

# Crear rama de trabajo personal
git checkout -b feature/mi-progreso-data-eng
```

### Paso 2: Seguir el Orden Secuencial
- Comienza siempre por el **README.md** del módulo
- Lee el contenido teórico
- Completa los ejercicios de **actividad-interactiva.md**
- Marca tu progreso en **progreso.md**
- Revisa tus respuestas con **retroalimentacion.md**
- Consulta **recursos.md** para profundizar

### Paso 3: Ritmo Recomendado
- **Intensivo**: 2 módulos/semana (20+ horas/semana) → 6 semanas
- **Moderado**: 1 módulo/semana (10-15 horas/semana) → 12 semanas
- **Relajado**: 1 módulo cada 2 semanas (5-8 horas/semana) → 24 semanas

### Paso 4: Proyecto Integrador
Una vez completados los módulos 01-11, dedica tiempo al proyecto final. Este proyecto consolidará todos los conceptos y te dará un portafolio demostrable.

## 📊 Sistema de Evaluación

Cada módulo tiene criterios definidos en `retroalimentacion.md`:

- **Completitud**: ¿Se completaron todos los ejercicios? (30%)
- **Calidad técnica**: ¿El código funciona y sigue mejores prácticas? (40%)
- **Documentación**: ¿Están documentadas las decisiones y procesos? (20%)
- **Creatividad**: ¿Se agregaron mejoras o casos adicionales? (10%)

**Aprobado**: ≥70% | **Excelente**: ≥90%

## 🎓 Certificación y Siguientes Pasos

Al completar este roadmap:

1. ✅ Tendrás un repositorio con 12+ proyectos prácticos
2. ✅ Portfolio demostrable para entrevistas
3. ✅ Base sólida para certificaciones:
   - Snowflake SnowPro Core
   - AWS Certified Data Analytics
   - Google Professional Data Engineer
   - dbt Analytics Engineering Certification

### Recursos Adicionales Post-Curso
- 📚 Libros: "Designing Data-Intensive Applications" (Kleppmann)
- 🎥 Cursos avanzados: Databricks, Spark, Kafka
- 🤝 Comunidades: dbt Community, DataTalks.Club, Data Engineering Slack
- 📝 Blogs: Seattle Data Guy, Data Engineering Weekly

## 🤝 Contribuciones y Feedback

Este roadmap es un recurso vivo. Si encuentras errores, quieres sugerir mejoras o agregar recursos:

1. Abre un Issue en el repositorio
2. Propón cambios mediante Pull Request
3. Comparte tu experiencia y feedback

## 📞 Soporte

- **GitHub Issues**: Para reportar errores o sugerencias
- **Discussions**: Para preguntas generales del curso
- **README de cada módulo**: Incluye recursos específicos de ayuda

---

**¡Bienvenido al mundo de Data Engineering! 🚀**  
*Este journey transformará tu carrera en datos. ¡Comencemos!*