# Módulo 8: Colaboración e Inglés Técnico

## Introducción

En este módulo desarrollarás habilidades esenciales para trabajar en equipos internacionales: inglés técnico, documentación efectiva, code reviews y comunicación en entornos distribuidos.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Comunicarte efectivamente en inglés técnico
- 🎯 Escribir documentación clara en inglés
- 🎯 Realizar y recibir code reviews constructivas
- 🎯 Participar en reuniones técnicas internacionales
- 🎯 Colaborar en equipos distribuidos
- 🎯 Usar terminología técnica correctamente

## ¿Por qué es importante?

El 90% de la documentación técnica está en inglés. Los mejores trabajos y proyectos requieren inglés. La colaboración global es el estándar en tech.

## Conceptos Principales

### 1. Vocabulario Técnico Esencial

**Data Engineering Terms**:

| Español | Inglés | Ejemplo de uso |
|---------|--------|----------------|
| Pipeline | Pipeline | "The ETL pipeline runs daily" |
| Datos | Data | "We process 1TB of data per day" |
| Almacén de datos | Data warehouse | "Load data into the warehouse" |
| Lago de datos | Data lake | "Store raw data in the lake" |
| Transformar | Transform | "Transform the data before loading" |
| Orquestar | Orchestrate | "Airflow orchestrates our workflows" |
| Fallo/Error | Failure/Error | "The pipeline failed due to timeout" |
| Registro | Log | "Check the logs for errors" |
| Métrica | Metric | "Monitor pipeline metrics" |
| Dependencia | Dependency | "This task depends on the previous one" |

**Verbos comunes**:
- **Trigger**: Activar ("Trigger the pipeline manually")
- **Monitor**: Monitorear ("Monitor the execution")
- **Debug**: Depurar ("Debug the issue")
- **Optimize**: Optimizar ("Optimize query performance")
- **Deploy**: Desplegar ("Deploy to production")
- **Rollback**: Revertir ("Rollback the changes")
- **Scale**: Escalar ("Scale the infrastructure")

### 2. Escribir Documentación en Inglés

**README Template**:
```markdown
# Sales Data Pipeline

## Overview
This pipeline processes daily sales data from multiple sources.

## Architecture
```
API → Airflow → S3 → Spark → Redshift
```

## Prerequisites
- Python 3.11+
- AWS credentials configured
- Airflow 2.7+

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```bash
# Run locally
python run_pipeline.py

# Run with Airflow
airflow dags trigger sales_etl
```

## Configuration
Edit `.env` file:
- `API_KEY`: Sales API key
- `DB_HOST`: Database host
- `LOG_LEVEL`: Logging level (INFO, DEBUG)

## Testing
```bash
pytest tests/
```

## Monitoring
- Dashboard: [link]
- Alerts: #data-alerts on Slack

## Troubleshooting
**Issue**: Pipeline fails with timeout
**Solution**: Increase timeout in config

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
MIT
```

**Docstrings en inglés**:
```python
def extract_sales_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Extract sales data from API for given date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    
    Returns:
        DataFrame with columns: [date, product_id, amount, quantity]
    
    Raises:
        ConnectionError: If API is unreachable
        ValueError: If dates are invalid
    
    Example:
        >>> df = extract_sales_data('2024-01-01', '2024-01-31')
        >>> len(df)
        1000
    """
    # Implementation
    pass
```

### 3. Code Reviews

**Escribir un code review**:

```markdown
## Review de PR #123: Add data quality checks

### Summary
Good addition! The data quality checks will prevent bad data from 
entering the warehouse.

### Strengths
- ✅ Well-structured validation functions
- ✅ Good test coverage
- ✅ Clear error messages

### Suggestions

#### 1. Performance concern
```python
# Current (slow for large datasets)
if df['price'].min() < 0:
    raise ValueError("Negative prices found")

# Suggested (faster)
negative_prices = df[df['price'] < 0]
if len(negative_prices) > 0:
    raise ValueError(f"Found {len(negative_prices)} negative prices")
```

#### 2. Missing edge case
Consider adding validation for empty DataFrames:
```python
if df.empty:
    raise ValueError("Cannot validate empty DataFrame")
```

#### 3. Documentation
Please add docstring to `validate_sales()` function explaining:
- What validations are performed
- What exceptions can be raised

### Questions
- How should we handle partial failures? (e.g., 1% of rows invalid)
- Should we log warnings instead of failing completely?

### Approval
Approved pending minor changes. Great work! 🎉

### Action Items
- [ ] Add empty DataFrame check
- [ ] Optimize performance for large datasets
- [ ] Add docstrings
```

**Responder a code review**:
```markdown
Thanks for the thorough review @reviewer!

> Performance concern

Good catch! I've updated the code to check in batches.
See commit abc123

> Missing edge case

Added empty DataFrame validation in commit def456

> Questions

For partial failures, I propose:
1. Log warning with row count
2. Save invalid rows to S3 for review
3. Continue with valid rows

What do you think?

All action items completed ✅
```

### 4. Comunicación en Reuniones

**Frases útiles**:

**Para presentar:**
- "Let me walk you through the architecture"
- "I'd like to share some findings"
- "Here's what we're planning to do"

**Para aclarar:**
- "Could you clarify what you mean by...?"
- "Just to make sure I understand correctly..."
- "Let me rephrase that"

**Para opiniones:**
- "In my opinion, we should..."
- "I think the best approach would be..."
- "From my experience..."

**Para problemas:**
- "We're facing an issue with..."
- "The main challenge is..."
- "I need help with..."

**Para acuerdo:**
- "That makes sense"
- "I agree with that approach"
- "Sounds good to me"

**Para desacuerdo (diplomático):**
- "I see your point, but have we considered...?"
- "That's one way to look at it. Another option might be..."
- "I have some concerns about..."

### 5. Emails Técnicos

**Template de email para reportar issue**:
```
Subject: Production pipeline failure - Sales ETL

Hi team,

The sales ETL pipeline failed this morning at 2:15 AM UTC.

**Issue**: 
Timeout error when connecting to the API

**Impact**:
- No sales data for 2024-01-15
- Downstream reports delayed
- Affecting 3 stakeholders

**Root Cause**:
API response time increased from 2s to 30s due to their maintenance

**Resolution**:
- Increased timeout from 10s to 60s
- Re-ran pipeline successfully at 3:00 AM
- Data is now up to date

**Next Steps**:
- Monitor API performance
- Set up alerts for slow responses
- Consider implementing retry logic

**Timeline**:
02:15 AM - Pipeline failed
02:30 AM - Issue identified
02:45 AM - Fix deployed
03:00 AM - Pipeline re-run successful

Let me know if you have any questions.

Best regards,
[Tu nombre]
```

### 6. Slack/Chat Communication

**Good practices**:

✅ **Be clear and concise**:
```
Bad: "hey, thing not working"
Good: "Sales ETL failed with timeout error. Investigating now."
```

✅ **Use threads**:
```
Main message: "Q1 data refresh completed"
Thread: "Details: 10M records, 45 min runtime, no errors"
```

✅ **Tag appropriately**:
```
"@john Can you review the PR when you have time?"
"@here Pipeline is down, urgent!"
```

✅ **Update status**:
```
"Issue: Pipeline failing [INVESTIGATING]"
"Issue: Pipeline failing [FIXED] - timeout increased"
```

### 7. Git Commit Messages

**Buenas prácticas**:

```bash
# Bad
git commit -m "fix"
git commit -m "updated file"

# Good
git commit -m "fix: increase API timeout from 10s to 60s"
git commit -m "feat: add data quality validations for sales data"
git commit -m "docs: update README with troubleshooting section"
```

**Conventional Commits**:
```
feat: Add new feature
fix: Fix a bug
docs: Documentation changes
style: Code style changes (formatting)
refactor: Code refactoring
test: Add or update tests
chore: Maintenance tasks
```

## Ejercicios Prácticos

### Ejercicio 1: Traducir Documentación

Traduce este README al inglés:

```markdown
# Pipeline de Ventas

## Descripción
Este pipeline procesa datos de ventas diariamente.

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
Ejecutar el pipeline:
```bash
python main.py
```

## Configuración
Editar el archivo config.yaml con tus credenciales.
```

### Ejercicio 2: Escribir Code Review

Revisa este código y escribe comentarios en inglés:

```python
def process(data):
    # Eliminar nulos
    data = data.dropna()
    
    # Calcular total
    data['total'] = data['price'] * data['qty']
    
    return data
```

### Ejercicio 3: Email de Incidente

Escribe un email en inglés reportando:
- Pipeline de ML falló
- Causa: Cambio no documentado en schema
- Impacto: Modelo no actualizado hoy
- Solución aplicada

## Frases y Expresiones Útiles

### En Code Reviews
- "Nice work on..."
- "Consider using... instead of..."
- "This could be simplified by..."
- "Have you thought about...?"
- "LGTM" (Looks Good To Me)
- "Minor nit:" (pequeño detalle)

### En Reuniones
- "That's a good point"
- "Let's take this offline" (hablemos después)
- "I'll follow up on that"
- "Can we table this for now?" (dejar para después)
- "Let's circle back to..." (volver a hablar de)

### En Documentación
- "Note that..."
- "Keep in mind..."
- "As a workaround..."
- "For more details, see..."
- "TL;DR" (Too Long; Didn't Read - resumen)

## De Open Source a Enterprise

| Aspecto | Open Source | Enterprise |
|---------|-------------|------------|
| **Idioma docs** | Inglés mayormente | Inglés obligatorio |
| **Code reviews** | Voluntarias | Obligatorias |
| **Comunicación** | GitHub Issues, Discord | Slack, Jira, Confluence |
| **Reuniones** | Asíncronas | Síncronas + asíncronas |

## Conceptos Clave

- 🔑 **Technical English**: Inglés para tech
- 🔑 **Code Review**: Revisión de código
- 🔑 **Documentation**: Documentación técnica
- 🔑 **Async Communication**: Comunicación asíncrona
- 🔑 **Distributed Team**: Equipo distribuido

## Próximos Pasos

En el **Módulo 9: Proyecto Integrador** aplicarás:
- Todo lo aprendido en el curso
- Construirás un sistema RAG completo
- Documentarás en inglés
- Presentarás tu proyecto

## Recursos Adicionales

- 📖 [Technical Writing Guide](https://developers.google.com/tech-writing)
- 📖 [Conventional Commits](https://www.conventionalcommits.org/)
- 🎥 [English for Developers](https://www.youtube.com/c/EnglishForDevelopers)
- 📚 "The Art of Readable Code"

---

**¡Excelente trabajo completando el Módulo 8!** 🎉

Ya tienes las habilidades para colaborar globalmente. Continúa al **Módulo 9: Proyecto Integrador**.
