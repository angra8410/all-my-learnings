# Módulo 07: Oracles, IPFS y Almacenamiento

## 🎯 Objetivos del Módulo

Este módulo te enseñará conceptos y prácticas avanzadas de Oracles, IPFS y Almacenamiento en el contexto de Blockchain y Web3.

**Duración estimada**: 3-5 horas

## 📚 Contenido Principal

Ver `actividad-interactiva.md` para ejercicios prácticos accionables con código listo para copiar/pegar.

## 🔧 Ejemplos Prácticos

Todos los ejemplos incluyen:
- Código Solidity cuando aplique
- JavaScript/TypeScript para interacción
- Docker/docker-compose snippets donde sea relevante
- FastAPI examples para módulos de AI
- Tests y validaciones

## 💡 Conceptos Clave

- Concepto 1: Explicación práctica
- Concepto 2: Código ejecutable
- Concepto 3: Ejemplos reales
- Concepto 4: Mejores prácticas

## 🚀 Quick Start

```bash
# Setup básico
npm install
# o pip install para módulos Python/AI

# Ejecutar ejemplos
npm run example
# o python main.py
```

## 📋 Checklist de Aprendizaje

- [ ] Completar ejercicios prácticos
- [ ] Ejecutar todos los ejemplos de código
- [ ] Pasar tests de validación
- [ ] Construir mini-proyecto del módulo

## 🔗 Recursos Adicionales

- Documentación oficial relevante
- Tutoriales complementarios
- Comunidades y soporte

---

**¡Importante!** Este es un curso 90% práctico. Asegúrate de ejecutar cada ejemplo y completar los ejercicios hands-on.

**Siguiente**: Módulo 08

## 🔗 Chainlink Price Feed Example

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceFeed {
    AggregatorV3Interface internal priceFeed;
    
    constructor() {
        // ETH/USD Sepolia testnet
        priceFeed = AggregatorV3Interface(
            0x694AA1769357215DE4FAC081bf1f309aDC325306
        );
    }
    
    function getLatestPrice() public view returns (int) {
        (,int price,,,) = priceFeed.latestRoundData();
        return price / 1e8;
    }
}
```

## 📦 IPFS Integration

```javascript
const { create } = require('ipfs-http-client');
const fs = require('fs');

const ipfs = create({ url: 'https://ipfs.infura.io:5001' });

async function uploadToIPFS(filePath) {
  const file = fs.readFileSync(filePath);
  const result = await ipfs.add(file);
  console.log('IPFS Hash:', result.path);
  return result.path;
}

async function retrieveFromIPFS(hash) {
  const chunks = [];
  for await (const chunk of ipfs.cat(hash)) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks).toString();
}
```

## 🖼️ NFT with IPFS Metadata

```solidity
contract IPFSNFuncionT is ERC721URIStorage {
    uint256 private _tokenIds;
    
    function mintNFT(address recipient, string memory ipfsHash) 
        public returns (uint256) {
        _tokenIds++;
        _safeMint(recipient, _tokenIds);
        _setTokenURI(_tokenIds, string(abi.encodePacked("ipfs://", ipfsHash)));
        return _tokenIds;
    }
}
```
