# Actividad Interactiva — SQL Core (respuestas en línea)

🎯 Objetivo
Instalar, configurar y verificar herramientas y practicar consultas SQL de alto impacto para reporting.

🐍 Ejercicio 1: Preparar entorno (15 minutos)
Objetivo: Tener una base de datos local (Postgres) corriendo con el dataset de ejemplo.

Pasos:
1. Verifica si tienes Docker:
```bash
docker --version
docker ps
```
2. Inicia Postgres local:
```bash
docker run --name pg-local -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres:13
```
3. Crea BD y carga el CSV de ventas (usa psql o pgadmin). Ejemplo con psql (ajusta credenciales):
```bash
cat data/sales_sample.csv | docker exec -i pg-local psql -U postgres -c "\copy ventas(order_id, cliente_id, fecha, producto, cantidad, precio_unitario, total) FROM STDIN WITH CSV HEADER"
```

Verificación:
- Ejecuta:
```sql
SELECT COUNT(*) FROM ventas;
```
- Resultado: _______________

Duración: 15 minutos

🐣 Ejercicio 2: Top 5 clientes por facturación (20 minutos)
Objetivo: Escribir una consulta que devuelva los 5 clientes con mayor facturación anual.

SQL sugerido:
```sql
SELECT cliente_id, SUM(total) AS total_cliente
FROM ventas
WHERE fecha BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY cliente_id
ORDER BY total_cliente DESC
LIMIT 5;
```

Verificación (copiar resultado):
Cliente top1: _______________ Total: _______________

Duración: 20 minutos

🏃 Ejercicio 3: Rankings y Window Functions (30 minutos)
Objetivo: Calcular ranking por mes y top-3 productos por mes usando window functions.

SQL ejemplo:
```sql
WITH monthly AS (
  SELECT date_trunc('month', fecha) as fecha_trunc, producto, SUM(total) as total_producto
  FROM ventas
  GROUP BY 1,2
)
SELECT fecha_trunc, producto, total_producto,
  RANK() OVER (PARTITION BY fecha_trunc ORDER BY total_producto DESC) AS rank_month
FROM monthly
WHERE RANK() OVER (PARTITION BY fecha_trunc ORDER BY total_producto DESC) <= 3;
```

Nota: si tu SGDB no permite usar RANK() en WHERE directo, usa una CTE con row_number.

Verificación: copia un resultado ejemplo (mes, producto, rank): _______________

Duración: 30 minutos

🔁 Ejercicio 4: Carga incremental y MERGE/UPSERT (40 minutos)
Objetivo: Simular una carga incremental y aplicar MERGE para actualizar/insertar datos en tabla destino.

Pasos:
1. Crea tabla destino `ventas_mart`.
2. Prepara un CSV incremental `data/sales_incremental.csv`.
3. Usa MERGE (ejemplo en Postgres 15 usa INSERT ... ON CONFLICT) o sintaxis MERGE si tu SGDB la soporta.

SQL ejemplo (Postgres UPSERT):
```sql
INSERT INTO ventas_mart (order_id, cliente_id, fecha, producto, cantidad, precio_unitario, total)
SELECT order_id, cliente_id, fecha, producto, cantidad, precio_unitario, total FROM ventas_stage
ON CONFLICT (order_id) DO UPDATE SET
  cantidad = EXCLUDED.cantidad,
  precio_unitario = EXCLUDED.precio_unitario,
  total = EXCLUDED.total;
```

Verificación: número de filas nuevas: _______________ filas actualizadas: _______________

Duración: 40 minutos

🧰 Ejercicio 5: Optimización básica (30 minutos)
Objetivo: Evaluar costos de consulta y proponer un índice o partición.

Pasos:
1. Ejecuta `EXPLAIN ANALYZE` en una consulta de join/aggregate.
2. Observa si hay secuencias completas o faltan índices.
3. Crea índice ejemplo si procede:
```sql
CREATE INDEX idx_ventas_cliente_fecha ON ventas(cliente_id, fecha);
```

Verificación: tiempo antes: _______________ ms tiempo después: _______________ ms

Duración: 30 minutos

📦 Ejercicio 6: Mini-proyecto (2 horas)
Objetivo: Construir un conjunto de consultas que alimenten un dashboard de ventas con: ventas por día, top clientes, churn semanal y métrica de retención.

Entregables:
- Script SQL con vistas/materializadas para: daily_sales, top_clients, weekly_churn, retention_metrics.
- Archivo: queries/sql_dashboard.sql

Duración: 2 horas

📊 Resumen de Tiempo
Ejercicio	Duración	Completado
1. Preparar entorno	15 min	[ ]
2. Top 5 clientes	20 min	[ ]
3. Window functions	30 min	[ ]
4. MERGE/UPSERT	40 min	[ ]
5. Optimización	30 min	[ ]
6. Mini-proyecto	120 min	[ ]
TOTAL	~5 horas

Próximo paso: Actualiza `progreso.md` con tus tiempos y sube las consultas a la carpeta del módulo.
