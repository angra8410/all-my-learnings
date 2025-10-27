# Retroalimentación y Soluciones - Módulo 01: Introducción y Setup

## ✅ Soluciones a los Ejercicios

---

## Ejercicio 1: Setup Completo del Entorno

### Validación de Éxito

Si completaste correctamente:
- `node --version` muestra v18.0.0 o superior
- `npx hardhat` crea proyecto sin errores
- Carpetas `contracts/`, `scripts/`, `test/` existen
- Archivo `hardhat.config.js` fue creado

### Problemas Comunes

**Error: "command not found: node"**
- **Solución**: Instala Node.js desde nodejs.org o usa nvm
- Verifica PATH con `echo $PATH`

**Error: "hardhat: command not found"**
- **Solución**: Usa `npx hardhat` en lugar de `hardhat`
- O instala globalmente: `npm install -g hardhat`

**Error en npm install**
- **Solución**: Limpia cache con `npm cache clean --force`
- Elimina `node_modules` y vuelve a instalar

---

## Ejercicio 2: Tu Primer Smart Contract

### Solución Completa - HelloBlockchain.sol

El contrato correcto debe verse así:

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

### Análisis del Código

**Línea 1-2**: Licencia y versión
- `MIT` es la licencia más permisiva
- `^0.8.19` significa versión 0.8.19 o superior (pero menor a 0.9.0)

**Variables de estado**:
- `string public message`: Almacenada en blockchain, accesible públicamente
- `uint256 public updateCount`: Contador de actualizaciones

**Constructor**:
- Se ejecuta UNA SOLA VEZ al desplegar
- Inicializa el estado del contrato

**Event MessageChanged**:
- Los eventos son registros en la blockchain
- Permiten a las DApps escuchar cambios
- Más baratos que almacenar datos

**Función setMessage**:
- `public`: Cualquiera puede llamarla
- Modifica estado (cuesta gas)
- Emite evento para notificar cambios

**Función getMessage**:
- `view`: Solo lee, no modifica estado
- No cuesta gas cuando se llama externamente
- Retorna el mensaje actual

### Compilación Exitosa

Deberías ver:
```
Compiled 1 Solidity file successfully
```

Archivos generados en:
- `artifacts/`: Bytecode compilado
- `cache/`: Cache de compilación

### Despliegue Exitoso

Output esperado:
```
✅ Contrato desplegado en: 0x5FbDB2315678afecb367f032d93F642f64180aa3
📝 Mensaje: ¡Mi primer mensaje en blockchain!
```

La dirección será diferente cada vez que reinicies el nodo local.

---

## Ejercicio 3: Interactuar con el Contrato

### Script de Interacción Completo

```javascript
const hre = require("hardhat");

async function main() {
  // Dirección obtenida del ejercicio anterior
  const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
  
  const HelloBlockchain = await hre.ethers.getContractFactory("HelloBlockchain");
  const hello = HelloBlockchain.attach(contractAddress);

  console.log("=== INTERACTUANDO CON HELLO BLOCKCHAIN ===\n");

  // Operación 1: Leer mensaje inicial
  console.log("1️⃣ Leyendo mensaje inicial...");
  const msg1 = await hello.getMessage();
  console.log(`   📝 Mensaje: "${msg1}"`);
  console.log(`   📊 Contador: ${await hello.updateCount()}`);
  
  // Operación 2: Actualizar mensaje
  console.log("\n2️⃣ Actualizando mensaje...");
  const tx1 = await hello.setMessage("¡Blockchain es increíble!");
  console.log(`   ⏳ Esperando confirmación...`);
  const receipt1 = await tx1.wait();
  console.log(`   ✅ Confirmado en bloque: ${receipt1.blockNumber}`);
  
  // Operación 3: Leer mensaje actualizado
  console.log("\n3️⃣ Leyendo mensaje actualizado...");
  const msg2 = await hello.getMessage();
  console.log(`   📝 Mensaje: "${msg2}"`);
  console.log(`   📊 Contador: ${await hello.updateCount()}`);
  
  // Operación 4: Segunda actualización
  console.log("\n4️⃣ Segunda actualización...");
  const tx2 = await hello.setMessage("¡Web3 es el futuro!");
  await tx2.wait();
  console.log(`   ✅ Confirmado`);
  console.log(`   📊 Contador final: ${await hello.updateCount()}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```

### Output Esperado

```
=== INTERACTUANDO CON HELLO BLOCKCHAIN ===

1️⃣ Leyendo mensaje inicial...
   📝 Mensaje: "¡Mi primer mensaje en blockchain!"
   📊 Contador: 0

2️⃣ Actualizando mensaje...
   ⏳ Esperando confirmación...
   ✅ Confirmado en bloque: 2

3️⃣ Leyendo mensaje actualizado...
   📝 Mensaje: "¡Blockchain es increíble!"
   📊 Contador: 1

4️⃣ Segunda actualización...
   ✅ Confirmado
   📊 Contador final: 2
```

### Conceptos Importantes

**await tx.wait()**
- Espera a que la transacción sea minada
- Retorna el recibo de la transacción
- Incluye número de bloque, gas usado, etc.

**Lectura vs Escritura**
- Lectura (`getMessage`): Instantánea, gratis
- Escritura (`setMessage`): Requiere mining, cuesta gas

---

## Ejercicio 4: Testing Automatizado

### Análisis de Tests

**describe y it**
- `describe`: Agrupa tests relacionados
- `it`: Define un test individual

**beforeEach**
- Se ejecuta antes de cada test
- Asegura estado limpio
- Despliega nuevo contrato para cada test

**expect y to.equal**
- Librería Chai para assertions
- Sintaxis expresiva y legible

**Test de Eventos**
```javascript
await expect(hello.setMessage("Test event"))
  .to.emit(hello, "MessageChanged")
  .withArgs("Test event", owner.address);
```
- Verifica que el evento fue emitido
- Valida los argumentos del evento

### Resultado Esperado

```
  HelloBlockchain Contract
    Deployment
      ✔ Debe establecer el mensaje inicial
      ✔ Debe inicializar el contador en 0
    setMessage
      ✔ Debe actualizar el mensaje
      ✔ Debe incrementar el contador
      ✔ Debe emitir evento MessageChanged
    getMessage
      ✔ Debe retornar el mensaje actual

  7 passing (1s)
```

### Debugging de Tests

**Test falla con "expected X to equal Y"**
- Verifica que el valor esperado sea correcto
- Usa `console.log` para ver valores actuales

**Test falla con timeout**
- Aumenta timeout: `this.timeout(5000)`
- Verifica que el nodo local esté corriendo

---

## Ejercicio 5: Configurar Docker

### Dockerfile Explicado

```dockerfile
# Imagen base de Node.js Alpine (ligera)
FROM node:18-alpine

# Directorio de trabajo dentro del container
WORKDIR /app

# Dependencias del sistema necesarias para compilar módulos nativos
RUN apk add --no-cache git python3 make g++

# Copiar archivos de dependencias primero (mejor caching)
COPY package*.json ./

# Instalar dependencias npm
RUN npm install

# Copiar código fuente
COPY . .

# Compilar contratos Solidity
RUN npx hardhat compile

# Exponer puerto 8545 para el nodo Hardhat
EXPOSE 8545

# Comando por defecto al iniciar container
CMD ["npx", "hardhat", "node"]
```

### docker-compose.yml Explicado

```yaml
version: '3.8'

services:
  hardhat-node:
    build: .  # Construye desde Dockerfile en directorio actual
    container_name: web3-hardhat-node
    ports:
      - "8545:8545"  # Mapea puerto del container al host
    volumes:
      # Monta carpetas locales en el container (desarrollo en vivo)
      - ./contracts:/app/contracts
      - ./scripts:/app/scripts
      - ./test:/app/test
    networks:
      - web3-net

networks:
  web3-net:
    driver: bridge  # Red privada para containers
```

### Comandos Docker Útiles

```bash
# Ver containers corriendo
docker ps

# Ver logs del container
docker-compose logs -f

# Ejecutar comando en container
docker-compose exec hardhat-node npx hardhat compile

# Detener containers
docker-compose down

# Reconstruir imagen
docker-compose build --no-cache

# Limpiar todo (containers, imágenes, volúmenes)
docker-compose down -v
docker system prune -a
```

---

## Ejercicio 6: Configurar MetaMask

### Configuración Paso a Paso

**Red Local - Configuración Completa**:
```
Network Name: Localhost 8545
New RPC URL: http://127.0.0.1:8545
Chain ID: 31337
Currency Symbol: ETH
Block Explorer URL: (dejar vacío)
```

**Importar Cuenta de Prueba**:

Cuando ejecutas `npx hardhat node`, ves:
```
Account #0: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
Private Key: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
```

Copia la Private Key (SIN el prefijo 0x si da error) y pégala en MetaMask.

### Problemas Comunes

**"Nonce too high"**
- MetaMask guardó estado viejo
- **Solución**: Configuración → Avanzado → Reiniciar Cuenta

**"No se puede conectar a la red"**
- Verifica que el nodo local esté corriendo
- Verifica la URL: http://127.0.0.1:8545 (no https)

**Balance no aparece**
- Asegúrate de estar en la red "Localhost 8545"
- Verifica que importaste la cuenta correcta

---

## 🏆 Desafío Bonus: Solución Completa - Counter.sol

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
        counter += 1;
        emit Incremented(counter);
    }

    function decrement() public {
        counter -= 1;
        emit Decremented(counter);
    }

    function reset() public {
        counter = 0;
        emit Reset();
    }

    function getValue() public view returns (int256) {
        return counter;
    }
}
```

### Tests para Counter

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Counter", function () {
  let counter;

  beforeEach(async function () {
    const Counter = await ethers.getContractFactory("Counter");
    counter = await Counter.deploy();
    await counter.waitForDeployment();
  });

  it("Debe inicializar en 0", async function () {
    expect(await counter.getValue()).to.equal(0);
  });

  it("Debe incrementar correctamente", async function () {
    await counter.increment();
    expect(await counter.getValue()).to.equal(1);
    
    await counter.increment();
    expect(await counter.getValue()).to.equal(2);
  });

  it("Debe decrementar correctamente", async function () {
    await counter.decrement();
    expect(await counter.getValue()).to.equal(-1);
  });

  it("Debe resetear a 0", async function () {
    await counter.increment();
    await counter.increment();
    await counter.reset();
    expect(await counter.getValue()).to.equal(0);
  });

  it("Debe emitir evento Incremented", async function () {
    await expect(counter.increment())
      .to.emit(counter, "Incremented")
      .withArgs(1);
  });

  it("Debe emitir evento Decremented", async function () {
    await expect(counter.decrement())
      .to.emit(counter, "Decremented")
      .withArgs(-1);
  });

  it("Debe emitir evento Reset", async function () {
    await counter.increment();
    await expect(counter.reset())
      .to.emit(counter, "Reset");
  });
});
```

---

## 📊 Criterios de Evaluación

### Nivel Principiante ⭐
- [ ] Instaló todas las herramientas
- [ ] Compiló y desplegó HelloBlockchain
- [ ] Ejecutó tests básicos

### Nivel Intermedio ⭐⭐
- [ ] Configuró Docker exitosamente
- [ ] Escribió scripts de interacción
- [ ] Configuró MetaMask

### Nivel Avanzado ⭐⭐⭐
- [ ] Completó desafío Counter
- [ ] Escribió tests comprehensivos
- [ ] Experimentó con modificaciones

---

## 💡 Mejores Prácticas Aprendidas

1. **Siempre compila antes de desplegar**
   ```bash
   npx hardhat compile
   ```

2. **Usa variables para direcciones de contratos**
   ```javascript
   const contractAddress = process.env.CONTRACT_ADDRESS;
   ```

3. **Espera confirmación de transacciones**
   ```javascript
   const tx = await contract.setMessage("...");
   await tx.wait();
   ```

4. **Limpia antes de rebuild**
   ```bash
   npx hardhat clean
   npx hardhat compile
   ```

5. **Reinicia MetaMask si algo se rompe**
   - Settings → Advanced → Reset Account

---

## 🔍 Troubleshooting Guide

### Problema: Compilación falla
```
Error HH600: Compilation failed
```
**Solución**:
- Verifica sintaxis de Solidity
- Asegúrate de tener `// SPDX-License-Identifier:`
- Limpia con `npx hardhat clean`

### Problema: Despliegue falla
```
Error: cannot estimate gas
```
**Solución**:
- Verifica que el nodo local esté corriendo
- Revisa el constructor del contrato
- Asegúrate de tener ETH en la cuenta

### Problema: Tests no pasan
```
Error: Timeout of 2000ms exceeded
```
**Solución**:
- Aumenta timeout en el test
- Verifica conexión a red local
- Limpia y recompila

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Hardhat Docs](https://hardhat.org/getting-started/)
- [Solidity Docs](https://docs.soliditylang.org/)
- [Ethers.js Docs](https://docs.ethers.org/)

### Tutoriales Recomendados
- [Hardhat Tutorial](https://hardhat.org/tutorial)
- [Solidity by Example](https://solidity-by-example.org/)
- [Ethers.js Workshop](https://docs.ethers.org/v5/getting-started/)

### Comunidades
- [Hardhat Discord](https://hardhat.org/discord)
- [Ethereum StackExchange](https://ethereum.stackexchange.com/)
- [r/ethdev](https://reddit.com/r/ethdev)

---

## ✅ Checklist Final

Antes de avanzar al Módulo 02:

- [ ] Entorno completamente funcional
- [ ] HelloBlockchain compilado, desplegado y testeado
- [ ] Docker configurado y funcional
- [ ] MetaMask conectado a red local
- [ ] Capaz de escribir, compilar y testear contratos
- [ ] Comprendo el flujo de desarrollo completo

---

**¡Felicidades! 🎉** Has completado el Módulo 01. Ahora tienes un entorno sólido para desarrollar en Web3.

**Próximo paso**: Módulo 02 - Fundamentos de Criptografía
