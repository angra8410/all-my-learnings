# Módulo 01: Introducción y Setup del Entorno

## 🎯 Objetivos del Módulo

Al finalizar este módulo serás capaz de:

1. Configurar tu entorno de desarrollo completo para Blockchain y Web3
2. Instalar y configurar Node.js, Hardhat, Docker y herramientas esenciales
3. Crear tu primer proyecto Hardhat
4. Ejecutar un nodo local de Ethereum
5. Desplegar tu primer Smart Contract
6. Comprender la arquitectura básica de Web3

**Duración estimada**: 2-3 horas

## 🚀 ¿Por Qué es Importante?

Un entorno bien configurado es la base para todo tu aprendizaje. Este módulo te ahorra horas de frustración estableciendo las herramientas correctas desde el inicio. Cada herramienta tiene un propósito específico en el ecosistema Web3.

## 🛠️ Stack Tecnológico

- **Node.js** (v18+): Runtime de JavaScript
- **Hardhat**: Framework de desarrollo para Ethereum
- **Solidity**: Lenguaje para Smart Contracts
- **Ethers.js**: Librería para interactuar con Ethereum
- **Docker**: Contenerización para desarrollo reproducible
- **MetaMask**: Wallet para desarrollo y testing
- **Git**: Control de versiones

## 📦 Instalación Paso a Paso

### Paso 1: Verificar Node.js (10 min)

```bash
# Verificar versión de Node.js (debe ser 18+)
node --version

# Si no tienes Node.js, instálalo desde https://nodejs.org/
# O usa nvm (recomendado):
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

### Paso 2: Instalar Hardhat Globalmente (5 min)

```bash
# Crear carpeta para tu primer proyecto
mkdir mi-primer-proyecto-web3
cd mi-primer-proyecto-web3

# Inicializar proyecto Node.js
npm init -y

# Instalar Hardhat
npm install --save-dev hardhat

# Inicializar proyecto Hardhat
npx hardhat
```

**Selecciona**: "Create a JavaScript project" y acepta todas las opciones por defecto.

### Paso 3: Instalar Dependencias Esenciales (5 min)

```bash
# Instalar librerías necesarias
npm install --save-dev @nomicfoundation/hardhat-toolbox
npm install --save-dev @nomicfoundation/hardhat-ethers ethers
npm install dotenv
```

### Paso 4: Configurar Docker (15 min)

**Dockerfile para desarrollo**:
```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

# Instalar dependencias del sistema
RUN apk add --no-cache git python3 make g++

# Copiar package files
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar código fuente
COPY . .

# Exponer puerto para nodo local
EXPOSE 8545

# Comando por defecto: iniciar nodo Hardhat
CMD ["npx", "hardhat", "node"]
```

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  hardhat-node:
    build: .
    ports:
      - "8545:8545"
    volumes:
      - ./contracts:/app/contracts
      - ./scripts:/app/scripts
      - ./test:/app/test
    networks:
      - web3-network

  frontend:
    image: node:18-alpine
    working_dir: /app
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    command: npm run dev
    networks:
      - web3-network
    depends_on:
      - hardhat-node

networks:
  web3-network:
    driver: bridge
```

### Paso 5: Tu Primer Smart Contract (15 min)

Crea el archivo `contracts/HelloBlockchain.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract HelloBlockchain {
    string public message;
    address public owner;
    uint256 public messageCount;

    event MessageUpdated(string newMessage, address updatedBy);

    constructor(string memory _initialMessage) {
        message = _initialMessage;
        owner = msg.sender;
        messageCount = 0;
    }

    function setMessage(string memory _newMessage) public {
        message = _newMessage;
        messageCount++;
        emit MessageUpdated(_newMessage, msg.sender);
    }

    function getMessage() public view returns (string memory) {
        return message;
    }

    function getMessageCount() public view returns (uint256) {
        return messageCount;
    }
}
```

### Paso 6: Script de Despliegue (10 min)

Crea el archivo `scripts/deploy.js`:

```javascript
const hre = require("hardhat");

async function main() {
  console.log("🚀 Desplegando HelloBlockchain...");

  // Obtener el contrato
  const HelloBlockchain = await hre.ethers.getContractFactory("HelloBlockchain");
  
  // Desplegar con mensaje inicial
  const hello = await HelloBlockchain.deploy("¡Hola Blockchain!");
  
  await hello.waitForDeployment();

  const address = await hello.getAddress();
  console.log("✅ HelloBlockchain desplegado en:", address);
  
  // Verificar el mensaje
  const message = await hello.getMessage();
  console.log("📝 Mensaje inicial:", message);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

### Paso 7: Compilar y Desplegar (10 min)

```bash
# Compilar el contrato
npx hardhat compile

# Iniciar nodo local (en una terminal separada)
npx hardhat node

# Desplegar en nodo local (en otra terminal)
npx hardhat run scripts/deploy.js --network localhost
```

### Paso 8: Configurar Hardhat (hardhat.config.js)

```javascript
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    hardhat: {
      chainId: 31337
    },
    localhost: {
      url: "http://127.0.0.1:8545",
      chainId: 31337
    }
  },
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  }
};
```

### Paso 9: Instalar MetaMask (10 min)

1. Instala la extensión MetaMask en tu navegador
2. Crea una nueva wallet (guarda tu frase secreta en un lugar seguro)
3. Agrega red local:
   - Network Name: Localhost 8545
   - RPC URL: http://localhost:8545
   - Chain ID: 31337
   - Currency Symbol: ETH

4. Importa una cuenta de Hardhat:
   - Copia una clave privada de las cuentas de prueba de Hardhat
   - Importa en MetaMask

## 🎯 Script de Interacción Completo

Crea `scripts/interact.js`:

```javascript
const hre = require("hardhat");

async function main() {
  // Dirección del contrato desplegado (reemplaza con la tuya)
  const contractAddress = "TU_DIRECCION_AQUI";
  
  // Obtener el contrato desplegado
  const HelloBlockchain = await hre.ethers.getContractFactory("HelloBlockchain");
  const hello = HelloBlockchain.attach(contractAddress);

  console.log("📖 Leyendo mensaje actual...");
  const currentMessage = await hello.getMessage();
  console.log("Mensaje:", currentMessage);

  console.log("\n✍️  Actualizando mensaje...");
  const tx = await hello.setMessage("¡Blockchain es increíble!");
  await tx.wait();
  console.log("✅ Mensaje actualizado!");

  console.log("\n📖 Leyendo nuevo mensaje...");
  const newMessage = await hello.getMessage();
  console.log("Nuevo mensaje:", newMessage);

  const count = await hello.getMessageCount();
  console.log("📊 Número de actualizaciones:", count.toString());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

## 📝 Estructura del Proyecto

```
mi-primer-proyecto-web3/
├── contracts/
│   └── HelloBlockchain.sol
├── scripts/
│   ├── deploy.js
│   └── interact.js
├── test/
│   └── HelloBlockchain.test.js
├── hardhat.config.js
├── package.json
├── Dockerfile
└── docker-compose.yml
```

## 🧪 Test Básico

Crea `test/HelloBlockchain.test.js`:

```javascript
const { expect } = require("chai");

describe("HelloBlockchain", function () {
  let hello;
  let owner;
  let addr1;

  beforeEach(async function () {
    [owner, addr1] = await ethers.getSigners();
    const HelloBlockchain = await ethers.getContractFactory("HelloBlockchain");
    hello = await HelloBlockchain.deploy("Mensaje inicial");
    await hello.waitForDeployment();
  });

  it("Debe establecer el mensaje inicial correctamente", async function () {
    expect(await hello.getMessage()).to.equal("Mensaje inicial");
  });

  it("Debe actualizar el mensaje correctamente", async function () {
    await hello.setMessage("Nuevo mensaje");
    expect(await hello.getMessage()).to.equal("Nuevo mensaje");
  });

  it("Debe incrementar el contador de mensajes", async function () {
    await hello.setMessage("Mensaje 1");
    await hello.setMessage("Mensaje 2");
    expect(await hello.getMessageCount()).to.equal(2);
  });
});
```

**Ejecutar tests**:
```bash
npx hardhat test
```

## 🐳 Usando Docker

```bash
# Construir imagen
docker-compose build

# Iniciar nodo Hardhat en container
docker-compose up hardhat-node

# En otra terminal, desplegar
docker-compose exec hardhat-node npx hardhat run scripts/deploy.js --network localhost
```

## 🔧 Comandos Útiles de Hardhat

```bash
# Compilar contratos
npx hardhat compile

# Limpiar artefactos
npx hardhat clean

# Iniciar nodo local
npx hardhat node

# Ejecutar tests
npx hardhat test

# Ver cuentas de desarrollo
npx hardhat accounts

# Obtener ayuda
npx hardhat help
```

## 📊 Verificación de Setup

Marca lo que has completado:
- [ ] Node.js 18+ instalado
- [ ] Hardhat instalado y configurado
- [ ] Proyecto inicializado
- [ ] Smart contract compilado
- [ ] Nodo local ejecutándose
- [ ] Contrato desplegado localmente
- [ ] Tests ejecutados exitosamente
- [ ] MetaMask configurado
- [ ] Docker instalado y funcional
- [ ] docker-compose ejecutando correctamente

## 🎓 Conceptos Clave

### Hardhat
Framework de desarrollo que proporciona:
- Compilador de Solidity
- Nodo local de Ethereum
- Herramientas de testing
- Scripts de despliegue
- Debugging avanzado

### Red Local vs Testnet vs Mainnet
- **Local**: Desarrollo rápido, sin costos
- **Testnet**: Testing en red pública sin valor real
- **Mainnet**: Red principal de Ethereum con ETH real

### Gas y Transacciones
Cada operación en blockchain consume "gas":
- Lectura (view/pure): Gratis
- Escritura: Cuesta gas
- Despliegue: Mayor costo de gas

## 💡 Mejores Prácticas

1. **Siempre usa control de versiones (Git)**
2. **Nunca commitees claves privadas**
3. **Usa .env para configuraciones sensibles**
4. **Mantén Hardhat actualizado**
5. **Escribe tests antes de desplegar**

## 🚀 Siguiente Paso

Una vez completado este módulo, continúa con el **Módulo 02: Fundamentos de Criptografía** donde aprenderás sobre hashing, firmas digitales y criptografía asimétrica.

## 📚 Recursos Adicionales

- [Documentación de Hardhat](https://hardhat.org/docs)
- [Solidity Docs](https://docs.soliditylang.org/)
- [Ethers.js Docs](https://docs.ethers.org/)
- [MetaMask Docs](https://docs.metamask.io/)

---

**¡Felicidades! 🎉** Has configurado tu entorno de desarrollo completo para Web3. Ahora estás listo para construir aplicaciones descentralizadas.
