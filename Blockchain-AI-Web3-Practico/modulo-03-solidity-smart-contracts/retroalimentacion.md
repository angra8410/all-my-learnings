# Retroalimentación - Módulo 03: Solidity y Smart Contracts

## Conceptos Clave

### Tipos de Datos
✅ uint256 es más gas-efficient que uint8 en muchos casos
✅ address payable puede recibir ETH
✅ mappings no se pueden iterar directamente

### Modificadores
✅ onlyOwner es el pattern más común
✅ whenNotPaused protege funciones
✅ Orden importa: checks, effects, interactions

### ERC-20
✅ Standard para tokens fungibles
✅ transfer, approve, transferFrom son core
✅ Eventos son esenciales

### Optimización
✅ ++i más barato que i++
✅ calldata más barato que memory
✅ Agrupar variables ahorra storage

## Soluciones

Ver código completo en README.md. Tests deben todos pasar.

## Problemas Comunes

**"Stack too deep"**: Demasiadas variables locales.
**Solución**: Usa structs o divide en funciones.

**"Gas estimation failed"**: require falló.
**Solución**: Revisa condiciones y balances.

## Checklist
- [ ] ERC-20 funcional
- [ ] Tests pasando (10+)
- [ ] Ownable implementado
- [ ] Pausable implementado
- [ ] Gas optimizado

**Siguiente**: Módulo 04 - Testing y Security
