# Retroalimentación y Soluciones - Módulo 02: Fundamentos de Criptografía

## Conceptos Clave Dominados

### Funciones Hash
- ✅ Determinísticas: mismo input → mismo output
- ✅ Unidireccionales: imposible revertir
- ✅ Avalanche effect: cambio mínimo → hash diferente
- ✅ SHA-256 vs Keccak-256

### Criptografía Asimétrica
- ✅ Clave privada: secreta, genera firmas
- ✅ Clave pública: compartible, verifica firmas
- ✅ Dirección: derivada de clave pública

### Firmas Digitales
- ✅ Autenticidad: prueba quién firmó
- ✅ Integridad: detecta alteraciones
- ✅ No repudio: no se puede negar

## Soluciones a Ejercicios

### Ejercicio 1: Hashing
El hash debe ser determinístico. 'Hello Blockchain' siempre produce el mismo hash.
Cambiar una letra produce hash completamente diferente.

### Ejercicio 2: Firmas
La firma solo es válida si mensaje no cambia. Alterar el mensaje invalida la firma.

### Ejercicio 3: Merkle Tree
El root hash representa todo el árbol. Con el proof puedes verificar pertenencia sin revelar todo.

### Ejercicio 4-6
Ver soluciones completas en README.md

## Problemas Comunes

**"Firma no válida"**: Verifica que el mensaje sea exactamente igual.
**"Nonce muy alto"**: Normal en PoW, es el proceso de mining.

## Checklist Final
- [ ] Comprendo funciones hash
- [ ] Sé firmar y verificar
- [ ] Entiendo wallets y direcciones
- [ ] Implementé Merkle Tree
- [ ] Probé PoW

**Siguiente**: Módulo 03 - Solidity y Smart Contracts
