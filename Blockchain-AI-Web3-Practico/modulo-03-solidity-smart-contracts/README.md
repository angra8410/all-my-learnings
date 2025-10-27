# Módulo 03: Solidity y Smart Contracts

## 🎯 Objetivos del Módulo

1. Dominar sintaxis y tipos de datos de Solidity
2. Implementar patterns comunes (Ownable, Pausable)
3. Crear token ERC-20 completo
4. Trabajar con herencia e interfaces
5. Manejo de eventos y modificadores
6. Optimización de gas

**Duración**: 4-5 horas

## 📚 Sintaxis Básica de Solidity

### Tipos de Datos

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract TiposDeDatos {
    // Enteros
    uint256 public numeroPositivo;  // 0 a 2^256-1
    int256 public numeroConSigno;   // -2^255 a 2^255-1
    
    // Booleanos
    bool public estaActivo = true;
    
    // Direcciones
    address public owner;
    address payable public recipient;
    
    // Strings
    string public nombre = "MiContrato";
    
    // Bytes
    bytes32 public hash;
    bytes public data;
    
    // Arrays
    uint256[] public arrayDinamico;
    uint256[5] public arrayFijo;
    
    // Mappings
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;
    
    // Structs
    struct Usuario {
        string nombre;
        uint256 edad;
        bool activo;
    }
    Usuario[] public usuarios;
    
    // Enums
    enum Estado { Pendiente, Activo, Cancelado }
    Estado public estadoActual;
}
```

### Funciones y Modificadores

```solidity
contract Funciones {
    address public owner;
    uint256 public contador;
    
    event ContadorActualizado(uint256 nuevoValor);
    
    constructor() {
        owner = msg.sender;
    }
    
    // Modificador personalizado
    modifier soloPropietario() {
        require(msg.sender == owner, "No eres el propietario");
        _;
    }
    
    // Función public
    function incrementar() public soloPropietario {
        contador++;
        emit ContadorActualizado(contador);
    }
    
    // Función view (solo lee)
    function obtenerContador() public view returns (uint256) {
        return contador;
    }
    
    // Función pure (sin estado)
    function sumar(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }
    
    // Función payable (recibe ETH)
    function depositar() public payable {
        // msg.value contiene ETH enviado
    }
    
    // Función internal (solo dentro del contrato)
    function _funcionInterna() internal pure returns (uint256) {
        return 42;
    }
}
```

## 🎨 Token ERC-20 Completo

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ERC20Token {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        totalSupply = _initialSupply * 10**decimals;
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }
    
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Direccion invalida");
        require(balanceOf[msg.sender] >= _value, "Saldo insuficiente");
        
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        
        emit Transfer(msg.sender, _to, _value);
        return true;
    }
    
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }
    
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Direccion invalida");
        require(balanceOf[_from] >= _value, "Saldo insuficiente");
        require(allowance[_from][msg.sender] >= _value, "Allowance insuficiente");
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        
        emit Transfer(_from, _to, _value);
        return true;
    }
    
    function mint(address _to, uint256 _amount) external {
        require(_to != address(0), "Direccion invalida");
        
        totalSupply += _amount;
        balanceOf[_to] += _amount;
        
        emit Transfer(address(0), _to, _amount);
    }
    
    function burn(uint256 _amount) external {
        require(balanceOf[msg.sender] >= _amount, "Saldo insuficiente");
        
        balanceOf[msg.sender] -= _amount;
        totalSupply -= _amount;
        
        emit Transfer(msg.sender, address(0), _amount);
    }
}
```

## 🔐 Pattern: Ownable

```solidity
contract Ownable {
    address public owner;
    
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    constructor() {
        owner = msg.sender;
        emit OwnershipTransferred(address(0), msg.sender);
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "No eres el owner");
        _;
    }
    
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Direccion invalida");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    function renounceOwnership() public onlyOwner {
        emit OwnershipTransferred(owner, address(0));
        owner = address(0);
    }
}
```

## ⏸️ Pattern: Pausable

```solidity
contract Pausable is Ownable {
    bool public paused;
    
    event Paused(address account);
    event Unpaused(address account);
    
    modifier whenNotPaused() {
        require(!paused, "Contrato pausado");
        _;
    }
    
    modifier whenPaused() {
        require(paused, "Contrato no pausado");
        _;
    }
    
    function pause() public onlyOwner whenNotPaused {
        paused = true;
        emit Paused(msg.sender);
    }
    
    function unpause() public onlyOwner whenPaused {
        paused = false;
        emit Unpaused(msg.sender);
    }
}
```

## 🏗️ Herencia e Interfaces

```solidity
// Interfaz
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address to, uint256 amount) external returns (bool);
}

// Contrato base
contract Token {
    string public name;
    uint256 public totalSupply;
    
    constructor(string memory _name) {
        name = _name;
    }
}

// Herencia
contract MyToken is Token, Ownable, Pausable {
    constructor() Token("MiToken") {}
    
    function specialFunction() public onlyOwner whenNotPaused {
        // Combina funcionalidad de ambos contratos padre
    }
}
```

## ⛽ Optimización de Gas

```solidity
contract GasOptimization {
    // ❌ MALO: usa más gas
    function malLoop() public pure returns (uint256) {
        uint256 sum = 0;
        for (uint256 i = 0; i < 100; i++) {
            sum = sum + i;  // Operación costosa
        }
        return sum;
    }
    
    // ✅ BUENO: menos gas
    function buenLoop() public pure returns (uint256) {
        uint256 sum;  // Default a 0
        for (uint256 i; i < 100; ++i) {  // ++i más barato que i++
            sum += i;  // += más barato
        }
        return sum;
    }
    
    // Usar calldata en lugar de memory cuando sea posible
    function procesarDatos(uint256[] calldata datos) external pure returns (uint256) {
        return datos[0];
    }
    
    // Agrupar variables para optimizar storage
    struct Usuario {
        uint128 balance;  // Usa uint128 si 256 no es necesario
        uint128 timestamp;
        bool activo;     // Se empaquetan juntos
        // address nextUser; // Esto iría en otro slot
    }
}
```

## 📝 Script de Despliegue Avanzado

```javascript
const hre = require("hardhat");

async function main() {
  console.log("�� Desplegando Token ERC-20...");
  
  const [deployer] = await hre.ethers.getSigners();
  console.log("Desplegando con cuenta:", deployer.address);
  
  const balance = await hre.ethers.provider.getBalance(deployer.address);
  console.log("Balance:", hre.ethers.formatEther(balance), "ETH");
  
  // Desplegar
  const Token = await hre.ethers.getContractFactory("ERC20Token");
  const token = await Token.deploy("MiToken", "MTK", 1000000);
  
  await token.waitForDeployment();
  
  const address = await token.getAddress();
  console.log("✅ Token desplegado en:", address);
  
  // Verificar datos
  console.log("📋 Verificando...");
  console.log("  Nombre:", await token.name());
  console.log("  Símbolo:", await token.symbol());
  console.log("  Supply:", (await token.totalSupply()).toString());
  console.log("  Decimals:", await token.decimals());
  
  // Hacer algunas transferencias de prueba
  const recipient = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8";
  const amount = hre.ethers.parseEther("100");
  
  console.log("\n💸 Transfiriendo 100 tokens...");
  const tx = await token.transfer(recipient, amount);
  await tx.wait();
  console.log("  Balance destino:", (await token.balanceOf(recipient)).toString());
  
  console.log("\n✨ Despliegue completado!");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

## 🧪 Tests Comprehensivos

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ERC20Token", function () {
  let token;
  let owner, addr1, addr2;
  const INITIAL_SUPPLY = 1000000;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    const Token = await ethers.getContractFactory("ERC20Token");
    token = await Token.deploy("TestToken", "TT", INITIAL_SUPPLY);
  });

  describe("Deployment", function () {
    it("Debe asignar supply total al owner", async function () {
      const ownerBalance = await token.balanceOf(owner.address);
      expect(await token.totalSupply()).to.equal(ownerBalance);
    });

    it("Debe establecer nombre y símbolo correctamente", async function () {
      expect(await token.name()).to.equal("TestToken");
      expect(await token.symbol()).to.equal("TT");
    });
  });

  describe("Transacciones", function () {
    it("Debe transferir tokens entre cuentas", async function () {
      await token.transfer(addr1.address, 50);
      expect(await token.balanceOf(addr1.address)).to.equal(50);
      
      await token.connect(addr1).transfer(addr2.address, 50);
      expect(await token.balanceOf(addr2.address)).to.equal(50);
      expect(await token.balanceOf(addr1.address)).to.equal(0);
    });

    it("Debe fallar si sender no tiene suficientes tokens", async function () {
      await expect(
        token.connect(addr1).transfer(owner.address, 1)
      ).to.be.revertedWith("Saldo insuficiente");
    });

    it("Debe actualizar balances después de transferencias", async function () {
      const initialOwnerBalance = await token.balanceOf(owner.address);
      await token.transfer(addr1.address, 100);
      await token.transfer(addr2.address, 50);
      
      const finalOwnerBalance = await token.balanceOf(owner.address);
      expect(finalOwnerBalance).to.equal(initialOwnerBalance - BigInt(150));
    });
  });

  describe("Allowances", function () {
    it("Debe aprobar y usar allowance correctamente", async function () {
      await token.approve(addr1.address, 100);
      expect(await token.allowance(owner.address, addr1.address)).to.equal(100);
      
      await token.connect(addr1).transferFrom(owner.address, addr2.address, 50);
      expect(await token.balanceOf(addr2.address)).to.equal(50);
      expect(await token.allowance(owner.address, addr1.address)).to.equal(50);
    });
  });
});
```

**Siguiente**: Módulo 04 - Testing y Security Básico
