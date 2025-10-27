# Actividades Interactivas - Módulo 01: Introducción y Setup

## 🎯 Objetivo

Completar la configuración del entorno y validar que todo funciona correctamente mediante ejercicios prácticos accionables.

---

## Ejercicio 1: Setup Completo del Entorno (30 min)

### Objetivo
Instalar y verificar todas las herramientas necesarias.

### Pasos

1. **Instalar Node.js** (si no lo tienes)
   ```bash
   # Verificar instalación
   node --version
   npm --version
   ```
   ✅ Debe mostrar v18.x o superior

2. **Crear proyecto Hardhat**
   ```bash
   mkdir blockchain-practica-01
   cd blockchain-practica-01
   npm init -y
   npm install --save-dev hardhat
   npx hardhat
   ```
   ✅ Selecciona "Create a JavaScript project"

3. **Instalar dependencias**
   ```bash
   npm install --save-dev @nomicfoundation/hardhat-toolbox
   npm install --save-dev @nomicfoundation/hardhat-ethers ethers
   ```
   ✅ Sin errores en la instalación

4. **Verificar estructura**
   ```bash
   ls -la
   ```
   ✅ Debe existir: contracts/, scripts/, test/, hardhat.config.js

### Validación
- [ ] Node.js instalado correctamente
- [ ] Proyecto Hardhat inicializado
- [ ] Dependencias instaladas
- [ ] Estructura de carpetas correcta

---

## Ejercicio 2: Tu Primer Smart Contract (25 min)

### Objetivo
Crear, compilar y desplegar tu primer contrato inteligente.

### Pasos

1. **Crear el contrato HelloBlockchain.sol**
   
   Crea `contracts/HelloBlockchain.sol`:
   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.19;

   contract HelloBlockchain {
       string public message;
       uint256 public updateCount;

       event MessageChanged(string newMessage, address changedBy);

       constructor(string memory _initialMessage) {
           message = _initialMessage;
           updateCount = 0;
       }

       function setMessage(string memory _newMessage) public {
           message = _newMessage;
           updateCount++;
           emit MessageChanged(_newMessage, msg.sender);
       }

       function getMessage() public view returns (string memory) {
           return message;
       }
   }
   ```

2. **Compilar**
   ```bash
   npx hardhat compile
   ```
   ✅ Debe mostrar "Compiled 1 Solidity file successfully"

3. **Crear script de despliegue**
   
   Crea `scripts/deploy-hello.js`:
   ```javascript
   const hre = require("hardhat");

   async function main() {
     const HelloBlockchain = await hre.ethers.getContractFactory("HelloBlockchain");
     const hello = await HelloBlockchain.deploy("¡Mi primer mensaje en blockchain!");
     
     await hello.waitForDeployment();
     
     console.log("✅ Contrato desplegado en:", await hello.getAddress());
     console.log("📝 Mensaje:", await hello.getMessage());
   }

   main().catch((error) => {
     console.error(error);
     process.exit(1);
   });
   ```

4. **Iniciar nodo local** (terminal 1)
   ```bash
   npx hardhat node
   ```
   ✅ Debe mostrar 20 cuentas con ETH

5. **Desplegar contrato** (terminal 2)
   ```bash
   npx hardhat run scripts/deploy-hello.js --network localhost
   ```
   ✅ Debe mostrar dirección del contrato

### Validación
- [ ] Contrato compilado sin errores
- [ ] Nodo local ejecutándose
- [ ] Contrato desplegado
- [ ] Dirección del contrato obtenida

---

## Ejercicio 3: Interactuar con el Contrato (20 min)

### Objetivo
Leer y escribir datos en tu contrato desplegado.

### Pasos

1. **Crear script de interacción**
   
   Crea `scripts/interact-hello.js`:
   ```javascript
   const hre = require("hardhat");

   async function main() {
     // REEMPLAZA con la dirección de tu contrato desplegado
     const contractAddress = "TU_DIRECCION_AQUI";
     
     const HelloBlockchain = await hre.ethers.getContractFactory("HelloBlockchain");
     const hello = HelloBlockchain.attach(contractAddress);

     console.log("1️⃣ Leyendo mensaje inicial...");
     const msg1 = await hello.getMessage();
     console.log("   Mensaje:", msg1);
     
     console.log("\n2️⃣ Actualizando mensaje...");
     const tx = await hello.setMessage("¡Blockchain es increíble!");
     await tx.wait();
     console.log("   ✅ Transacción confirmada");
     
     console.log("\n3️⃣ Leyendo mensaje actualizado...");
     const msg2 = await hello.getMessage();
     console.log("   Mensaje:", msg2);
     
     console.log("\n4️⃣ Contador de actualizaciones...");
     const count = await hello.updateCount();
     console.log("   Actualizaciones:", count.toString());
   }

   main().catch((error) => {
     console.error(error);
     process.exit(1);
   });
   ```

2. **Ejecutar interacción**
   ```bash
   npx hardhat run scripts/interact-hello.js --network localhost
   ```

### Validación
- [ ] Script lee mensaje inicial
- [ ] Script actualiza mensaje
- [ ] Contador incrementa correctamente
- [ ] Todas las operaciones se ejecutan sin error

---

## Ejercicio 4: Testing Automatizado (25 min)

### Objetivo
Escribir y ejecutar tests para validar tu contrato.

### Pasos

1. **Crear archivo de test**
   
   Crea `test/HelloBlockchain.test.js`:
   ```javascript
   const { expect } = require("chai");
   const { ethers } = require("hardhat");

   describe("HelloBlockchain Contract", function () {
     let hello;
     let owner;
     let addr1;
     let addr2;

     beforeEach(async function () {
       [owner, addr1, addr2] = await ethers.getSigners();
       
       const HelloBlockchain = await ethers.getContractFactory("HelloBlockchain");
       hello = await HelloBlockchain.deploy("Mensaje inicial de test");
       await hello.waitForDeployment();
     });

     describe("Deployment", function () {
       it("Debe establecer el mensaje inicial", async function () {
         expect(await hello.getMessage()).to.equal("Mensaje inicial de test");
       });

       it("Debe inicializar el contador en 0", async function () {
         expect(await hello.updateCount()).to.equal(0);
       });
     });

     describe("setMessage", function () {
       it("Debe actualizar el mensaje", async function () {
         await hello.setMessage("Nuevo mensaje");
         expect(await hello.getMessage()).to.equal("Nuevo mensaje");
       });

       it("Debe incrementar el contador", async function () {
         await hello.setMessage("Mensaje 1");
         await hello.setMessage("Mensaje 2");
         await hello.setMessage("Mensaje 3");
         expect(await hello.updateCount()).to.equal(3);
       });

       it("Debe emitir evento MessageChanged", async function () {
         await expect(hello.setMessage("Test event"))
           .to.emit(hello, "MessageChanged")
           .withArgs("Test event", owner.address);
       });
     });

     describe("getMessage", function () {
       it("Debe retornar el mensaje actual", async function () {
         const testMessage = "Mensaje de prueba";
         await hello.setMessage(testMessage);
         expect(await hello.getMessage()).to.equal(testMessage);
       });
     });
   });
   ```

2. **Ejecutar tests**
   ```bash
   npx hardhat test
   ```
   ✅ Todos los tests deben pasar

3. **Ver cobertura** (opcional)
   ```bash
   npx hardhat coverage
   ```

### Validación
- [ ] 7 tests pasan exitosamente
- [ ] No hay errores de compilación
- [ ] Tests verifican deployment
- [ ] Tests verifican funcionalidad

---

## Ejercicio 5: Configurar Docker (30 min)

### Objetivo
Crear un entorno contenerizado para desarrollo reproducible.

### Pasos

1. **Crear Dockerfile**
   
   Crea `Dockerfile`:
   ```dockerfile
   FROM node:18-alpine

   WORKDIR /app

   # Instalar dependencias del sistema
   RUN apk add --no-cache git python3 make g++

   # Copiar package files
   COPY package*.json ./

   # Instalar dependencias npm
   RUN npm install

   # Copiar código fuente
   COPY . .

   # Compilar contratos
   RUN npx hardhat compile

   # Exponer puerto para Hardhat node
   EXPOSE 8545

   CMD ["npx", "hardhat", "node"]
   ```

2. **Crear docker-compose.yml**
   
   Crea `docker-compose.yml`:
   ```yaml
   version: '3.8'

   services:
     hardhat-node:
       build: .
       container_name: web3-hardhat-node
       ports:
         - "8545:8545"
       volumes:
         - ./contracts:/app/contracts
         - ./scripts:/app/scripts
         - ./test:/app/test
       networks:
         - web3-net

   networks:
     web3-net:
       driver: bridge
   ```

3. **Crear .dockerignore**
   
   Crea `.dockerignore`:
   ```
   node_modules
   cache
   artifacts
   .env
   .git
   coverage
   ```

4. **Construir y ejecutar**
   ```bash
   # Construir imagen
   docker-compose build

   # Iniciar nodo
   docker-compose up

   # En otra terminal, desplegar
   docker-compose exec hardhat-node npx hardhat run scripts/deploy-hello.js --network localhost
   ```

### Validación
- [ ] Imagen Docker construida exitosamente
- [ ] Container se inicia sin errores
- [ ] Nodo Hardhat accesible en localhost:8545
- [ ] Puede desplegar contratos desde container

---

## Ejercicio 6: Configurar MetaMask (15 min)

### Objetivo
Conectar MetaMask a tu nodo local para interacciones manuales.

### Pasos

1. **Instalar MetaMask**
   - Ir a https://metamask.io/
   - Instalar extensión en tu navegador
   - Crear nueva wallet (guarda tu frase secreta)

2. **Agregar red local**
   - Abrir MetaMask
   - Configuración → Redes → Agregar Red
   - Completar:
     ```
     Network Name: Localhost 8545
     RPC URL: http://127.0.0.1:8545
     Chain ID: 31337
     Currency Symbol: ETH
     ```

3. **Importar cuenta de prueba**
   - Cuando ejecutas `npx hardhat node`, muestra 20 cuentas
   - Copia la clave privada de Account #0
   - En MetaMask: Importar Cuenta → Pegar clave privada

4. **Verificar balance**
   - Deberías ver 10000 ETH en la cuenta importada

### Validación
- [ ] MetaMask instalado
- [ ] Red local agregada
- [ ] Cuenta de prueba importada
- [ ] Balance de 10000 ETH visible

---

## 🏆 Desafío Bonus: Contrato Personalizado (45 min)

### Objetivo
Aplicar lo aprendido creando tu propio contrato.

### Tarea
Crea un contrato `Counter.sol` que:
- Tenga un contador que inicia en 0
- Función `increment()` que suma 1
- Función `decrement()` que resta 1
- Función `reset()` que vuelve a 0
- Función `getValue()` que retorna el valor actual
- Emita eventos para cada operación

### Pasos
1. Crear `contracts/Counter.sol`
2. Escribir tests en `test/Counter.test.js`
3. Crear script de despliegue
4. Crear script de interacción
5. Desplegar y probar en red local

### Código de Inicio

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Counter {
    int256 private counter;

    event Incremented(int256 newValue);
    event Decremented(int256 newValue);
    event Reset();

    constructor() {
        counter = 0;
    }

    function increment() public {
        // TU CÓDIGO AQUÍ
    }

    function decrement() public {
        // TU CÓDIGO AQUÍ
    }

    function reset() public {
        // TU CÓDIGO AQUÍ
    }

    function getValue() public view returns (int256) {
        // TU CÓDIGO AQUÍ
    }
}
```

### Validación
- [ ] Contrato compila sin errores
- [ ] Tests cubren todas las funciones
- [ ] Script despliega correctamente
- [ ] Puedes interactuar con todas las funciones

---

## 📋 Checklist de Finalización

Antes de avanzar al Módulo 02, asegúrate de haber completado:

### Setup Básico
- [ ] Node.js v18+ instalado
- [ ] Hardhat configurado
- [ ] Proyecto inicializado
- [ ] Dependencias instaladas

### Desarrollo
- [ ] HelloBlockchain compilado y desplegado
- [ ] Tests escritos y pasando
- [ ] Scripts de deploy e interact funcionando
- [ ] Nodo local ejecutándose

### Docker
- [ ] Dockerfile creado
- [ ] docker-compose.yml configurado
- [ ] Imagen construida exitosamente
- [ ] Container ejecutándose

### Herramientas
- [ ] MetaMask instalado y configurado
- [ ] Red local agregada
- [ ] Cuenta de prueba importada
- [ ] Capaz de enviar transacciones

### Bonus (Opcional)
- [ ] Contrato Counter completado
- [ ] Tests del Counter pasando
- [ ] Experimentado con modificaciones

---

## 💡 Tips y Trucos

1. **Nodo bloqueado**: Si el nodo Hardhat se congela, usa Ctrl+C y reinicia
2. **Gas estimado incorrecto**: Limpia cache con `npx hardhat clean`
3. **Contratos no se actualizan**: Recompila con `npx hardhat compile --force`
4. **MetaMask muestra balance incorrecto**: Reinicia la red local y reinicia MetaMask
5. **Tests fallan aleatoriamente**: Usa `beforeEach` para setup limpio en cada test

---

## 🎯 Resultado Esperado

Al completar estos ejercicios deberías tener:
- Entorno de desarrollo completamente funcional
- Al menos 2 contratos funcionando (HelloBlockchain y Counter)
- Suite de tests automatizados
- Capacidad de desplegar en red local
- Docker configurado para reproducibilidad
- MetaMask conectado y funcional

**Tiempo total estimado**: 2-3 horas

---

**¡Excelente trabajo! 🚀** Ahora tienes las bases para comenzar a desarrollar aplicaciones blockchain. Continúa con el Módulo 02 para aprender sobre criptografía.
