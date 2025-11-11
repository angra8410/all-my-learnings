# Actividad Interactiva — Seguridad y Gobernanza

🎯 Objetivo
Implementar RLS simple, gestionar secretos y documentar una política básica de gobernanza.

🔒 Ejercicio 1: Gestión de secretos (20 minutos)  
Objetivo: No poner secretos en el código; usar GitHub Secrets o Databricks Secrets.

Pasos (GitHub Actions / repo):
1. Añade `DB_TOKEN` como secret en GitHub (Settings > Secrets).
2. En workflow usa: `${{ secrets.DB_TOKEN }}`.

Verificación:
- Workflow: secrets accesible en job (no imprimir valor) -> yes / no

Duración: 20 minutos

🛡 Ejercicio 2: Implementar Row-Level Security (30 minutos)  
Objetivo: Añadir RLS en una tabla Postgres (ejemplo) o en Snowflake.

Ejemplo Postgres (policy):
```sql
-- Crear role y policy
CREATE ROLE analyst;
CREATE TABLE ventas (..., region text, ...);

-- RLS: permitir ver sólo rows de su region
ALTER TABLE ventas ENABLE ROW LEVEL SECURITY;
CREATE POLICY region_policy
  ON ventas
  USING (region = current_setting('app.current_region', true));
```

Pasos:
1. Simula usuario con `SET app.current_region = 'north'`.
2. Ejecuta `SELECT * FROM ventas` y confirma resultados filtrados.

Verificación: filas visibles para region 'north': __

Duración: 30 minutos

🧾 Ejercicio 3: Enmascarado de PII (30 minutos)  
Objetivo: Crear vista que devuelve datos enmascarados (ejemplo: email, phone).

SQL ejemplo:
```sql
CREATE VIEW ventas_safe AS
SELECT order_id,
       cliente_id,
       regexp_replace(email, '(^[^@]{3}).+(@.+$)', '\\1***\\2') AS email_masked,
       substring(phone from 1 for 3) || '***' AS phone_masked,
       total
FROM ventas;
```

Verificación: muestra un registro con `email_masked`, `phone_masked`: __

Duración: 30 minutos

📜 Ejercicio 4: Auditoría básica (25 minutos)  
Objetivo: Registrar acceso/ejecuciones básicas en una tabla audit.

SQL example:
```sql
CREATE TABLE audit_log (
  id serial primary key,
  user_name text,
  action text,
  object_name text,
  occurred_at timestamptz default now()
);

-- Insertar desde trigger (ejemplo simplificado)
```

Verificación: insertar y leer última fila -> user/action -> __

Duración: 25 minutos

📦 Mini-proyecto (2 horas)  
Objetivo: Implementar RLS para un caso de uso, gestionar secrets en el repo/Databricks y crear el runbook de incident response.

Entregables:
- examples/rls_example.sql
- examples/secrets_example.md
- runbook_security.md

Duración: 2 horas
