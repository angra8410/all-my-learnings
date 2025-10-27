# Módulo 02: Fundamentos de Criptografía

## 🎯 Objetivos del Módulo

Al finalizar este módulo serás capaz de:

1. Comprender conceptos fundamentales de criptografía aplicados a blockchain
2. Usar funciones hash (SHA-256, Keccak-256) en JavaScript y Solidity
3. Generar y verificar firmas digitales
4. Implementar criptografía asimétrica (claves públicas/privadas)
5. Crear un sistema básico de proof-of-work
6. Entender cómo funcionan las wallets y direcciones Ethereum

**Duración estimada**: 3-4 horas

## 🔐 ¿Por Qué Criptografía en Blockchain?

La criptografía es el corazón de blockchain. Sin ella:
- No habría seguridad en las transacciones
- No podrían verificarse identidades
- No existirían las wallets
- No habría inmutabilidad de datos

## 📚 Conceptos Principales

### 1. Funciones Hash

Una función hash es una función matemática que:
- Toma input de cualquier tamaño
- Produce output de tamaño fijo
- Es determinística (mismo input → mismo output)
- Es unidireccional (irreversible)
- Pequeños cambios en input → output completamente diferente

**Ejemplo en JavaScript**:
```javascript
const crypto = require('crypto');

function sha256(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

console.log(sha256('Hello'));
// a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

console.log(sha256('hello'));
// 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

// Cambio mínimo = hash completamente diferente
```

**Ejemplo en Solidity**:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract HashExample {
    function hashString(string memory _text) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(_text));
    }

    function hashMultiple(string memory _a, uint256 _b) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(_a, _b));
    }

    function hashAddress(address _addr) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(_addr));
    }
}
```

### 2. Criptografía Asimétrica

Sistema de dos claves:
- **Clave privada**: Secreta, solo tú la conoces
- **Clave pública**: Derivada de la privada, compartible

**Propiedades**:
- Lo que se encripta con una clave, se desencripta con la otra
- Imposible derivar la privada desde la pública (matemáticamente)

**Ejemplo con ethers.js**:
```javascript
const { ethers } = require('ethers');

// Generar wallet (par de claves)
const wallet = ethers.Wallet.createRandom();

console.log('Clave privada:', wallet.privateKey);
console.log('Clave pública:', wallet.publicKey);
console.log('Dirección:', wallet.address);

// La dirección es el hash de la clave pública
// Dirección = últimos 20 bytes de keccak256(publicKey)
```

### 3. Firmas Digitales

Permiten:
- Probar que tú creaste un mensaje
- Garantizar que el mensaje no fue alterado
- No repudio (no puedes negar que firmaste)

**Flujo**:
1. Hash del mensaje
2. Firma del hash con clave privada
3. Cualquiera puede verificar con tu clave pública

**Ejemplo completo**:
```javascript
const { ethers } = require('ethers');

async function firmarYVerificar() {
  // Crear wallet
  const wallet = ethers.Wallet.createRandom();
  
  // Mensaje a firmar
  const message = "Transfiero 10 ETH a Alice";
  
  // Firmar
  const signature = await wallet.signMessage(message);
  console.log('Firma:', signature);
  
  // Verificar
  const recoveredAddress = ethers.verifyMessage(message, signature);
  console.log('Dirección recuperada:', recoveredAddress);
  console.log('¿Coincide?:', recoveredAddress === wallet.address);
  
  // Si alguien modifica el mensaje, la verificación falla
  const tamperedMessage = "Transfiero 100 ETH a Alice";
  const recoveredFromTampered = ethers.verifyMessage(tamperedMessage, signature);
  console.log('¿Firma válida para mensaje alterado?:', 
              recoveredFromTampered === wallet.address); // false
}

firmarYVerificar();
```

### 4. Merkle Trees

Estructura de datos que permite verificar eficientemente la pertenencia:

```javascript
const crypto = require('crypto');

function hash(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

class MerkleTree {
  constructor(leaves) {
    this.leaves = leaves.map(leaf => hash(leaf));
    this.tree = this.buildTree(this.leaves);
  }

  buildTree(leaves) {
    if (leaves.length === 1) return leaves;
    
    const parentLayer = [];
    for (let i = 0; i < leaves.length; i += 2) {
      const left = leaves[i];
      const right = leaves[i + 1] || left;
      parentLayer.push(hash(left + right));
    }
    
    return [leaves, ...this.buildTree(parentLayer)];
  }

  getRoot() {
    return this.tree[this.tree.length - 1][0];
  }

  getProof(leaf) {
    let index = this.leaves.indexOf(hash(leaf));
    const proof = [];
    
    for (let layer of this.tree) {
      if (layer.length === 1) break;
      
      const isLeft = index % 2 === 0;
      const siblingIndex = isLeft ? index + 1 : index - 1;
      
      if (siblingIndex < layer.length) {
        proof.push({
          hash: layer[siblingIndex],
          isLeft: !isLeft
        });
      }
      
      index = Math.floor(index / 2);
    }
    
    return proof;
  }
}

// Uso
const transactions = ['tx1', 'tx2', 'tx3', 'tx4'];
const tree = new MerkleTree(transactions);
console.log('Merkle Root:', tree.getRoot());
console.log('Proof para tx2:', tree.getProof('tx2'));
```

## 🎨 Proyecto Práctico: Sistema de Verificación

**Contrato VerificationSystem.sol**:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract VerificationSystem {
    // Mapeo de hashes de documentos verificados
    mapping(bytes32 => bool) public verifiedDocuments;
    mapping(bytes32 => address) public documentOwner;
    mapping(bytes32 => uint256) public documentTimestamp;

    event DocumentVerified(bytes32 indexed documentHash, address indexed owner, uint256 timestamp);

    function verifyDocument(string memory _document) public returns (bytes32) {
        bytes32 docHash = keccak256(abi.encodePacked(_document));
        
        require(!verifiedDocuments[docHash], "Documento ya verificado");
        
        verifiedDocuments[docHash] = true;
        documentOwner[docHash] = msg.sender;
        documentTimestamp[docHash] = block.timestamp;
        
        emit DocumentVerified(docHash, msg.sender, block.timestamp);
        
        return docHash;
    }

    function checkDocument(string memory _document) public view returns (
        bool verified,
        address owner,
        uint256 timestamp
    ) {
        bytes32 docHash = keccak256(abi.encodePacked(_document));
        return (
            verifiedDocuments[docHash],
            documentOwner[docHash],
            documentTimestamp[docHash]
        );
    }

    function isDocumentVerified(bytes32 _docHash) public view returns (bool) {
        return verifiedDocuments[_docHash];
    }
}
```

## 🧪 Proof of Work Simplificado

```javascript
const crypto = require('crypto');

function sha256(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

function mineBlock(data, difficulty) {
  let nonce = 0;
  const target = '0'.repeat(difficulty);
  
  console.log(`Mining con dificultad ${difficulty}...`);
  const startTime = Date.now();
  
  while (true) {
    const hash = sha256(data + nonce);
    
    if (hash.startsWith(target)) {
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);
      console.log(`✅ Bloque minado!`);
      console.log(`   Nonce: ${nonce}`);
      console.log(`   Hash: ${hash}`);
      console.log(`   Tiempo: ${elapsed}s`);
      return { nonce, hash, time: elapsed };
    }
    
    nonce++;
    
    if (nonce % 100000 === 0) {
      process.stdout.write(`\r   Intentos: ${nonce.toLocaleString()}`);
    }
  }
}

// Prueba con diferentes dificultades
console.log('\n=== Proof of Work Demo ===\n');
mineBlock('Bloque Genesis', 2);
console.log('\n');
mineBlock('Bloque 1', 3);
console.log('\n');
mineBlock('Bloque 2', 4);
```

## 🔑 Generación de Wallets

```javascript
const { ethers } = require('ethers');

function createWallet() {
  // Método 1: Wallet aleatorio
  const randomWallet = ethers.Wallet.createRandom();
  
  console.log('=== Wallet Aleatorio ===');
  console.log('Mnemonic:', randomWallet.mnemonic.phrase);
  console.log('Private Key:', randomWallet.privateKey);
  console.log('Public Key:', randomWallet.publicKey);
  console.log('Address:', randomWallet.address);
  
  // Método 2: Desde private key
  const privateKey = '0x' + crypto.randomBytes(32).toString('hex');
  const walletFromPK = new ethers.Wallet(privateKey);
  
  console.log('\n=== Wallet desde Private Key ===');
  console.log('Address:', walletFromPK.address);
  
  // Método 3: Desde mnemonic
  const mnemonic = ethers.Wallet.createRandom().mnemonic.phrase;
  const walletFromMnemonic = ethers.Wallet.fromPhrase(mnemonic);
  
  console.log('\n=== Wallet desde Mnemonic ===');
  console.log('Mnemonic:', mnemonic);
  console.log('Address:', walletFromMnemonic.address);
  
  // Derivar múltiples wallets desde un mnemonic (HD Wallets)
  console.log('\n=== HD Wallet (múltiples direcciones) ===');
  for (let i = 0; i < 5; i++) {
    const path = `m/44'/60'/0'/0/${i}`;
    const hdWallet = ethers.HDNodeWallet.fromPhrase(mnemonic, path);
    console.log(`Address ${i}:`, hdWallet.address);
  }
}

createWallet();
```

## 📊 Resumen de Algoritmos Crypto

| Algoritmo | Uso en Blockchain | Propósito |
|-----------|-------------------|-----------|
| SHA-256 | Bitcoin mining | Hashing general |
| Keccak-256 | Ethereum | Hashing en EVM |
| ECDSA | Firmas | Firmas digitales |
| secp256k1 | Bitcoin/Ethereum | Curva elíptica para claves |
| RIPEMD-160 | Direcciones Bitcoin | Crear direcciones |

## 🎯 Ejercicios Prácticos

Ver **actividad-interactiva.md** para ejercicios detallados que incluyen:
- Implementar funciones hash
- Crear y verificar firmas
- Construir Merkle Tree
- Sistema de proof-of-work
- Generación de wallets

## 📚 Recursos Adicionales

- [Cryptographic Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Elliptic Curve Cryptography](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [Merkle Trees Explained](https://brilliant.org/wiki/merkle-tree/)
- [Digital Signatures](https://www.ssl.com/article/how-do-digital-signatures-work/)

---

**¡Siguiente paso!** Continúa con el **Módulo 03: Solidity y Smart Contracts** para aplicar estos conceptos en contratos reales.
