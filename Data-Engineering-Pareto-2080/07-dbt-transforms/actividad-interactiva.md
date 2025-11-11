# Actividad Interactiva — dbt / Transforms

🎯 Objetivo
Crear un pequeño proyecto dbt (o estructura equivalente) que transforme raw → staging → marts con tests y documentación.

🛠 Ejercicio 1: Inicializar proyecto dbt (20 minutos)  
Objetivo: Crear el skeleton del proyecto.

Pasos:
1. Instala dbt-core y el adaptador (ej. dbt-spark o dbt-postgres):
```bash
pip install dbt-core dbt-spark   # o dbt-postgres
dbt init ventas_project
```
2. Configura `profiles.yml` con tu target (usa placeholders `<YOUR_CONN>`).

Verificación: `dbt debug` -> OK / FAIL. Mensaje: _______________

Duración: 20 minutos

🔁 Ejercicio 2: Crear modelo staging (30 minutos)  
Objetivo: Crear `models/staging/stg_ventas.sql` que lea la tabla raw y normalice tipos.

Ejemplo `stg_ventas.sql`:
```sql
with raw as (
  select * from {{ source('raw', 'ventas') }}
)
select
  order_id,
  cliente_id::int as cliente_id,
  cast(fecha as date) as fecha,
  lower(trim(producto)) as producto,
  cast(cantidad as int) as cantidad,
  cast(precio_unitario as numeric) as precio_unitario,
  cast(total as numeric) as total
from raw;
```
Verificación: `dbt run --models staging` -> filas procesadas: _______________

Duración: 30 minutos

🧪 Ejercicio 3: Añadir tests y ejecutar (25 minutos)  
Objetivo: Añadir tests YAML y ejecutar `dbt test`.

Ejemplo `schema.yml`:
```yaml
version: 2

models:
  - name: stg_ventas
    columns:
      - name: order_id
        tests:
          - not_null
          - unique
      - name: cliente_id
        tests:
          - not_null
```
Ejecuta: `dbt test --models stg_ventas`  
Verificación: tests passed -> _______________

Duración: 25 minutos

📦 Ejercicio 4: Crear mart y docs (45 minutos)  
Objetivo: Crear `models/marts/mart_sales.sql` con agregaciones para reporting y generar docs.

Pasos:
1. Escribe mart SQL (daily_sales, top_clients).
2. Ejecuta `dbt run --models marts` y `dbt docs generate`.
3. Visualiza docs con `dbt docs serve`.

Verificación: URL docs local: _______________

Duración: 45 minutos

📦 Mini-proyecto (2 horas)  
Objetivo: Proyecto end-to-end dbt: source raw -> staging -> marts -> tests -> docs.  
Entregables:
- ventas_project/ (models, schema.yml)
- runbook_dbftest.md (instrucciones para CI)
Duración: 2 horas
