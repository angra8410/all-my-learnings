# Actividades Interactivas - Módulo 02: Fundamentos de Criptografía

## Ejercicio 1: Funciones Hash en JavaScript (20 min)

### Código para ejecutar
```javascript
const crypto = require('crypto');

function sha256(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

// Prueba estos ejemplos
console.log(sha256('Hello Blockchain'));
console.log(sha256('Hello blockchain')); // Nota la diferencia
console.log(sha256('Hello Blockchain')); // Igual al primero

// Ejercicio: Crea una función que mine un bloque simple
function mineBlock(data, difficulty) {
  let nonce = 0;
  const target = '0'.repeat(difficulty);
  
  while (true) {
    const hash = sha256(data + nonce);
    if (hash.startsWith(target)) {
      return { nonce, hash };
    }
    nonce++;
  }
}

console.log(mineBlock('Block 1', 3));
```

**Validación**: 
- [ ] Hash es determin.stico
- [ ] Cambios mínimos alteran completamente el hash
- [ ] Mining encuentra nonce correcto

## Ejercicio 2: Firmas Digitales (25 min)

```javascript
const { ethers } = require('ethers');

async function practicaFirmas() {
  const wallet = ethers.Wallet.createRandom();
  
  const mensaje = "Transfiero 5 ETH";
  const firma = await wallet.signMessage(mensaje);
  
  const addressRecuperada = ethers.verifyMessage(mensaje, firma);
  
  console.log('¿Firma válida?:', addressRecuperada === wallet.address);
}

practicaFirmas();
```

**Tareas**:
- [ ] Firmar 3 mensajes diferentes
- [ ] Verificar cada firma
- [ ] Intentar verificar con mensaje alterado

## Ejercicio 3: Merkle Tree Implementación (35 min)

Ver README.md para código base. Tareas:
- [ ] Crear árbol con 8 transacciones
- [ ] Obtener root hash
- [ ] Generar proof para transacción específica
- [ ] Verificar proof

## Ejercicio 4: Contrato de Verificación (30 min)

Desplegar VerificationSystem.sol:
- [ ] Compilar contrato
- [ ] Desplegar en red local
- [ ] Verificar 5 documentos diferentes
- [ ] Comprobar verificaciones

## Ejercicio 5: Generación de Wallets (20 min)

```javascript
const { ethers } = require('ethers');

// Genera 5 wallets y guarda sus datos
for (let i = 0; i < 5; i++) {
  const wallet = ethers.Wallet.createRandom();
  console.log(`Wallet ${i}:`, wallet.address);
}
```

Tareas:
- [ ] Generar wallets aleatorios
- [ ] Crear wallet desde mnemonic
- [ ] Derivar HD wallet (5 direcciones)

## Ejercicio 6: Proof of Work (25 min)

Ejecuta el código de PoW del README con dificultades 2, 3, 4, 5:
- [ ] Observa tiempo de mining
- [ ] Anota nonces encontrados
- [ ] Compara tiempos

**Tiempo total**: 2.5-3 horas
