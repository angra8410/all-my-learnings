# Actividades Interactivas - Módulo 03: Solidity y Smart Contracts

## Ejercicio 1: Tipos de Datos y Variables (30 min)

Crea un contrato `DatosBasicos.sol` que incluya:
- Variables de cada tipo (uint, int, bool, address, string, bytes)
- Arrays dinámicos y fijos
- Mappings
- Structs
- Enums

**Tareas**:
- [ ] Compilar sin errores
- [ ] Desplegar en red local
- [ ] Leer/escribir cada tipo de variable
- [ ] Probar arrays y mappings

## Ejercicio 2: Token ERC-20 Completo (45 min)

Implementa el token ERC-20 del README:
- [ ] Copiar código del README
- [ ] Compilar y desplegar
- [ ] Hacer 5 transferencias
- [ ] Probar approve y transferFrom
- [ ] Probar mint y burn

## Ejercicio 3: Implementar Ownable (25 min)

Crea contrato que herede de Ownable:
- [ ] Implementar Ownable pattern
- [ ] Crear función que solo owner puede ejecutar
- [ ] Transferir ownership
- [ ] Validar que funciona

## Ejercicio 4: Implementar Pausable (25 min)

Extiende tu token para ser pausable:
- [ ] Heredar de Pausable
- [ ] Pausar transferencias cuando pausado
- [ ] Probar pausar/despausar
- [ ] Validar que solo owner puede pausar

## Ejercicio 5: Tests Comprehensivos (40 min)

Escribe tests para tu token:
- [ ] Mínimo 10 casos de test
- [ ] Cubrir deployment
- [ ] Cubrir transferencias
- [ ] Cubrir allowances
- [ ] Cubrir casos de error

## Ejercicio 6: Optimización de Gas (30 min)

Compara gas entre diferentes implementaciones:
- [ ] Medir gas de loops
- [ ] Probar memory vs calldata
- [ ] Optimizar un contrato
- [ ] Comparar antes/después

**Tiempo total**: 3-4 horas
