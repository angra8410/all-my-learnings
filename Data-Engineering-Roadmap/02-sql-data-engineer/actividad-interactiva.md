# Actividad interactiva — SQL (respuestas incluidas)

Ejercicio 1:
- Descripción: Obtener los 5 clientes con mayor facturación en 2024.
- SQL sugerido:
SELECT cliente_id, SUM(total) AS total_cliente
FROM ventas
WHERE fecha BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY cliente_id
ORDER BY total_cliente DESC
LIMIT 5;

Ejercicio 2:
- Descripción: Calcular la diferencia entre pedidos por día y su media móvil 7 días.
- Pista: usar window functions con AVG() OVER (ORDER BY fecha ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)