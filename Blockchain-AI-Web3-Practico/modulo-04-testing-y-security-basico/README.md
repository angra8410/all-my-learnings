# Módulo 04: Testing y Security Básico

## 🎯 Objetivos

1. Escribir tests comprehensivos con Hardhat y Chai
2. Alcanzar alta cobertura de código
3. Identificar vulnerabilidades comunes
4. Implementar patterns de seguridad
5. Usar herramientas de análisis (Slither básico)
6. Aplicar Checks-Effects-Interactions

**Duración**: 3-4 horas

## 🧪 Testing Avanzado con Hardhat

### Setup de Tests

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");
const { loadFixture, time } = require("@nomicfoundation/hardhat-network-helpers");

describe("Token Avanzado", function () {
  async function deployTokenFixture() {
    const [owner, addr1, addr2] = await ethers.getSigners();
    const Token = await ethers.getContractFactory("Token");
    const token = await Token.deploy("Test", "TST", 1000000);
    return { token, owner, addr1, addr2 };
  }

  it("Debe manejar transferencias grandes", async function () {
    const { token, owner, addr1 } = await loadFixture(deployTokenFixture);
    const largeAmount = ethers.parseEther("999999");
    await token.transfer(addr1.address, largeAmount);
    expect(await token.balanceOf(addr1.address)).to.equal(largeAmount);
  });

  it("Debe revertir en overflow", async function () {
    const { token, addr1 } = await loadFixture(deployTokenFixture);
    const maxUint = ethers.MaxUint256;
    await expect(
      token.transfer(addr1.address, maxUint)
    ).to.be.revertedWith("Insufficient balance");
  });
});
```

### Test de Eventos

```javascript
it("Debe emitir evento Transfer correcto", async function () {
  const { token, owner, addr1 } = await loadFixture(deployTokenFixture);
  const amount = ethers.parseEther("100");
  
  await expect(token.transfer(addr1.address, amount))
    .to.emit(token, "Transfer")
    .withArgs(owner.address, addr1.address, amount);
});
```

### Test de Time-based Logic

```javascript
it("Debe permitir unlock después del tiempo", async function () {
  const { token } = await loadFixture(deployTokenFixture);
  
  // Avanzar tiempo 1 día
  await time.increase(86400);
  
  await token.unlock();
  expect(await token.isUnlocked()).to.be.true;
});
```

## 🔒 Vulnerabilidades Comunes

### 1. Reentrancy Attack

```solidity
// ❌ VULNERABLE
contract VulnerableBank {
    mapping(address => uint256) public balances;
    
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        // PELIGRO: llamada externa antes de actualizar estado
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success);
        balances[msg.sender] = 0;  // Demasiado tarde!
    }
}

// ✅ SEGURO - Checks-Effects-Interactions
contract SecureBank {
    mapping(address => uint256) public balances;
    
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        // Checks
        require(amount > 0, "No balance");
        
        // Effects (actualizar estado PRIMERO)
        balances[msg.sender] = 0;
        
        // Interactions (llamadas externas AL FINAL)
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}

// ✅ MÁS SEGURO - ReentrancyGuard
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SafeBank is ReentrancyGuard {
    mapping(address => uint256) public balances;
    
    function withdraw() public nonReentrant {
        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success);
    }
}
```

### 2. Integer Overflow/Underflow

```solidity
// ❌ VULNERABLE (Solidity <0.8.0)
contract VulnerableCounter {
    uint8 public counter = 255;
    
    function increment() public {
        counter++;  // Overflow a 0
    }
}

// ✅ SEGURO (Solidity >=0.8.0)
contract SafeCounter {
    uint8 public counter = 255;
    
    function increment() public {
        counter++;  // Auto-revierte en overflow
    }
}

// ✅ EXTRA SEGURO - Validación explícita
contract ExtraSafeCounter {
    uint8 public counter;
    
    function increment() public {
        require(counter < 255, "Overflow protection");
        counter++;
    }
}
```

### 3. Access Control

```solidity
// ❌ VULNERABLE
contract VulnerableVault {
    function withdraw() public {
        // Cualquiera puede retirar!
        payable(msg.sender).transfer(address(this).balance);
    }
}

// ✅ SEGURO
import "@openzeppelin/contracts/access/Ownable.sol";

contract SecureVault is Ownable {
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```

### 4. Unchecked External Calls

```solidity
// ❌ VULNERABLE
contract VulnerablePayment {
    function pay(address recipient) public payable {
        recipient.call{value: msg.value}("");  // Ignora el return!
    }
}

// ✅ SEGURO
contract SecurePayment {
    function pay(address recipient) public payable {
        (bool success, ) = recipient.call{value: msg.value}("");
        require(success, "Payment failed");
    }
}
```

## 🛡️ Security Patterns

### Pull over Push Pattern

```solidity
// ❌ PUSH (riesgoso)
contract PushPayment {
    function distributeRewards(address[] memory recipients) public {
        for (uint i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(1 ether);  // Puede fallar
        }
    }
}

// ✅ PULL (seguro)
contract PullPayment {
    mapping(address => uint256) public pendingWithdrawals;
    
    function addReward(address recipient) public {
        pendingWithdrawals[recipient] += 1 ether;
    }
    
    function withdraw() public {
        uint256 amount = pendingWithdrawals[msg.sender];
        require(amount > 0, "No rewards");
        pendingWithdrawals[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
```

### Rate Limiting

```solidity
contract RateLimited {
    mapping(address => uint256) public lastActionTime;
    uint256 public constant COOLDOWN = 1 hours;
    
    modifier rateLimited() {
        require(
            block.timestamp >= lastActionTime[msg.sender] + COOLDOWN,
            "Too soon"
        );
        lastActionTime[msg.sender] = block.timestamp;
        _;
    }
    
    function sensitiveAction() public rateLimited {
        // Acción limitada por tiempo
    }
}
```

## 📊 Code Coverage

```bash
# Instalar plugin de coverage
npm install --save-dev solidity-coverage

# Ejecutar coverage
npx hardhat coverage
```

**hardhat.config.js**:
```javascript
require("solidity-coverage");

module.exports = {
  solidity: "0.8.19",
};
```

## 🔍 Análisis Estático con Slither

```bash
# Instalar Slither
pip3 install slither-analyzer

# Analizar contrato
slither contracts/MyContract.sol
```

## 🧪 Tests de Seguridad

```javascript
describe("Security Tests", function () {
  it("Debe prevenir reentrancy", async function () {
    const Attacker = await ethers.getContractFactory("ReentrancyAttacker");
    const attacker = await Attacker.deploy(bank.address);
    
    await expect(
      attacker.attack({value: ethers.parseEther("1")})
    ).to.be.revertedWith("ReentrancyGuard");
  });

  it("Debe prevenir overflow", async function () {
    await expect(
      token.transfer(addr1.address, ethers.MaxUint256)
    ).to.be.reverted;
  });

  it("Debe requerir ownership", async function () {
    await expect(
      contract.connect(addr1).adminFunction()
    ).to.be.revertedWith("Ownable: caller is not the owner");
  });
});
```

## 📚 Checklist de Seguridad

Antes de desplegar:

- [ ] Usa Solidity >= 0.8.0 (protección overflow)
- [ ] Implementa Checks-Effects-Interactions
- [ ] Usa ReentrancyGuard en funciones con external calls
- [ ] Valida todos los inputs
- [ ] Usa access control (Ownable, AccessControl)
- [ ] Verifica return values de external calls
- [ ] Limita gas donde sea apropiado
- [ ] Implementa emergency stop (Pausable)
- [ ] Ejecuta Slither o similar
- [ ] Code coverage > 90%
- [ ] Auditoría por peers

**Siguiente**: Módulo 05 - DApps Frontend
