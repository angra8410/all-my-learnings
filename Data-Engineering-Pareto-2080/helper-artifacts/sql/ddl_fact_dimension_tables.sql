-- ============================================================================
-- SQL DDL Examples - Fact and Dimension Tables
-- ============================================================================
--
-- Este archivo contiene ejemplos de DDL (Data Definition Language) para
-- crear tablas de hechos (fact) y dimensiones (dimension) siguiendo el
-- modelo de star schema - el patrón más usado en data warehousing.
--
-- Cubre el 20% de patterns que usarás en 80% de tus diseños de warehouse.
--
-- Autor: Data Engineering Pareto 20/80 Course
-- ============================================================================

-- ============================================================================
-- DIMENSION TABLES (Slowly Changing Dimensions)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- dim_customer: Dimensión de clientes (SCD Type 2)
-- ----------------------------------------------------------------------------
-- SCD Type 2: Mantiene historial de cambios con effective_date y end_date
-- Permite analizar datos "as of" cualquier fecha histórica

CREATE TABLE dim_customer (
    customer_key        BIGSERIAL PRIMARY KEY,      -- Surrogate key (nunca cambia)
    customer_id         VARCHAR(50) NOT NULL,       -- Natural key (business ID)
    customer_name       VARCHAR(200) NOT NULL,
    email               VARCHAR(200),
    phone               VARCHAR(50),
    address             VARCHAR(500),
    city                VARCHAR(100),
    state               VARCHAR(50),
    country             VARCHAR(50),
    postal_code         VARCHAR(20),
    customer_segment    VARCHAR(50),                -- ej: 'Premium', 'Standard'
    credit_limit        DECIMAL(12,2),
    
    -- SCD Type 2 fields
    effective_date      DATE NOT NULL,              -- Fecha de inicio de vigencia
    end_date            DATE,                       -- NULL = registro actual
    is_current          BOOLEAN NOT NULL DEFAULT TRUE,  -- Flag para registro actual
    
    -- Audit fields
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by          VARCHAR(50) DEFAULT 'system',
    
    -- Constraints
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date >= effective_date)
);

-- Indexes para performance
CREATE INDEX idx_dim_customer_natural ON dim_customer(customer_id);
CREATE INDEX idx_dim_customer_current ON dim_customer(is_current) WHERE is_current = TRUE;
CREATE INDEX idx_dim_customer_dates ON dim_customer(effective_date, end_date);

-- ----------------------------------------------------------------------------
-- dim_product: Dimensión de productos (SCD Type 1)
-- ----------------------------------------------------------------------------
-- SCD Type 1: Sobrescribe cambios (no mantiene historial)
-- Usar cuando el historial no es importante (ej: correción de typos)

CREATE TABLE dim_product (
    product_key         BIGSERIAL PRIMARY KEY,
    product_id          VARCHAR(50) NOT NULL UNIQUE,  -- Natural key
    product_name        VARCHAR(200) NOT NULL,
    product_description TEXT,
    category            VARCHAR(100),
    subcategory         VARCHAR(100),
    brand               VARCHAR(100),
    unit_price          DECIMAL(10,2),
    cost                DECIMAL(10,2),
    weight_kg           DECIMAL(8,2),
    is_active           BOOLEAN DEFAULT TRUE,
    
    -- Audit
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dim_product_category ON dim_product(category, subcategory);
CREATE INDEX idx_dim_product_active ON dim_product(is_active) WHERE is_active = TRUE;

-- ----------------------------------------------------------------------------
-- dim_date: Dimensión de fechas (tabla de calendario)
-- ----------------------------------------------------------------------------
-- Pre-populated table con todas las fechas necesarias
-- Facilita agregaciones por períodos (semana, mes, trimestre, año)

CREATE TABLE dim_date (
    date_key            INTEGER PRIMARY KEY,        -- YYYYMMDD format (ej: 20240115)
    full_date           DATE NOT NULL UNIQUE,
    day_of_week         INTEGER,                    -- 1-7 (1=Sunday)
    day_name            VARCHAR(10),                -- 'Monday', 'Tuesday', ...
    day_of_month        INTEGER,
    day_of_year         INTEGER,
    week_of_year        INTEGER,
    month               INTEGER,
    month_name          VARCHAR(10),                -- 'January', 'February', ...
    quarter             INTEGER,                    -- 1, 2, 3, 4
    year                INTEGER,
    is_weekend          BOOLEAN,
    is_holiday          BOOLEAN DEFAULT FALSE,
    holiday_name        VARCHAR(100),
    
    -- Fiscal calendar (si aplica)
    fiscal_year         INTEGER,
    fiscal_quarter      INTEGER,
    fiscal_month        INTEGER
);

CREATE INDEX idx_dim_date_full ON dim_date(full_date);
CREATE INDEX idx_dim_date_year_month ON dim_date(year, month);

-- ----------------------------------------------------------------------------
-- dim_location: Dimensión de ubicaciones
-- ----------------------------------------------------------------------------

CREATE TABLE dim_location (
    location_key        BIGSERIAL PRIMARY KEY,
    location_id         VARCHAR(50) NOT NULL UNIQUE,
    store_name          VARCHAR(200),
    address             VARCHAR(500),
    city                VARCHAR(100),
    state               VARCHAR(50),
    country             VARCHAR(50),
    postal_code         VARCHAR(20),
    region              VARCHAR(50),                -- 'North', 'South', 'East', 'West'
    timezone            VARCHAR(50),
    latitude            DECIMAL(10,6),
    longitude           DECIMAL(10,6),
    is_active           BOOLEAN DEFAULT TRUE,
    
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dim_location_region ON dim_location(region);
CREATE INDEX idx_dim_location_country_city ON dim_location(country, city);

-- ============================================================================
-- FACT TABLES (Transactional Data)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- fact_sales: Tabla de hechos de ventas
-- ----------------------------------------------------------------------------
-- Contiene métricas numéricas y foreign keys a dimensiones
-- Particionada por fecha para performance

CREATE TABLE fact_sales (
    sales_key           BIGSERIAL,                  -- Surrogate key (opcional)
    transaction_id      VARCHAR(100) NOT NULL,      -- Business key
    
    -- Foreign keys a dimensiones (usar surrogate keys!)
    date_key            INTEGER NOT NULL,
    customer_key        BIGINT NOT NULL,
    product_key         BIGINT NOT NULL,
    location_key        BIGINT NOT NULL,
    
    -- Métricas (measures)
    quantity            INTEGER NOT NULL,
    unit_price          DECIMAL(10,2) NOT NULL,
    discount_amount     DECIMAL(10,2) DEFAULT 0,
    tax_amount          DECIMAL(10,2) DEFAULT 0,
    total_amount        DECIMAL(12,2) NOT NULL,     -- Calculated: quantity * unit_price - discount + tax
    cost_amount         DECIMAL(12,2),              -- Para cálculo de profit
    profit_amount       DECIMAL(12,2),              -- total_amount - cost_amount
    
    -- Degenerate dimensions (atributos transaccionales sin tabla propia)
    order_number        VARCHAR(50),
    payment_method      VARCHAR(50),
    shipping_method     VARCHAR(50),
    
    -- Audit
    loaded_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraints
    CONSTRAINT pk_fact_sales PRIMARY KEY (sales_key, date_key),  -- Composite key con partition column
    CONSTRAINT fk_sales_date FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_sales_customer FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    CONSTRAINT fk_sales_product FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    CONSTRAINT fk_sales_location FOREIGN KEY (location_key) REFERENCES dim_location(location_key),
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT chk_total CHECK (total_amount >= 0)
) PARTITION BY RANGE (date_key);  -- Particionado por fecha (PostgreSQL 10+)

-- Crear particiones por año (ejemplo para 2024)
CREATE TABLE fact_sales_2024 PARTITION OF fact_sales
    FOR VALUES FROM (20240101) TO (20250101);

CREATE TABLE fact_sales_2025 PARTITION OF fact_sales
    FOR VALUES FROM (20250101) TO (20260101);

-- Indexes para performance
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_transaction ON fact_sales(transaction_id);

-- ----------------------------------------------------------------------------
-- fact_inventory: Snapshot fact table (inventario diario)
-- ----------------------------------------------------------------------------
-- Fact table periódica que captura estado en un momento específico

CREATE TABLE fact_inventory (
    inventory_key       BIGSERIAL PRIMARY KEY,
    date_key            INTEGER NOT NULL,
    product_key         BIGINT NOT NULL,
    location_key        BIGINT NOT NULL,
    
    -- Métricas
    quantity_on_hand    INTEGER NOT NULL,
    quantity_reserved   INTEGER DEFAULT 0,
    quantity_available  INTEGER,                    -- on_hand - reserved
    reorder_point       INTEGER,
    reorder_quantity    INTEGER,
    unit_cost           DECIMAL(10,2),
    total_value         DECIMAL(12,2),              -- quantity_on_hand * unit_cost
    
    snapshot_date       DATE NOT NULL,
    loaded_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_inventory_date FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_inventory_product FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    CONSTRAINT fk_inventory_location FOREIGN KEY (location_key) REFERENCES dim_location(location_key),
    CONSTRAINT uq_inventory_snapshot UNIQUE (date_key, product_key, location_key)
);

CREATE INDEX idx_fact_inventory_date ON fact_inventory(date_key);
CREATE INDEX idx_fact_inventory_product ON fact_inventory(product_key);

-- ============================================================================
-- AGGREGATE TABLES (Pre-calculated summaries para performance)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- agg_sales_daily: Agregación diaria de ventas
-- ----------------------------------------------------------------------------
-- Mejora performance de queries frecuentes

CREATE TABLE agg_sales_daily (
    date_key            INTEGER NOT NULL,
    product_key         BIGINT NOT NULL,
    location_key        BIGINT NOT NULL,
    
    -- Métricas agregadas
    total_transactions  INTEGER,
    total_quantity      INTEGER,
    total_revenue       DECIMAL(12,2),
    total_cost          DECIMAL(12,2),
    total_profit        DECIMAL(12,2),
    avg_transaction_value DECIMAL(10,2),
    
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (date_key, product_key, location_key),
    CONSTRAINT fk_agg_daily_date FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_agg_daily_product FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    CONSTRAINT fk_agg_daily_location FOREIGN KEY (location_key) REFERENCES dim_location(location_key)
);

-- ============================================================================
-- STAGING TABLES (Raw data landing zone)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- stg_sales_raw: Tabla de staging para carga inicial
-- ----------------------------------------------------------------------------
-- Sin constraints para permitir carga rápida
-- Después se limpia y carga a fact table

CREATE TABLE stg_sales_raw (
    transaction_id      VARCHAR(100),
    transaction_date    VARCHAR(50),               -- String (todavía no parseado)
    customer_id         VARCHAR(50),
    product_id          VARCHAR(50),
    location_id         VARCHAR(50),
    quantity            VARCHAR(20),
    unit_price          VARCHAR(20),
    discount            VARCHAR(20),
    
    -- Audit
    file_name           VARCHAR(200),              -- Origen del archivo
    loaded_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed           BOOLEAN DEFAULT FALSE
);

-- ============================================================================
-- VIEWS (Queries pre-defined para acceso fácil)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- v_sales_current_month: Vista de ventas del mes actual
-- ----------------------------------------------------------------------------

CREATE OR REPLACE VIEW v_sales_current_month AS
SELECT 
    d.full_date,
    c.customer_name,
    p.product_name,
    l.store_name,
    f.quantity,
    f.total_amount,
    f.profit_amount
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_customer c ON f.customer_key = c.customer_key
JOIN dim_product p ON f.product_key = p.product_key
JOIN dim_location l ON f.location_key = l.location_key
WHERE d.year = EXTRACT(YEAR FROM CURRENT_DATE)
  AND d.month = EXTRACT(MONTH FROM CURRENT_DATE)
  AND c.is_current = TRUE;

-- ----------------------------------------------------------------------------
-- v_top_products: Vista de productos top por revenue
-- ----------------------------------------------------------------------------

CREATE OR REPLACE VIEW v_top_products AS
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    SUM(f.quantity) as total_quantity_sold,
    SUM(f.total_amount) as total_revenue,
    SUM(f.profit_amount) as total_profit,
    COUNT(DISTINCT f.transaction_id) as num_transactions
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
WHERE p.is_active = TRUE
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC;

-- ============================================================================
-- PARETO 20% - DDL Best Practices
-- ============================================================================
--
-- 1. SURROGATE KEYS:
--    - Usar BIGSERIAL para dimension keys
--    - Nunca exponer business keys como PK
--    - Permite cambios en natural keys sin afectar fact tables
--
-- 2. NAMING CONVENTIONS:
--    - dim_*: dimension tables
--    - fact_*: fact tables
--    - agg_*: aggregate tables
--    - stg_*: staging tables
--    - v_*: views
--
-- 3. DATA TYPES:
--    - VARCHAR(n): usar tamaño realista (no 255 por default)
--    - DECIMAL(p,s): para montos (no FLOAT!)
--    - TIMESTAMP: para audit fields
--    - BOOLEAN: para flags
--
-- 4. CONSTRAINTS:
--    - PRIMARY KEY: siempre definir
--    - FOREIGN KEY: para integridad referencial
--    - CHECK: para validaciones de negocio
--    - UNIQUE: cuando aplique
--    - NOT NULL: ser explícito
--
-- 5. INDEXES:
--    - Columnas en WHERE clauses frecuentes
--    - Foreign keys
--    - Columnas de JOIN
--    - Evitar sobre-indexar (costo en writes)
--
-- 6. PARTITIONING:
--    - Por fecha (más común)
--    - Mejora performance de queries y mantenimiento
--    - PostgreSQL 10+: PARTITION BY RANGE
--
-- 7. AUDIT FIELDS:
--    - created_at, updated_at: timestamps
--    - created_by, updated_by: user tracking
--    - Facilitan troubleshooting
--
-- 8. SCD (Slowly Changing Dimensions):
--    - Type 1: Overwrite (sin historial)
--    - Type 2: Historial completo (effective_date, end_date)
--    - Type 3: Columnas "previous" (raramente usado)
--
-- NEXT STEPS:
--    1. Ejecutar estos DDLs en PostgreSQL
--    2. Poblar dim_date con script (ver recursos)
--    3. Cargar datos de prueba en staging
--    4. Implementar MERGE para SCD Type 2
-- ============================================================================
