-- ============================================================================
-- SQL Data Quality Tests Examples
-- ============================================================================
--
-- Este archivo contiene ejemplos de tests SQL para validar calidad de datos.
-- Cubre el 20% de checks que previenen 80% de problemas de calidad.
--
-- Uso:
-- 1. Ejecutar después de cada carga ETL
-- 2. Integrar en pipeline de CI/CD
-- 3. Alertar si algún test falla
--
-- Autor: Data Engineering Pareto 20/80 Course
-- ============================================================================

-- ============================================================================
-- TEST CATEGORY 1: COMPLETENESS (Datos completos)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 1.1: Row Count (¿Se cargaron datos?)
-- ----------------------------------------------------------------------------

-- Expect: count > 0
SELECT 
    'Row Count Test' as test_name,
    COUNT(*) as row_count,
    CASE 
        WHEN COUNT(*) = 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE date_key = 20240115;  -- Fecha de la carga

-- ----------------------------------------------------------------------------
-- TEST 1.2: Null Checks en Columnas Críticas
-- ----------------------------------------------------------------------------

-- Expect: null_count = 0
SELECT 
    'Null Check - Customer Key' as test_name,
    COUNT(*) as null_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE customer_key IS NULL;

-- Versión genérica para múltiples columnas
WITH null_checks AS (
    SELECT 
        'transaction_id' as column_name,
        COUNT(*) FILTER (WHERE transaction_id IS NULL) as null_count
    FROM fact_sales
    UNION ALL
    SELECT 
        'customer_key',
        COUNT(*) FILTER (WHERE customer_key IS NULL)
    FROM fact_sales
    UNION ALL
    SELECT 
        'product_key',
        COUNT(*) FILTER (WHERE product_key IS NULL)
    FROM fact_sales
    UNION ALL
    SELECT 
        'total_amount',
        COUNT(*) FILTER (WHERE total_amount IS NULL)
    FROM fact_sales
)
SELECT 
    column_name,
    null_count,
    CASE 
        WHEN null_count > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM null_checks;

-- ----------------------------------------------------------------------------
-- TEST 1.3: Missing Data (¿Hay gaps en la serie temporal?)
-- ----------------------------------------------------------------------------

-- Expect: no missing dates
WITH date_range AS (
    SELECT generate_series(
        '2024-01-01'::date,
        '2024-01-31'::date,
        '1 day'::interval
    )::date as expected_date
),
actual_dates AS (
    SELECT DISTINCT d.full_date
    FROM fact_sales f
    JOIN dim_date d ON f.date_key = d.date_key
    WHERE d.full_date BETWEEN '2024-01-01' AND '2024-01-31'
)
SELECT 
    'Missing Dates Test' as test_name,
    dr.expected_date,
    CASE 
        WHEN ad.full_date IS NULL THEN 'MISSING'
        ELSE 'OK'
    END as status
FROM date_range dr
LEFT JOIN actual_dates ad ON dr.expected_date = ad.full_date
WHERE ad.full_date IS NULL;

-- ============================================================================
-- TEST CATEGORY 2: UNIQUENESS (Datos únicos)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 2.1: Duplicate Primary Keys
-- ----------------------------------------------------------------------------

-- Expect: duplicate_count = 0
WITH duplicates AS (
    SELECT 
        transaction_id,
        COUNT(*) as cnt
    FROM fact_sales
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
)
SELECT 
    'Duplicate Transaction IDs' as test_name,
    COUNT(*) as duplicate_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM duplicates;

-- ----------------------------------------------------------------------------
-- TEST 2.2: Duplicate Business Keys en Dimensions (SCD Type 2)
-- ----------------------------------------------------------------------------

-- Para SCD Type 2, solo debe haber 1 registro "current" por customer_id
-- Expect: duplicate_current = 0
WITH duplicate_current AS (
    SELECT 
        customer_id,
        COUNT(*) as cnt
    FROM dim_customer
    WHERE is_current = TRUE
    GROUP BY customer_id
    HAVING COUNT(*) > 1
)
SELECT 
    'Duplicate Current Customers' as test_name,
    COUNT(*) as duplicate_current,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM duplicate_current;

-- ============================================================================
-- TEST CATEGORY 3: VALIDITY (Datos válidos)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 3.1: Range Checks (Valores en rango esperado)
-- ----------------------------------------------------------------------------

-- Quantity debe ser > 0
SELECT 
    'Invalid Quantity Test' as test_name,
    COUNT(*) as invalid_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE quantity <= 0;

-- Total amount debe ser >= 0
SELECT 
    'Negative Total Amount Test' as test_name,
    COUNT(*) as invalid_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE total_amount < 0;

-- ----------------------------------------------------------------------------
-- TEST 3.2: Referential Integrity (Foreign Keys válidos)
-- ----------------------------------------------------------------------------

-- Todos los customer_keys deben existir en dim_customer
SELECT 
    'Orphan Customers Test' as test_name,
    COUNT(*) as orphan_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales f
LEFT JOIN dim_customer c ON f.customer_key = c.customer_key
WHERE c.customer_key IS NULL;

-- Todos los product_keys deben existir en dim_product
SELECT 
    'Orphan Products Test' as test_name,
    COUNT(*) as orphan_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales f
LEFT JOIN dim_product p ON f.product_key = p.product_key
WHERE p.product_key IS NULL;

-- ----------------------------------------------------------------------------
-- TEST 3.3: Format Checks (Email, phone, etc.)
-- ----------------------------------------------------------------------------

-- Email debe tener formato válido
SELECT 
    'Invalid Email Format' as test_name,
    COUNT(*) as invalid_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM dim_customer
WHERE email IS NOT NULL
  AND email NOT LIKE '%@%.%';

-- Phone debe tener solo números y caracteres permitidos
SELECT 
    'Invalid Phone Format' as test_name,
    COUNT(*) as invalid_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM dim_customer
WHERE phone IS NOT NULL
  AND phone !~ '^[0-9\-\+\(\) ]+$';  -- Regex para validar formato

-- ============================================================================
-- TEST CATEGORY 4: CONSISTENCY (Datos consistentes)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 4.1: Calculated Fields (Validar cálculos)
-- ----------------------------------------------------------------------------

-- total_amount debe ser igual a quantity * unit_price - discount + tax
SELECT 
    'Incorrect Total Amount Calculation' as test_name,
    COUNT(*) as error_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE ABS(
    total_amount - (quantity * unit_price - discount_amount + tax_amount)
) > 0.01;  -- Tolerance de 1 centavo por redondeo

-- profit debe ser total_amount - cost
SELECT 
    'Incorrect Profit Calculation' as test_name,
    COUNT(*) as error_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales
WHERE cost_amount IS NOT NULL
  AND ABS(profit_amount - (total_amount - cost_amount)) > 0.01;

-- ----------------------------------------------------------------------------
-- TEST 4.2: Cross-Table Consistency
-- ----------------------------------------------------------------------------

-- Suma de fact_sales debe coincidir con aggregate table
WITH fact_sum AS (
    SELECT 
        date_key,
        product_key,
        SUM(total_amount) as fact_total
    FROM fact_sales
    WHERE date_key = 20240115
    GROUP BY date_key, product_key
),
agg_sum AS (
    SELECT 
        date_key,
        product_key,
        total_revenue as agg_total
    FROM agg_sales_daily
    WHERE date_key = 20240115
)
SELECT 
    'Fact vs Aggregate Mismatch' as test_name,
    COUNT(*) as mismatch_count,
    CASE 
        WHEN COUNT(*) > 0 THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sum f
FULL OUTER JOIN agg_sum a 
    ON f.date_key = a.date_key 
    AND f.product_key = a.product_key
WHERE ABS(COALESCE(f.fact_total, 0) - COALESCE(a.agg_total, 0)) > 0.01;

-- ============================================================================
-- TEST CATEGORY 5: TIMELINESS (Datos a tiempo)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 5.1: Freshness (¿Datos recientes cargados?)
-- ----------------------------------------------------------------------------

-- Expect: last_load_time < 6 horas atrás
SELECT 
    'Data Freshness Test' as test_name,
    MAX(loaded_at) as last_load_time,
    CURRENT_TIMESTAMP - MAX(loaded_at) as age,
    CASE 
        WHEN CURRENT_TIMESTAMP - MAX(loaded_at) > INTERVAL '6 hours' THEN 'FAIL'
        ELSE 'PASS'
    END as status
FROM fact_sales;

-- ============================================================================
-- TEST CATEGORY 6: STATISTICAL OUTLIERS
-- ============================================================================

-- ----------------------------------------------------------------------------
-- TEST 6.1: Detectar Valores Anómalos (IQR method)
-- ----------------------------------------------------------------------------

WITH stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY total_amount) as q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_amount) as q3
    FROM fact_sales
),
outliers AS (
    SELECT 
        f.transaction_id,
        f.total_amount,
        s.q1,
        s.q3,
        (s.q3 - s.q1) as iqr
    FROM fact_sales f
    CROSS JOIN stats s
    WHERE f.total_amount < (s.q1 - 1.5 * (s.q3 - s.q1))
       OR f.total_amount > (s.q3 + 1.5 * (s.q3 - s.q1))
)
SELECT 
    'Outlier Detection Test' as test_name,
    COUNT(*) as outlier_count,
    MIN(total_amount) as min_outlier,
    MAX(total_amount) as max_outlier,
    CASE 
        WHEN COUNT(*) > 100 THEN 'WARNING'  -- > 100 outliers es sospechoso
        ELSE 'PASS'
    END as status
FROM outliers;

-- ============================================================================
-- COMPREHENSIVE TEST SUITE (Ejecutar todos los tests a la vez)
-- ============================================================================

CREATE OR REPLACE FUNCTION run_all_data_quality_tests()
RETURNS TABLE (
    test_category VARCHAR,
    test_name VARCHAR,
    status VARCHAR,
    error_count BIGINT,
    details TEXT
) AS $$
BEGIN
    -- Test 1: Row count
    RETURN QUERY
    SELECT 
        'Completeness'::VARCHAR as test_category,
        'Row Count'::VARCHAR as test_name,
        CASE WHEN COUNT(*) > 0 THEN 'PASS' ELSE 'FAIL' END::VARCHAR,
        COUNT(*),
        'Total rows: ' || COUNT(*)::TEXT
    FROM fact_sales
    WHERE date_key >= TO_CHAR(CURRENT_DATE, 'YYYYMMDD')::INTEGER;
    
    -- Test 2: Nulls en columnas clave
    RETURN QUERY
    SELECT 
        'Completeness'::VARCHAR,
        'Null Customer Keys'::VARCHAR,
        CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END::VARCHAR,
        COUNT(*),
        'Null count: ' || COUNT(*)::TEXT
    FROM fact_sales
    WHERE customer_key IS NULL;
    
    -- Test 3: Duplicados
    RETURN QUERY
    WITH dups AS (
        SELECT transaction_id, COUNT(*) as cnt
        FROM fact_sales
        GROUP BY transaction_id
        HAVING COUNT(*) > 1
    )
    SELECT 
        'Uniqueness'::VARCHAR,
        'Duplicate Transaction IDs'::VARCHAR,
        CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END::VARCHAR,
        COUNT(*),
        'Duplicates found: ' || COUNT(*)::TEXT
    FROM dups;
    
    -- Test 4: Valores negativos
    RETURN QUERY
    SELECT 
        'Validity'::VARCHAR,
        'Negative Amounts'::VARCHAR,
        CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END::VARCHAR,
        COUNT(*),
        'Negative values: ' || COUNT(*)::TEXT
    FROM fact_sales
    WHERE total_amount < 0;
    
    -- Más tests...
END;
$$ LANGUAGE plpgsql;

-- Ejecutar test suite
-- SELECT * FROM run_all_data_quality_tests();

-- ============================================================================
-- PARETO 20% - Testing Best Practices
-- ============================================================================
--
-- 1. TESTS ESENCIALES (cubre 80% de problemas):
--    ✅ Row count > 0
--    ✅ No nulls en columnas clave
--    ✅ No duplicados en primary keys
--    ✅ Valores en rango válido (>= 0, fechas razonables)
--    ✅ Foreign keys válidos
--
-- 2. CUÁNDO EJECUTAR:
--    - Después de cada carga ETL
--    - Antes de publicar datos a usuarios
--    - En CI/CD pipeline
--    - Scheduled (ej: diario)
--
-- 3. QUÉ HACER SI UN TEST FALLA:
--    - Log el error con detalles
--    - Alertar (email, Slack, PagerDuty)
--    - Bloquear pipeline (no cargar datos malos)
--    - Rollback si es posible
--
-- 4. STORING TEST RESULTS:
--    - Crear tabla test_results para tracking histórico
--    - Campos: test_name, execution_time, status, error_count, details
--
-- 5. AUTOMATIZACIÓN:
--    - Integrar con Airflow (task de validación)
--    - Usar Great Expectations para tests más sofisticados
--    - Generar reports automáticos
--
-- 6. PERFORMANCE:
--    - Usar sampling para tables muy grandes
--    - Ejecutar tests en parallel cuando sea posible
--    - Indexar columnas usadas en tests
--
-- NEXT STEPS:
--    1. Ejecutar estos tests en tu base de datos
--    2. Crear tabla test_results para tracking
--    3. Integrar en tu pipeline ETL
--    4. Configurar alertas automáticas
-- ============================================================================
